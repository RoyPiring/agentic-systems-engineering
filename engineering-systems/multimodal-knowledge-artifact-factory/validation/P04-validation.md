# P04 validation — Multimodal study artifact assembly (AIRI)

| | |
|--|--|
| **Plan** | [../executions/implementation/P04-implementation-plan.md](../executions/implementation/P04-implementation-plan.md) |
| **Result** | **Pending** — execute after P04 build; see checks below |

## Checks

| # | Criterion | Pass when |
|---|-----------|-----------|
| 1 | Export binary | `cargo run --bin export` (from `build/`, documented args) produces valid **`flashcards.json`** and **`quiz.md`** under the path named in the plan |
| 2 | JSON quality | `flashcards.json` parses as a JSON array; objects include stable **term** / **definition** (or equivalent) fields; no manual unescaped breakage |
| 3 | Quiz markdown | `quiz.md` is readable markdown with questions and answers separated as documented |
| 4 | Integration script | `integration.py` runs without path resolution errors when cwd matches **`build/README.md`**; uses relative resolution from engineering-system root (no brittle absolute paths) |
| 5 | AIRI handoff | Documented command to launch AIRI with asset paths; **or** explicit **conditional** note if AIRI is not installed in a given environment |
| 6 | Pipeline order | Execution record lists an ordered end-to-end sequence (parse → audio → export → integration) with evidence pointers |
| 7 | Evidence | Transcripts under `executions/evidence/` (`p04-*`); optional AIRI screenshot when available |

## How to run

Follow commands recorded in [`../executions/execution-record.md`](../executions/execution-record.md) after P04 execution.

## Results

| Check | Expected | Actual |
| ----- | -------- | ------ |
| 1 | Export binary runs | *Pending* |
| 2 | Valid flashcards JSON | *Pending* |
| 3 | Quiz markdown | *Pending* |
| 4 | `integration.py` smoke | *Pending* |
| 5 | AIRI / documented skip | *Pending* |
| 6 | E2E narrative | *Pending* |
| 7 | Evidence files | *Pending* |
