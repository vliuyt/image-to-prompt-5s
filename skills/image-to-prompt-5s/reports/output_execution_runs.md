> Evidence scope: recorded v0.1.0 authored examples, identical on both sides. Not a model comparison, not human review, not evidence of improvement. See benchmark_methodology.md.

# Output Execution Runs

This report records how output-eval variants were produced and whether timing or token evidence is observed or estimated.

- Cases: `2`
- Variant runs: `4`
- Command executed: `0`
- Model executed: `0`
- Recorded fixtures: `4`
- Timing observed: `0`
- Token observed: `0`
- Token estimated: `4`
- Delta: `0.0`
- Gate pass: `True`

No model-executed runs are recorded yet.

Use `python3 scripts/yao.py output-exec --provider-runner openai` or `--runner-command` with a reviewed provider-backed runner to replace recorded fixtures with real model output evidence.

## Runs

| Case | Variant | Mode | Model | Duration ms | Tokens | Score | Status |
| --- | --- | --- | --- | ---: | ---: | ---: | --- |
| cup | baseline | recorded_fixture |  |  | 54 | 100.0 | pass |
| cup | tie (identical fixtures) | recorded_fixture |  |  | 54 | 100.0 | pass |
| poster | baseline | recorded_fixture |  |  | 65 | 100.0 | pass |
| poster | tie (identical fixtures) | recorded_fixture |  |  | 65 | 100.0 | pass |

## Next Fixes

- Keep recorded fixtures as reproducible baselines, but do not describe them as model-executed evidence.
- Use `scripts/provider_output_eval_runner.py` for provider-backed holdout cases when release confidence depends on real generation behavior.
- Compare timing, token cost, and assertion deltas before promoting a skill to governed reuse.
