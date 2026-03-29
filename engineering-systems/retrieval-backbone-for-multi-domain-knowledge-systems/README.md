> ← [All Systems](../../engineering-systems/README.md) · [Home](../../README.md)

# Retrieval Backbone — Multi-Domain Knowledge

**Problem:** Ad hoc RAG pipelines across domains rarely share a **measured**, **citation-aware** backbone—quality erodes quietly as content and models change.

**Approach:** Four-phase **Python** path: **Unstructured + Qdrant** ingestion → **LlamaIndex + Ollama** citation-aware retrieval → **Firecrawl** web integration → **Ragas** evaluation and service-shaped packaging—**$0 recurring** API posture by default.

**Outcome:** (In progress.) **P01** and **P02** are **executed** and [validated](./validation/P01-validation.md) / [P02 validated](./validation/P02-validation.md) **PASS**; operators: [P01 user guide](./user-guides/P01-user-guide.md) · [P02 user guide](./user-guides/P02-user-guide.md).

---

## What This Proves

| Signal | What a reviewer learns | Evidence |
| --- | --- | --- |
| Problem framing | Why a reusable, measured retrieval backbone matters | [business-context.md](./business-context.md) |
| Architectural judgment | Ingest → retrieve → web augment → evaluate; ADRs | [architecture.md](./architecture.md), [architecture/adr/](./architecture/adr/) |
| Delivery discipline | Phased plans under `executions/implementation/` | [implementation.md](./implementation.md) |
| Validation rigor | Per-phase **PASS** / **Pending** with proof paths | [validation.md](./validation.md); **P01–P02** **PASS** ([P01](./validation/P01-validation.md), [P02](./validation/P02-validation.md)); P03–P04 pending |

---

## Visual (P01)

*No Qdrant dashboard screenshot committed yet. For proof of run, see [executions/evidence/p01/](./executions/evidence/p01/) and [validation/P01-validation.md](./validation/P01-validation.md).*

<!-- When captured, replace the paragraph above with:
![Qdrant collection multi_domain_docs — points after ingest](./executions/evidence/p01/p01-qdrant-dashboard.png)
-->

## Text proof (P02)

*Citation-aware query output (Answer + source nodes) is captured in* [`executions/evidence/p02/p02-query-run.txt`](./executions/evidence/p02/p02-query-run.txt) *— see* [P02 validation](./validation/P02-validation.md).

---

## Intended Audience

- **Recruiters and non-technical readers** — [business-context.md](./business-context.md)
- **Hiring managers** — [business-context.md](./business-context.md) → [architecture.md](./architecture.md)
- **Operators** — [user-guides/README.md](./user-guides/README.md) · [P01](./user-guides/P01-user-guide.md) · [P02](./user-guides/P02-user-guide.md) · [Series order](./user-guides/SERIES-user-guide.md)
- **Peer engineers** — [architecture.md](./architecture.md) → [validation.md](./validation.md) → [executions/evidence/](./executions/evidence/)

## How to read this

1. [business-context.md](./business-context.md)
2. [architecture.md](./architecture.md) (plus [architecture/diagrams/](./architecture/diagrams/) and [architecture/adr/](./architecture/adr/))
3. [implementation.md](./implementation.md)
4. [validation.md](./validation.md)
5. [build/](./build/) — code and configs as phases land

---

## System Summary

- **Problem:** Fragmented RAG stacks without shared indexing, citations, or quality measurement.
- **Scope:** P01–P04 as defined in [implementation.md](./implementation.md); **P01**–**P02** **PASS**; **P03–P04** planned.
- **Outcome:** End-to-end retrieval backbone with evidence per phase (target state).
- **Constraints:** Local-first defaults; **$0 recurring** API spend in the default path; no production cloud claims.

## Repository Artifacts

- `business-context.md`, `architecture.md`, `implementation.md`, `validation.md`
- `architecture/diagrams/` (`.mmd` sources), `architecture/adr/`
- `executions/` — plans, execution record, `evidence/p01/` … `p04/`
- `validation/P01-validation.md` … `P04-validation.md`
- `user-guides/` — [P01](./user-guides/P01-user-guide.md) · [P02](./user-guides/P02-user-guide.md) · [index](./user-guides/README.md) · [series](./user-guides/SERIES-user-guide.md); P03–P04 when validated
- `case-study/` — scenario scaffold (requirements, runbook, `data/`); **R1/R2** verification rows filled (**P01**–**P02** **PASS**); **R3/R4** when P03–P04 validate
- `build/` — **`ingest.py`**, **`query_pipeline.py`**, `requirements.txt`, `data/` samples (P01); further scripts as P03–P04 land

---

## Related systems

- [Multimodal Knowledge Artifact Factory](../multimodal-knowledge-artifact-factory/) — local multimodal study pipeline (separate problem domain; same portfolio standards)
