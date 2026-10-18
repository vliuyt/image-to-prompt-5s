"""Run paired Codex vision requests without fixture answers or answer-key exposure.

Development-only harness. It uses existing Codex authentication, never reads it,
and leaves private CLI context/events in an ignored work directory.
"""

import argparse
import concurrent.futures
import hashlib
import json
import random
import secrets
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent.parent
SKILL = REPO / "skills" / "image-to-prompt-5s"
MODEL = "gpt-6.1-sol"
DISABLED_SKILL = str(Path.home() / ".codex/skills/image-to-prompt-5s/SKILL.md")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def skill_instructions():
    names = ["SKILL.md", "references/analysis-guide.md", "references/output-template.md",
             "references/delivery-checklist.md", "references/examples.md"]
    return "\n\n".join(f"--- {name} ---\n{(SKILL / name).read_text()}" for name in names)


def safe_fixture(name):
    path = (ROOT / "fixtures" / name).resolve()
    if path.parent != (ROOT / "fixtures").resolve() or not path.is_file():
        raise ValueError(f"Unsafe or absent fixture: {name}")
    return path


def make_prompt(case, variant, snapshot):
    common = "请完成用户请求。直接交付最终回答；不要调用工具、读取其他文件、联网或生成图片。参考图片按附件顺序提供。\n\n"
    if variant == "with_skill":
        common += "本次使用以下图片提示词技能。\n" + snapshot + "\n\n"
    return common + "用户请求：\n" + case["user_request"]


def parse_events(events):
    messages, tool_calls, usage, diagnostics, failures = [], [], {}, [], []
    for event in events:
        event_type = event.get("type")
        if event_type in {"error", "turn.failed"}:
            failures.append({"type": event_type, "message": str(event.get("message") or event.get("error", {}).get("message", ""))})
        if event_type == "turn.completed":
            usage = event.get("usage", {})
        if event_type == "item.completed":
            item = event.get("item", {})
            item_type = item.get("type")
            if item_type == "agent_message":
                messages.append(item.get("text", ""))
            elif item_type == "error":
                message = str(item.get("message", ""))
                if message.startswith("clamping SessionEnd hook timeout to 3s in "):
                    diagnostics.append("SessionEnd hook timeout clamped to 3s (host diagnostic)")
                else:
                    failures.append({"type": "item.error", "message": message})
            elif item_type not in {"reasoning", "plan"}:
                tool_calls.append(item_type or "unknown")
    return {"output": "\n\n".join(messages).strip(), "tool_calls": tool_calls,
            "usage": usage, "host_diagnostics": diagnostics, "failure_events": failures}


def run_one(case, variant, work, timeout, snapshot, disabled_config=None):
    case_id = case["case_id"]
    job = work / case_id / variant
    job.mkdir(parents=True, exist_ok=False)
    prompt = make_prompt(case, variant, snapshot)
    images = [safe_fixture(ref["filename"]) for ref in case["references"]]
    command = ["codex", "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check",
               "--sandbox", "read-only", "--color", "never", "--json", "--model", MODEL,
               "-c", 'model_reasoning_effort="medium"',
               "-c", disabled_config or ('skills.config=[{path=' + json.dumps(DISABLED_SKILL) + ',enabled=false}]'),
               "-C", str(job)]
    for image in images:
        command += ["--image", str(image)]
    # A lone '-' consumes stdin. Never put prompts or credential material in shell strings.
    command.append("-")
    start = time.perf_counter()
    (job / "request.txt").write_text(prompt)
    record = {"case_id": case_id, "variant": variant, "provider": "openai",
              "model": MODEL, "model_reporting": "requested model via existing Codex login; no server model attestation",
              "execution_kind": "model", "prompt_sha256": sha(prompt.encode()),
              "input_images": [{"name": p.name, "sha256": sha(p.read_bytes())} for p in images]}
    try:
        result = subprocess.run(command, input=prompt, text=True, capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        for name, data in [("events.jsonl", exc.stdout), ("stderr.log", exc.stderr)]:
            (job / name).write_text(data.decode(errors="replace") if isinstance(data, bytes) else (data or ""))
        record.update(status="failed", failure="model invocation timed out", duration_ms=round((time.perf_counter()-start)*1000, 2))
        return record
    (job / "events.jsonl").write_text(result.stdout)
    (job / "stderr.log").write_text(result.stderr)
    events = []
    for line in result.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    parsed = parse_events(events)
    answer = parsed["output"]
    ok = result.returncode == 0 and bool(answer) and bool(parsed["usage"]) and not parsed["tool_calls"] and not parsed["failure_events"]
    record.update(parsed)
    record.update(status="pass" if ok else "failed", exit_code=result.returncode,
                  output_sha256=sha(answer.encode()), duration_ms=round((time.perf_counter()-start)*1000, 2))
    if not ok:
        record["failure"] = "Nonzero exit, empty output, missing observed usage, or prohibited tool use; inspect private trace."
    return record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--work-dir", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--workers", type=int, choices=(1, 2), default=2)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--disable-skills-file", type=Path,
                        help="Private JSON array of discovered SKILL.md paths to disable in both arms.")
    args = parser.parse_args()
    work, out = args.work_dir.resolve(), args.out.resolve()
    if work.exists() or out.exists():
        parser.error("Use fresh work/output locations; never silently overwrite or rerun selected results.")
    design = json.loads((ROOT / "design.json").read_text())
    cases = design["cases"]
    ids = [c["case_id"] for c in cases]
    if len(set(ids)) != len(ids) or any(Path(x).name != x or x in {".", ".."} for x in ids):
        parser.error("Case IDs must be unique simple directory names.")
    # Validate every input before the first provider call.
    for case in cases:
        for ref in case["references"]:
            safe_fixture(ref["filename"])
    work.mkdir(parents=True)
    out.mkdir(parents=True)
    snapshot = skill_instructions()
    (work / "skill-snapshot.txt").write_text(snapshot)
    disabled = json.loads(args.disable_skills_file.read_text()) if args.disable_skills_file else [DISABLED_SKILL]
    if not isinstance(disabled, list) or not disabled or not all(isinstance(p, str) and Path(p).is_absolute() for p in disabled):
        parser.error("Disabled skill list must contain absolute paths.")
    disabled_config = "skills.config=[" + ",".join("{path=" + json.dumps(p) + ",enabled=false}" for p in disabled) + "]"
    seed = secrets.randbits(64)
    jobs = [(case, variant) for case in cases for variant in ("baseline", "with_skill")]
    random.Random(seed).shuffle(jobs)
    protocol = {"started_at": datetime.now(timezone.utc).isoformat(), "model": MODEL,
                "design_sha256": sha((ROOT / "design.json").read_bytes()),
                "skill_snapshot_sha256": sha(snapshot.encode()),
                "fixture_sha256": {p.name: sha(p.read_bytes()) for p in sorted((ROOT / "fixtures").glob("*.png"))},
                "job_order": [[c["case_id"], v] for c, v in jobs], "random_seed": seed,
                "repetitions": 1, "selection_policy": "all preregistered cases; no selected reruns",
                "skill_in_baseline": False, "tools_permitted": False,
                "disabled_discovery_paths": len(disabled),
                "disabled_discovery_config_sha256": sha(disabled_config.encode()),
                "notes": "Same model, common host context, task and images; only treatment adds frozen skill instructions. Skill disabled in discovery on both arms. Model snapshots still have inherent stochastic variation."}
    (out / "protocol.json").write_text(json.dumps(protocol, ensure_ascii=False, indent=2)+"\n")
    records = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(run_one, case, variant, work, args.timeout, snapshot, disabled_config) for case, variant in jobs]
        for future in concurrent.futures.as_completed(futures):
            record = future.result()
            records.append(record)
            (out / "runs.json").write_text(json.dumps(records, ensure_ascii=False, indent=2)+"\n")
            print(json.dumps({k: record[k] for k in ("case_id", "variant", "status", "duration_ms")}, ensure_ascii=False), flush=True)
    raise SystemExit(0 if all(r["status"] == "pass" for r in records) else 2)


if __name__ == "__main__":
    main()
