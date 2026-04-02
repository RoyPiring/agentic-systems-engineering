> ← [System README](../README.md) · [All Systems](../../README.md) · [Home](../../../README.md)

# Case study — Local knowledge spine (Retrieval Backbone)

**Scenario:** A small platform team needs one **local-first** pipeline from **mixed documents** + **one web slice** to **cited answers** and **measured quality**, without mandatory paid APIs. This pack proves the **full P01–P04 series** works **by design** for that story using existing **`build/`** scripts only.

This is **not** a second copy of every operator detail — for setup depth and troubleshooting, start at [`../user-guides/README.md`](../user-guides/README.md) and [`../user-guides/SERIES-user-guide.md`](../user-guides/SERIES-user-guide.md).

| Doc | Purpose |
| --- | -------- |
| [SCENARIO.md](./SCENARIO.md) | Narrative, R1–R4 mapping, constraints, non-goals |
| [REQUIREMENTS.md](./REQUIREMENTS.md) | Acceptance criteria **R1–R4** + representative queries |
| [RUNBOOK.md](./RUNBOOK.md) | **Linear** copy-paste end-to-end run (Qdrant → ingest → web slice → query → Ragas → consumer) |
| [data/README.md](./data/README.md) | Where corpus inputs live (`build/data/` + optional BYO) |
| [data/queries.md](./data/queries.md) | Canonical questions (match `ragas_eval.py` batch rows + manual checks) |
| [diagrams/e2e-flow.mmd](./diagrams/e2e-flow.mmd) | Mermaid source for P01–P04 flow |

**Tools (optional automation):**

| Path | Purpose |
| --- | -------- |
| [tools/run_case_study.ps1](./tools/run_case_study.ps1) | Windows: run the same steps as RUNBOOK from `build/` |
| [tools/run_case_study.sh](./tools/run_case_study.sh) | Unix: same |

**Evidence of record:** Per **PORTFOLIO-BUILD-SOP**, committed transcripts and validation live under [`../executions/evidence/p01/`](../executions/evidence/p01/) … [`../executions/evidence/p04/`](../executions/evidence/p04/). This case-study folder is narrative + procedure; it does not replace **`validation/P0X-validation.md`**.

**Optional reviewer copies:** [`artifacts/README.md`](./artifacts/README.md) — optional snapshots pointing at `executions/evidence` (same idea as Multimodal’s `case-study/artifacts/`).

**Last updated:** 2026-04-01 — named scenario, linear RUNBOOK, tools, diagram, CI dry-dataset smoke.
