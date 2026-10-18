# Real model and blind review evaluation

This is development tooling, not skill runtime. `render_fixtures.py` creates seven original reference images. Install Pillow 12.1.1 for reproducible rendering, and ensure Arial or DejaVu Sans is available. `run_eval.py` invokes the installed Codex CLI with existing login, requested gpt-6.1-sol, read-only mode, no tool use, fixed skill snapshot and fresh per-cell jobs. It does not read credentials or replay fixture answers.

```sh
python3 -m unittest discover -s evals/live -p test_harness.py -v
python3 evals/live/render_fixtures.py
python3 evals/live/run_eval.py --help
```

Before real paired runs, make a private JSON array of all discovered local SKILL.md paths (include symbolic and resolved paths) and inspect that the tested skill is absent from Codex's model-visible skill catalog. Pass that file with `--disable-skills-file`; never commit it. The target list is per-process config, not a host setting. Packaged host skills may remain, so inspect startup diagnostics and invalidate any context-truncated batch before looking at answer quality.

Use new work/output directories for each batch. The runner refuses to overwrite results. Work directories must stay under an ignored private path because raw CLI events can contain host context. Publish only sanitized model answers and measured usage. The checked-in run-02 uses six held-out visual tasks, one response per arm, 12 successful real calls. Pilot was excluded as a whole; see attempt-inventory.json and protocol amendments.

For independent review, randomize A/B identities, send only reference images, user requests, frozen criteria and unchanged anonymous answers to fresh-context reviewers. Keep the identity key in a separate location, freeze reviewer files and hashes before deblinding, preserve ties, and explicitly disclose model-agent versus human review. Results include the actual pack, reviewer decisions and lock hashes. Our independent rubric is primary; output_cases.jsonl has post-run lexical checks as supplementary smoke assertions, not preregistered efficacy tests.

Built-in image generation was run once per prompt for one preselected case, no reference supplied and no quality-based rerolls. Exact backend model, seed and image-tool usage are not exposed. Results are workflow smoke evidence, not a verified GPT Image 2.5 API benchmark.

See ../../reports/live-evaluation-2026-10-18.md for outcome, limits and all links. New model runs consume account quota; do not run them merely to replay existing results. No human approvals are stored in AI reviewer fields.
