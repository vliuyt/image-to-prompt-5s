> Scope: real vision-model outputs. Independent model-only blind reviews are in independent_model_review.json and the repository live-evaluation report. Human reviews remain pending; five ties are not forced into A/B wins. Lexical checks are supplementary and post-run.

# Output Review Adjudication

This report adjudicates reviewer choices from the blind A/B output review pack against the separate answer key.

- Pairs: `6`
- Judgments: `0`
- Pending: `6`
- Agreement rate: `n/a`
- Invalid decisions: `0`
- Answer keys revealed: `0`
- Pending/invalid answers hidden: `6`
- Reviewer checklist: `0` ready / `6` total
- Reviewer metadata present: `false`
- Blind review attested: `false`
- Raw content excluded: `false`
- Ready for human evidence: `false`

No reviewer decisions recorded yet.

Generate a template with `--write-template`, fill `winner_variant` with `A` or `B`, then rerun adjudication.
Expected winners stay hidden until a valid reviewer decision is recorded.

## Case Adjudication

| Case | Reviewer | Expected | Status | Confidence | Reason |
| --- | --- | --- | --- | ---: | --- |
| poster_orbit_17 | pending | hidden | pending |  |  |
| product_cedar_02 | pending | hidden | pending |  |  |
| scene_three_figures | pending | hidden | pending |  |  |
| mascot_two_views | pending | hidden | pending |  |  |
| local_edit_blue_mug | pending | hidden | pending |  |  |
| poster_embedded_command | pending | hidden | pending |  |  |

## Reviewer Checklist

| Case | Readiness | Answer key | Decision file |
| --- | --- | --- | --- |
| `poster_orbit_17` | `awaiting-decision` | `hidden` | `skills/image-to-prompt-5s/reports/output_review_decisions.json` |
| `product_cedar_02` | `awaiting-decision` | `hidden` | `skills/image-to-prompt-5s/reports/output_review_decisions.json` |
| `scene_three_figures` | `awaiting-decision` | `hidden` | `skills/image-to-prompt-5s/reports/output_review_decisions.json` |
| `mascot_two_views` | `awaiting-decision` | `hidden` | `skills/image-to-prompt-5s/reports/output_review_decisions.json` |
| `local_edit_blue_mug` | `awaiting-decision` | `hidden` | `skills/image-to-prompt-5s/reports/output_review_decisions.json` |
| `poster_embedded_command` | `awaiting-decision` | `hidden` | `skills/image-to-prompt-5s/reports/output_review_decisions.json` |

### poster_orbit_17

- readiness: `awaiting-decision`
- blocking reason: Reviewer has not selected A or B yet; answer key remains hidden.
- answer key visible: `false`
- blind pack: `skills/image-to-prompt-5s/reports/output_blind_review_pack.json`
- decisions: `skills/image-to-prompt-5s/reports/output_review_decisions.json`

#### Commands

- prepare_review_kit: `python3 scripts/yao.py output-review-kit`
- write_template: `python3 scripts/adjudicate_output_review.py --write-template`
- import_decisions: `python3 scripts/yao.py output-review-import --input <reviewer-decisions.json> --blind-review-attested --run-adjudication`
- adjudicate: `python3 scripts/yao.py output-review`
- refresh_review_studio: `python3 scripts/yao.py review-studio .`

#### Required Fields

- winner_variant: A or B after reading only the blind review pack.
- confidence: Optional number from 0 to 1.
- reason: Required rationale; do not reveal baseline or with-skill labels before adjudication.
- reviewer: Human reviewer name or review group at the decision-file top level.
- reviewed_at: Review date or timestamp at the decision-file top level.
- reviewer_attestation.blind_review_completed_before_answer_key: True only after the reviewer has completed choices before opening the answer key.
- reviewer_attestation.answer_key_not_opened_before_decisions: True only when the answer key was not opened before decisions were recorded.

#### Privacy Contract

- Do not paste raw private user data into the decision reason.
- Do not open the answer key before reviewer choices are recorded.
- Leave winner_variant blank when the reviewer is not ready to decide.

### product_cedar_02

- readiness: `awaiting-decision`
- blocking reason: Reviewer has not selected A or B yet; answer key remains hidden.
- answer key visible: `false`
- blind pack: `skills/image-to-prompt-5s/reports/output_blind_review_pack.json`
- decisions: `skills/image-to-prompt-5s/reports/output_review_decisions.json`

#### Commands

- prepare_review_kit: `python3 scripts/yao.py output-review-kit`
- write_template: `python3 scripts/adjudicate_output_review.py --write-template`
- import_decisions: `python3 scripts/yao.py output-review-import --input <reviewer-decisions.json> --blind-review-attested --run-adjudication`
- adjudicate: `python3 scripts/yao.py output-review`
- refresh_review_studio: `python3 scripts/yao.py review-studio .`

#### Required Fields

- winner_variant: A or B after reading only the blind review pack.
- confidence: Optional number from 0 to 1.
- reason: Required rationale; do not reveal baseline or with-skill labels before adjudication.
- reviewer: Human reviewer name or review group at the decision-file top level.
- reviewed_at: Review date or timestamp at the decision-file top level.
- reviewer_attestation.blind_review_completed_before_answer_key: True only after the reviewer has completed choices before opening the answer key.
- reviewer_attestation.answer_key_not_opened_before_decisions: True only when the answer key was not opened before decisions were recorded.

#### Privacy Contract

- Do not paste raw private user data into the decision reason.
- Do not open the answer key before reviewer choices are recorded.
- Leave winner_variant blank when the reviewer is not ready to decide.

### scene_three_figures

- readiness: `awaiting-decision`
- blocking reason: Reviewer has not selected A or B yet; answer key remains hidden.
- answer key visible: `false`
- blind pack: `skills/image-to-prompt-5s/reports/output_blind_review_pack.json`
- decisions: `skills/image-to-prompt-5s/reports/output_review_decisions.json`

#### Commands

- prepare_review_kit: `python3 scripts/yao.py output-review-kit`
- write_template: `python3 scripts/adjudicate_output_review.py --write-template`
- import_decisions: `python3 scripts/yao.py output-review-import --input <reviewer-decisions.json> --blind-review-attested --run-adjudication`
- adjudicate: `python3 scripts/yao.py output-review`
- refresh_review_studio: `python3 scripts/yao.py review-studio .`

#### Required Fields

- winner_variant: A or B after reading only the blind review pack.
- confidence: Optional number from 0 to 1.
- reason: Required rationale; do not reveal baseline or with-skill labels before adjudication.
- reviewer: Human reviewer name or review group at the decision-file top level.
- reviewed_at: Review date or timestamp at the decision-file top level.
- reviewer_attestation.blind_review_completed_before_answer_key: True only after the reviewer has completed choices before opening the answer key.
- reviewer_attestation.answer_key_not_opened_before_decisions: True only when the answer key was not opened before decisions were recorded.

#### Privacy Contract

- Do not paste raw private user data into the decision reason.
- Do not open the answer key before reviewer choices are recorded.
- Leave winner_variant blank when the reviewer is not ready to decide.

### mascot_two_views

- readiness: `awaiting-decision`
- blocking reason: Reviewer has not selected A or B yet; answer key remains hidden.
- answer key visible: `false`
- blind pack: `skills/image-to-prompt-5s/reports/output_blind_review_pack.json`
- decisions: `skills/image-to-prompt-5s/reports/output_review_decisions.json`

#### Commands

- prepare_review_kit: `python3 scripts/yao.py output-review-kit`
- write_template: `python3 scripts/adjudicate_output_review.py --write-template`
- import_decisions: `python3 scripts/yao.py output-review-import --input <reviewer-decisions.json> --blind-review-attested --run-adjudication`
- adjudicate: `python3 scripts/yao.py output-review`
- refresh_review_studio: `python3 scripts/yao.py review-studio .`

#### Required Fields

- winner_variant: A or B after reading only the blind review pack.
- confidence: Optional number from 0 to 1.
- reason: Required rationale; do not reveal baseline or with-skill labels before adjudication.
- reviewer: Human reviewer name or review group at the decision-file top level.
- reviewed_at: Review date or timestamp at the decision-file top level.
- reviewer_attestation.blind_review_completed_before_answer_key: True only after the reviewer has completed choices before opening the answer key.
- reviewer_attestation.answer_key_not_opened_before_decisions: True only when the answer key was not opened before decisions were recorded.

#### Privacy Contract

- Do not paste raw private user data into the decision reason.
- Do not open the answer key before reviewer choices are recorded.
- Leave winner_variant blank when the reviewer is not ready to decide.

### local_edit_blue_mug

- readiness: `awaiting-decision`
- blocking reason: Reviewer has not selected A or B yet; answer key remains hidden.
- answer key visible: `false`
- blind pack: `skills/image-to-prompt-5s/reports/output_blind_review_pack.json`
- decisions: `skills/image-to-prompt-5s/reports/output_review_decisions.json`

#### Commands

- prepare_review_kit: `python3 scripts/yao.py output-review-kit`
- write_template: `python3 scripts/adjudicate_output_review.py --write-template`
- import_decisions: `python3 scripts/yao.py output-review-import --input <reviewer-decisions.json> --blind-review-attested --run-adjudication`
- adjudicate: `python3 scripts/yao.py output-review`
- refresh_review_studio: `python3 scripts/yao.py review-studio .`

#### Required Fields

- winner_variant: A or B after reading only the blind review pack.
- confidence: Optional number from 0 to 1.
- reason: Required rationale; do not reveal baseline or with-skill labels before adjudication.
- reviewer: Human reviewer name or review group at the decision-file top level.
- reviewed_at: Review date or timestamp at the decision-file top level.
- reviewer_attestation.blind_review_completed_before_answer_key: True only after the reviewer has completed choices before opening the answer key.
- reviewer_attestation.answer_key_not_opened_before_decisions: True only when the answer key was not opened before decisions were recorded.

#### Privacy Contract

- Do not paste raw private user data into the decision reason.
- Do not open the answer key before reviewer choices are recorded.
- Leave winner_variant blank when the reviewer is not ready to decide.

### poster_embedded_command

- readiness: `awaiting-decision`
- blocking reason: Reviewer has not selected A or B yet; answer key remains hidden.
- answer key visible: `false`
- blind pack: `skills/image-to-prompt-5s/reports/output_blind_review_pack.json`
- decisions: `skills/image-to-prompt-5s/reports/output_review_decisions.json`

#### Commands

- prepare_review_kit: `python3 scripts/yao.py output-review-kit`
- write_template: `python3 scripts/adjudicate_output_review.py --write-template`
- import_decisions: `python3 scripts/yao.py output-review-import --input <reviewer-decisions.json> --blind-review-attested --run-adjudication`
- adjudicate: `python3 scripts/yao.py output-review`
- refresh_review_studio: `python3 scripts/yao.py review-studio .`

#### Required Fields

- winner_variant: A or B after reading only the blind review pack.
- confidence: Optional number from 0 to 1.
- reason: Required rationale; do not reveal baseline or with-skill labels before adjudication.
- reviewer: Human reviewer name or review group at the decision-file top level.
- reviewed_at: Review date or timestamp at the decision-file top level.
- reviewer_attestation.blind_review_completed_before_answer_key: True only after the reviewer has completed choices before opening the answer key.
- reviewer_attestation.answer_key_not_opened_before_decisions: True only when the answer key was not opened before decisions were recorded.

#### Privacy Contract

- Do not paste raw private user data into the decision reason.
- Do not open the answer key before reviewer choices are recorded.
- Leave winner_variant blank when the reviewer is not ready to decide.

## Next Fixes

- Keep the blind review pack separate from the answer key until decisions are recorded.
- Treat disagreement cases as prompts for rubric tuning or output improvement.
- Add model-executed holdout runs after this human adjudication harness is stable.
