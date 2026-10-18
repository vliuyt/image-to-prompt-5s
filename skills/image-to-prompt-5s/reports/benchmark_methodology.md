# Live evaluation methodology

Six independent-design image tasks, seven original Pillow fixtures, twelve formal paired Codex CLI vision calls. Baseline and treatment share model gpt-6.1-sol, task, images and host configuration; treatment alone receives one frozen skill snapshot. Local skill discovery disabled on both arms (454 discovered paths), fixed packaged host skills remain. No candidate tools were used. Raw host context/authentication is not published.

A 13-attempt pilot (including one capacity retry) was excluded in its entirety after one request revealed ambient skill-context budget truncation. This was a protocol deviation identified before candidate-answer inspection, not quality-based result selection. No successful formal answer was rerun. All attempts remain in evals/live/attempt-inventory.json; unknown usage is not zero.

The six-case visual rubric was authored independently before outputs and before reading the tested skill. Two fresh-context model agents each saw the same randomized A/B pack, reference images, user requests and rubric; neither received source identity. Decisions were hashed and locked before the identity key was opened. Both gave treatment 59/60, baseline 58/60: 1 win, 5 ties, 0 losses. These are two correlated model judgments on the same six cases, not twelve independent case replications or human votes. Formatting/style can reveal treatment assignment; output differences and stochastic generation cannot be fully controlled.

One preselected product case was then generated once per prompt using built-in image_gen with no attached reference. Two new blinded model agents assessed the images against the reference. No seed or exact backend model ID is exposed, so this does not establish GPT Image 2.5 API performance. Full prompt, outputs, image hashes, reviewer files and assignment keys are in evals/live/results/run-02.

Yao lexical assertion checks are supplementary and written after execution; they are not preregistered efficacy evidence. The independently frozen visual rubric is the primary signal. The Yao human A/B template stays pending because it cannot represent our model-only tie-aware reviews without implying a human judgment. Independent AI decisions are recorded separately, not forged as human approvals.

missing evidence: human blind review, repeated samples, natural-photo holdouts, cross-model replication, exact image-generation backend ID and broad adoption telemetry. No generalized or statistical superiority claim is made. These limits do not erase the real model calls or the completed independent AI review.

owner: vliuyt. review cadence: per-release. input_files: seven original file-backed fixture PNGs. output contract: 0–6 visual analysis plus copyable prompt, prompt-only on request. rollback boundary: reinstall prior package; no host settings or user images changed.
