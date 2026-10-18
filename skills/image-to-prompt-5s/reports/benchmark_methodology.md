# Evaluation scope and missing evidence

Trigger cases use Yao's deterministic phrase/concept scorer, not Codex's actual skill router. The 18 cases are authored smoke fixtures, not an independent holdout. Both old and new descriptions passed the same scorer; no measured routing gain is claimed.

Output cases use two authored examples already published in v0.1.0. Both baseline_output and with_skill_output intentionally contain the same original answer. Seven assertions check visual invariants and incompatible syntax; these are regression fixtures, not an empirical without-skill/with-skill experiment. Both sides passing means preservation, not improvement. Generated A/B packs are identical pairs and cannot establish a preference.

missing evidence: provider-backed baseline comparison, visual-model execution, actual GPT Image 2.5 generated-image comparison, independent holdout, human blind review, adoption telemetry. No human reviewer decisions or waivers have been fabricated. An experimental release may document these limitations; it is not production promotion or a quality benchmark claim.

The file-backed fixture input_files are fictional scene descriptions in evals/output/fixtures/*.md. No user screenshot, identity, credential, private attachment or generated image is distributed.

owner: vliuyt. review cadence: per-release. output contract: 0–6 analysis + copyable natural-language prompt. rollback boundary: reinstall the unchanged v0.1.0 package; no host settings or user images are modified.
