> ← [All Systems](../../engineering-systems/README.md) · [Home](../../README.md)

# Retrieval Backbone — Multi-Domain Knowledge

**Problem:** Ad hoc RAG pipelines across domains rarely share a **measured**, **citation-aware** backbone—quality erodes quietly as content and models change.

**Approach:** Four-phase **Python** path: **Unstructured + Qdrant** ingestion → **LlamaIndex + Ollama** citation-aware retrieval → **Firecrawl** web integration → **Ragas** evaluation and service-shaped packaging—**$0 recurring** API posture by default.

**Outcome:** **P01**–**P03** are **executed** and [validated](./validation.md) **PASS**; operators: [P01](./user-guides/P01-user-guide.md) · [P02](./user-guides/P02-user-guide.md) · [P03](./user-guides/P03-user-guide.md).

---

## What This Proves

| Signal | What a reviewer learns | Evidence |
| --- | --- | --- |
| Problem framing | Why a reusable, measured retrieval backbone matters | [business-context.md](./business-context.md) |
| Architectural judgment | Ingest → retrieve → web augment → evaluate; ADRs | [architecture.md](./architecture.md), [architecture/adr/](./architecture/adr/) |
| Delivery discipline | Phased plans under `executions/implementation/` | [implementation.md](./implementation.md) |
| Validation rigor | Per-phase **PASS** / **Pending** with proof paths | [validation.md](./validation.md); **P01–P03** **PASS** ([P03](./validation/P03-validation.md)); **P04** pending |

---

## Visual (P01)

*No Qdrant dashboard screenshot committed yet. For proof of run, see [executions/evidence/p01/](./executions/evidence/p01/) and [validation/P01-validation.md](./validation/P01-validation.md).*

<!-- When captured, replace the paragraph above with:
![Qdrant collection multi_domain_docs — points after ingest](./executions/evidence/p01/p01-qdrant-dashboard.png)
-->

## Text proof (P02)

*Citation-aware query output (Answer + source nodes) is captured in* [`executions/evidence/p02/p02-query-run.txt`](./executions/evidence/p02/p02-query-run.txt) *— see* [P02 validation](./validation/P02-validation.md).

## Text proof (P03)

*Web-style provenance (**`source_url:`** in Citations) is captured in* [`executions/evidence/p03/p03-query-web-citation.txt`](./executions/evidence/p03/p03-query-web-citation.txt) *— see* [P03 validation](./validation/P03-validation.md) *and* [`evidence/p03/README.md`](./executions/evidence/p03/README.md)*.*

---

## Intended Audience

- **Recruiters and non-technical readers** — [business-context.md](./business-context.md)
- **Hiring managers** — [business-context.md](./business-context.md) → [architecture.md](./architecture.md)
- **Operators** — [user-guides/README.md](./user-guides/README.md) · [P01](./user-guides/P01-user-guide.md) · [P02](./user-guides/P02-user-guide.md) · [P03](./user-guides/P03-user-guide.md) · [Series order](./user-guides/SERIES-user-guide.md)
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
- **Scope:** P01–P04 as defined in [implementation.md](./implementation.md); **P01**–**P03** executed and **PASS**; **P04** planned.
- **Outcome:** End-to-end retrieval backbone with evidence per phase (target state).
- **Constraints:** Local-first defaults; **$0 recurring** API spend in the default path; no production cloud claims.

## Repository Artifacts

- `business-context.md`, `architecture.md`, `implementation.md`, `validation.md`
- `architecture/diagrams/` (`.mmd` sources), `architecture/adr/`
- `executions/` — plans, execution record, `evidence/p01/` … `p04/`
- `validation/P01-validation.md` … `P04-validation.md`
- `user-guides/` — [P01](./user-guides/P01-user-guide.md) · [P02](./user-guides/P02-user-guide.md) · [P03](./user-guides/P03-user-guide.md) · [index](./user-guides/README.md) · [series](./user-guides/SERIES-user-guide.md); P04 when validated
- `case-study/` — scenario scaffold (requirements, runbook, `data/`); **R1**–**R3** filled (**P01**–**P03** **PASS**); **R4** when P04 validates
- `build/` — **`ingest.py`**, **`query_pipeline.py`**, **`ingest_web.py`**, `requirements.txt`, `data/` samples (P01); P04 scripts when landed

---

## Related systems

- [Multimodal Knowledge Artifact Factory](../multimodal-knowledge-artifact-factory/) — local multimodal study pipeline (separate problem domain; same portfolio standards)
