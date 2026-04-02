> ← [Multimodal Knowledge Artifact Factory](../README.md) · [All Systems](../../README.md) · [Home](../../../README.md)

# Executions

| Item | Role |
| ---- | ---- |
| [execution-record.md](./execution-record.md) | Short summary of what ran for each project (vs the plan) |
| [implementation/](./implementation/) | Per-project **plans** (`P0X-implementation-plan.md`) |
| [evidence/](./evidence/) | Run artifacts only (logs, transcripts, toolchain capture). Layout: **`p01/`** … **`p04/`** per project; optional **`p02/audio/`** (WAV), **`p04/exports/`** (JSON/quiz). |

| Project | Plan | Record | Validation |
| ------- | ---- | ------ | ---------- |
| P01 | [implementation/P01-implementation-plan.md](./implementation/P01-implementation-plan.md) | [execution-record.md](./execution-record.md) | [../validation/P01-validation.md](../validation/P01-validation.md) |

Keep plans concise; keep the execution record as a **summary**, not a copy of the plan.

## Canonical Evidence Paths

- Canonical WAV directory: **`executions/evidence/p02/audio/`**
- Canonical export directory: **`executions/evidence/p04/exports/`**

Some preserved transcripts still print earlier flattened names such as **`p02-audio`** or **`p04-exports`**. Treat those as historical runtime output, not as the current repository layout.
