> ← [All Systems](../../engineering-systems/README.md) · [Home](../../README.md)

# Retrieval Backbone — Multi-Domain Knowledge

**Problem:** Ad hoc RAG pipelines across domains rarely share a **measured**, **citation-aware** backbone—quality erodes quietly as content and models change.

**Approach:** Four-phase **Python** path: **Unstructured + Qdrant** ingestion → **LlamaIndex + Ollama** citation-aware retrieval → **Firecrawl** web integration → **Ragas** evaluation and service-shaped packaging—**$0 recurring** API posture by default.

**Outcome:** **P01**–**P04** are **executed** and [validated](./validation.md) **PASS**; operators: [P01](./user-guides/P01-user-guide.md) · [P02](./user-guides/P02-user-guide.md) · [P03](./user-guides/P03-user-guide.md) · [P04](./user-guides/P04-user-guide.md).

---

## What This Proves

| Signal | What a reviewer learns | Evidence |
| --- | --- | --- |
| Problem framing | Why a reusable, measured retrieval backbone matters | [business-context.md](./business-context.md) |
| Architectural judgment | Ingest → retrieve → web augment → evaluate; ADRs | [architecture.md](./architecture.md), [architecture/adr/](./architecture/adr/) |
| Delivery discipline | Phased plans under `executions/implementation/` | [implementation.md](./implementation.md) |
| Validation rigor | Per-phase **PASS** with proof paths | [validation.md](./validation.md); **P01–P04** **PASS** ([P04](./validation/P04-validation.md)) |

---

## Best Evidence

| Proof | What it demonstrates |
| --- | --- |
| [P04 validation](./validation/P04-validation.md) | The full retrieval story is complete: ingest, citation-aware query, web augmentation, evaluation, and service packaging |
| [p04-ragas-batch.txt](./executions/evidence/p04/p04-ragas-batch.txt) | Retrieval quality was measured, not inferred |
| [p04-consumer-demo.txt](./executions/evidence/p04/p04-consumer-demo.txt) | The system is consumable through a service-shaped interface, not only internal scripts |
| [p03-query-web-citation.txt](./executions/evidence/p03/p03-query-web-citation.txt) | Web-backed provenance is visible in the query result itself |

## Evidence By Phase

### P01
Ingest run output, Qdrant collection confirmation, and negative-edge transcripts are committed under [executions/evidence/p01/](./executions/evidence/p01/). Validation details: [validation/P01-validation.md](./validation/P01-validation.md).

### P02

*Citation-aware query output (Answer + source nodes) is captured in* [`executions/evidence/p02/p02-query-run.txt`](./executions/evidence/p02/p02-query-run.txt) *— see* [P02 validation](./validation/P02-validation.md).

### P03

*Web-style provenance (**`source_url:`** in Citations) is captured in* [`executions/evidence/p03/p03-query-web-citation.txt`](./executions/evidence/p03/p03-query-web-citation.txt) *— see* [P03 validation](./validation/P03-validation.md) *and* [`evidence/p03/README.md`](./executions/evidence/p03/README.md)*.*

### P04

*Ragas aggregates (**context_precision**, **answer_relevancy**) and consumer API smoke are captured in* [`executions/evidence/p04/p04-ragas-batch.txt`](./executions/evidence/p04/p04-ragas-batch.txt) *and* [`p04-consumer-demo.txt`](./executions/evidence/p04/p04-consumer-demo.txt) *— see* [P04 validation](./validation/P04-validation.md) *and* [`evidence/p04/README.md`](./executions/evidence/p04/README.md)*.*

---

## Intended Audience

- **Recruiters and non-technical readers** — [business-context.md](./business-context.md)
- **Hiring managers** — [business-context.md](./business-context.md) → [architecture.md](./architecture.md)
- **Operators** — [user-guides/README.md](./user-guides/README.md) · [P01](./user-guides/P01-user-guide.md) · [P02](./user-guides/P02-user-guide.md) · [P03](./user-guides/P03-user-guide.md) · [P04](./user-guides/P04-user-guide.md) · [Series order](./user-guides/SERIES-user-guide.md)
- **Peer engineers** — [architecture.md](./architecture.md) → [validation.md](./validation.md) → [executions/evidence/](./executions/evidence/)

## How to read this

1. [business-context.md](./business-context.md)
2. [validation.md](./validation.md)
3. [architecture.md](./architecture.md) (plus [architecture/diagrams/](./architecture/diagrams/) and [architecture/adr/](./architecture/adr/))
4. [implementation.md](./implementation.md)
5. [executions/evidence/](./executions/evidence/) — proof files by phase
6. [build/](./build/) — code and configs as phases land
7. [case-study/](./case-study/) — end-to-end **Local knowledge spine** scenario (linear RUNBOOK + SCENARIO)

---

## System Summary

- **Problem:** Fragmented RAG stacks without shared indexing, citations, or quality measurement.
- **Scope:** P01–P04 as defined in [implementation.md](./implementation.md); **P01**–**P04** executed and **PASS**.
- **Outcome:** End-to-end retrieval backbone with evidence per phase.
- **Constraints:** Local-first defaults; **$0 recurring** API spend in the default path; no production cloud claims.

## Repository Artifacts

- `business-context.md`, `architecture.md`, `implementation.md`, `validation.md`
- `architecture/diagrams/` (`.mmd` sources), `architecture/adr/`
- `executions/` — plans, execution record, `evidence/p01/` … `p04/`
- `validation/P01-validation.md` … `P04-validation.md`
- `user-guides/` — [P01](./user-guides/P01-user-guide.md) · [P02](./user-guides/P02-user-guide.md) · [P03](./user-guides/P03-user-guide.md) · [P04](./user-guides/P04-user-guide.md) · [index](./user-guides/README.md) · [series](./user-guides/SERIES-user-guide.md)
- `case-study/` — **Local knowledge spine** end-to-end scenario ([README](./case-study/README.md), [SCENARIO](./case-study/SCENARIO.md), [RUNBOOK](./case-study/RUNBOOK.md)); **R1**–**R4** (**P01**–**P04** **PASS**); optional [tools](./case-study/tools/)
- `build/` — **`ingest.py`**, **`query_pipeline.py`**, **`ingest_web.py`**, **`retrieval_service.py`**, **`ragas_eval.py`**, **`consumer_demo.py`**, `requirements.txt`, `data/` samples

---

## Related systems

- [Multimodal Knowledge Artifact Factory](../multimodal-knowledge-artifact-factory/) — local multimodal study pipeline (separate problem domain; same portfolio standards)
