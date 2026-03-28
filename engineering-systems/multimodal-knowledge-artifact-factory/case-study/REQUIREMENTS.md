# Requirements — Multimodal factory case study

Acceptance criteria for [RUNBOOK.md](./RUNBOOK.md). When every **required** row passes, the shipped **P01–P04** design holds for this scenario.

| ID | Requirement | Required |
| -- | ----------- | -------- |
| **R1** | **P01** prints structured lines (`H{n}:`, `P:`) for `case-study/data/script.md` with exit code **0**. | Yes |
| **R2** | **P02** creates at least one `p02-chunk-*.wav` under `executions/evidence/p02/audio/` from that P01 output (stub backend is fine). | Yes |
| **R3** | **P04 export** writes `flashcards.json` and `quiz.md` under `executions/evidence/p04/exports/` when given `script.md` as input; **JSON array non-empty** requires at least one `#` / `##` heading before body text (this crate drops orphan paragraphs). | Yes |
| **R4** | **`python integration.py --dry-run`** exits **0** after the above (prints path map; AIRI may be absent). | Yes |
| **R5** | **P03** (optional): desktop **Knowledge Viewer** opens after building with `--features viewer`, passing **`../case-study/data/script.md`** so UI sections match **§1** stub WAVs. | No |
| **R6** | **Artifacts** (optional): `case-study/artifacts/` copies of **`flashcards.json`** / **`quiz.md`** match `executions/evidence/p04/exports/` after a fresh **§2** (see [artifacts/README.md](./artifacts/README.md)). | No |

## Out of scope for required rows

- Neural / VibeVoice audio quality (stub WAVs satisfy **R2**).
- **AIRI** desktop launch (**R4** uses **`--dry-run`** only).
- CI automation (local operator run is enough).
