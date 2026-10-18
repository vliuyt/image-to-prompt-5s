> Scope: real vision-model outputs. Independent model-only blind reviews are in independent_model_review.json and the repository live-evaluation report. Human reviews remain pending; five ties are not forced into A/B wins. Lexical checks are supplementary and post-run.

# Output Quality Scorecard

This v0 scorecard compares static without-skill and with-skill outputs using assertion grading.

- Cases: `6`
- Baseline pass rate: `91.67`
- With-skill pass rate: `100.0`
- Delta: `8.33`
- Regressions: `0`
- Blind A/B pairs: `6`
- Gate pass: `True`

Blind review artifacts are generated separately so reviewers can inspect A/B outputs without seeing the answer key.
Run output review adjudication after reviewer decisions are recorded; pending cases should stay pending rather than being counted as human agreement.

## Case Results

| Case | Baseline | With Skill | Delta | Winner | Failed With-Skill Assertions |
| --- | ---: | ---: | ---: | --- | --- |
| poster_orbit_17 | 100.0 | 100.0 | 0.0 | with_skill | None |
| product_cedar_02 | 50.0 | 100.0 | 50.0 | with_skill | None |
| scene_three_figures | 100.0 | 100.0 | 0.0 | with_skill | None |
| mascot_two_views | 100.0 | 100.0 | 0.0 | with_skill | None |
| local_edit_blue_mug | 100.0 | 100.0 | 0.0 | with_skill | None |
| poster_embedded_command | 100.0 | 100.0 | 0.0 | with_skill | None |

## Failure Taxonomy

- No with-skill assertion failures.

## Next Fixes

- Add holdout cases before using this as a release gate.
- Promote repeated failed assertions into the output-risk profile.
- Keep assertions tied to material deliverables, not phrasing trivia.
