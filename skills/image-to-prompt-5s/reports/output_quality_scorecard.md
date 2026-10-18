> Evidence scope: recorded v0.1.0 authored examples, identical on both sides. Not a model comparison, not human review, not evidence of improvement. See benchmark_methodology.md.

# Output Quality Scorecard

This scorecard runs regression assertions on recorded examples. Column names are generic tool labels.

- Cases: `2`
- Baseline pass rate: `100.0`
- With-skill pass rate: `100.0`
- Delta: `0.0`
- Regressions: `0`
- Blind A/B pairs: `2`
- Gate pass: `True`

Blind review artifacts are generated separately so reviewers can inspect A/B outputs without seeing the answer key.
Run output review adjudication after reviewer decisions are recorded; pending cases should stay pending rather than being counted as human agreement.

## Case Results

| Case | Baseline | With Skill | Delta | Winner | Failed With-Skill Assertions |
| --- | ---: | ---: | ---: | --- | --- |
| cup | 100.0 | 100.0 | 0.0 | tie (identical fixtures) | None |
| poster | 100.0 | 100.0 | 0.0 | tie (identical fixtures) | None |

## Failure Taxonomy

- No with-skill assertion failures.

## Next Fixes

- Add holdout cases before using this as a release gate.
- Promote repeated failed assertions into the output-risk profile.
- Keep assertions tied to material deliverables, not phrasing trivia.
