> ← [All Systems](../README.md) · [Home](../../README.md)

# Retrieval Backbone — Multi-Domain Knowledge

**Problem:** Ad hoc RAG pipelines across domains rarely share a **measured**, **citation-aware** backbone—quality erodes quietly as content and models change.

**Approach:** Four-phase **Python** path: **Unstructured + Qdrant** ingestion → **LlamaIndex + Ollama** citation-aware retrieval → **Firecrawl** web integration → **Ragas** evaluation and service-shaped packaging—**$0 recurring** API posture by default.

**Outcome:** (In progress.) Scaffold + requirements + architecture on this branch; **P01** execution and validation **Pending**.

---

## What This Proves

| Signal | What a reviewer learns | Evidence |
| --- | --- | --- |
| Problem framing | Why a reusable, measured retrieval backbone matters | [business-context.md](./business-context.md) |
| Architectural judgment | Ingest → retrieve → web augment → evaluate; ADRs | [architecture.md](./architecture.md), [architecture/adr/](./architecture/adr/) |
| Delivery discipline | Phased plans under `executions/implementation/` | [implementation.md](./implementation.md) |
| Validation rigor | Per-phase **PASS** / **Pending** with proof paths | [validation.md](./validation.md), [validation/P01-validation.md](./validation/P01-validation.md) … [validation/P04-validation.md](./validation/P04-validation.md) |

---

## Intended Audience

- **Recruiters and non-technical readers** — [business-context.md](./business-context.md)
- **Hiring managers** — [business-context.md](./business-context.md) → [architecture.md](./architecture.md)
- **Operators** — [user-guides/README.md](./user-guides/README.md) (runbooks grow as phases complete)
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
- **Scope:** P01–P04 as defined in [implementation.md](./implementation.md); **P01** is the next execution target.
- **Outcome:** End-to-end retrieval backbone with evidence per phase (target state).
- **Constraints:** Local-first defaults; **$0 recurring** API spend in the default path; no production cloud claims.

## Repository Artifacts

- `business-context.md`, `architecture.md`, `implementation.md`, `validation.md`
- `architecture/diagrams/` (`.mmd` sources), `architecture/adr/`
- `executions/` — plans, execution record, `evidence/p01/` … `p04/`
- `validation/P01-validation.md` … `P04-validation.md`
- `user-guides/` — operator runbooks (filled as phases complete); `SERIES-user-guide.md` is a placeholder until the series is runnable end-to-end
- `case-study/` — scenario scaffold (requirements, runbook, `data/`); flesh out when the **full series** is validated (**by-design** proof)
- `build/` — runnable code and configs (populated starting with **P01**)
