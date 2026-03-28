# Case study — Multimodal Knowledge Artifact Factory

**Scenario:** Run the **full shipped series** (P01 → P02 → P04, optional P03) using committed data under [`data/`](./data/), and confirm the system behaves **by design** for this path.

This is **not** a second copy of the generic tutorial — start with [`../user-guides/SERIES-user-guide.md`](../user-guides/SERIES-user-guide.md) if you only need command order and setup.

| Doc | Purpose |
| --- | -------- |
| [REQUIREMENTS.md](./REQUIREMENTS.md) | Acceptance criteria (**R1–R6**) |
| [RUNBOOK.md](./RUNBOOK.md) | Step-by-step commands from **`build/`** ( **`script.md`**, exports, integration, viewer with optional markdown path, artifact sync) |
| [`data/script.md`](./data/script.md) | Input markdown for P01 / P02 / P04 in the runbook |
| [`data/audio/`](./data/audio/README.md) | Optional **spoken** MP3 of `script.md` (Edge TTS; not used by P03 **Play Narration**, which uses **`executions/evidence/p02/audio/`** stub WAVs) |
| [`artifacts/`](./artifacts/README.md) | Optional **copies** of P04 **`flashcards.json`** / **`quiz.md`** for reviewers (source of truth remains **`executions/evidence/p04/exports/`**) |
| [`tools/generate_edge_narration.py`](./tools/generate_edge_narration.py) | Regenerate narration: `--one-file`, `--merge`, `--merge-only` |

**Standard:** One concrete scenario with **requirements**, **data**, **runbook**, and **verification** — portfolio **case-study** pack for end-to-end checks before release.

**Evidence layout:** Run transcripts and exports follow **`executions/evidence/p01/`** … **`p04/`**: stub WAVs under **`p02/audio/`**, study exports under **`p04/exports/`**.

**Last updated:** 2026-03-27 — runbook, requirements, **`artifacts/`**, viewer **`script.md`** path.
