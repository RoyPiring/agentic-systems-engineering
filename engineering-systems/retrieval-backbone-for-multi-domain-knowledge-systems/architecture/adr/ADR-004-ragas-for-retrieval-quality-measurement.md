# ADR-004: Ragas for retrieval and answer quality measurement

## Status

Accepted

## Context

Without **repeatable metrics**, retrieval tuning becomes subjective. **P04** must show that answers and retrieval behavior can be **scored** against a defined evaluation set so regressions are visible when corpora, models, or parameters change.

## Decision

Adopt **Ragas** (and documented companion metrics where the guide requires) as the default framework for measuring retrieval/answer quality over a **fixed** question-and-ground-truth set stored or referenced from `build/` / `case-study/data/` as the series matures.

## Alternatives considered

- **Human-only grading** — Captures nuance but is not reproducible for CI-style portfolio proof.
- **Single custom metric (e.g. cosine-only)** — Cheap but does not match end-user perception of “good answers.”
- **Cloud-only eval APIs** — Rejected as the **default** path under the series cost posture; optional cloud judges could be documented as out-of-band only.

## Consequences

**Positive:** Named metrics, comparable runs, clearer validation narrative for reviewers.

**Negative / tradeoffs:** Metric quality depends on eval set size and judge model choice; small sets can mislead—document limitations in validation.

**Follow-ups:** Pin Ragas and dataset paths in P04 validation; align the **case study** verification table with the same acceptance criteria where applicable.
