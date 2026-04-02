> ← [Retrieval Backbone — Multi-Domain Knowledge](./README.md) · [All Systems](../README.md) · [Home](../../README.md)

# Implementation

Phased delivery from a working **ingest + index** path through **citation-aware retrieval**, **web augmentation**, and **measured, packaged** retrieval services. Per-project plans live in [`executions/implementation/`](./executions/implementation/); evidence lives in [`executions/evidence/`](./executions/evidence/). **Operators:** start at [`user-guides/README.md`](./user-guides/README.md) and [`user-guides/SERIES-user-guide.md`](./user-guides/SERIES-user-guide.md); per phase: [P01](./user-guides/P01-user-guide.md) · [P02](./user-guides/P02-user-guide.md) · [P03](./user-guides/P03-user-guide.md) · [P04](./user-guides/P04-user-guide.md).

## Strategy

Work moves **P01 → P04** so each phase is testable alone: without a trustworthy index, retrieval metrics are meaningless; without retrieval, web and eval layers have nothing to attach to.

## Phases

### P01 — Document ingestion and vector indexing

| | |
| --- | --- |
| **Plan** | [executions/implementation/P01-implementation-plan.md](./executions/implementation/P01-implementation-plan.md) |
| **Goal** | Parse **Markdown/PDF** with **Unstructured**, embed with **Ollama** `nomic-embed-text`, index into **Qdrant** collection **`multi_domain_docs`** |
| **Inputs** | Samples under [`build/data/`](./build/data/) · script [`build/ingest.py`](./build/ingest.py) |
| **Output** | Running local Qdrant + repeatable ingest; evidence under [`executions/evidence/p01/`](./executions/evidence/p01/) |

**Status:** **Executed** — [validation/P01-validation.md](./validation/P01-validation.md) **PASS** (2026-03-28); evidence in [`executions/evidence/p01/`](./executions/evidence/p01/).

### P02 — Citation-aware retrieval (LlamaIndex + Ollama)

| | |
| --- | --- |
| **Plan** | [executions/implementation/P02-implementation-plan.md](./executions/implementation/P02-implementation-plan.md) |
| **Goal** | LlamaIndex query pipeline over Qdrant with **Ollama** models; answers cite retrieved nodes |
| **Inputs** | P01 index in **`multi_domain_docs`** · script [`build/query_pipeline.py`](./build/query_pipeline.py) |
| **Output** | Answer + **Citations** (source nodes); evidence under [`executions/evidence/p02/`](./executions/evidence/p02/) |
| **Depends on** | P01 **PASS** |

**Status:** **Executed** — [validation/P02-validation.md](./validation/P02-validation.md) **PASS** (2026-03-29); evidence in [`executions/evidence/p02/`](./executions/evidence/p02/); [P02 user guide](./user-guides/P02-user-guide.md).

### P03 — Live web content (Firecrawl)

| | |
| --- | --- |
| **Plan** | [executions/implementation/P03-implementation-plan.md](./executions/implementation/P03-implementation-plan.md) |
| **Goal** | Fold crawled pages into the same ingest/index contract as file corpora |
| **Inputs** | Self-hosted **Firecrawl** · script [`build/ingest_web.py`](./build/ingest_web.py) · existing **`multi_domain_docs`** |
| **Output** | Appended vectors with **`source_url`** metadata; evidence under [`executions/evidence/p03/`](./executions/evidence/p03/) |
| **Depends on** | P02 **PASS** |

**Status:** **Executed** — [validation/P03-validation.md](./validation/P03-validation.md) **PASS** (2026-03-29); evidence in [`executions/evidence/p03/`](./executions/evidence/p03/) (see [`evidence/p03/README.md`](./executions/evidence/p03/README.md)); [P03 user guide](./user-guides/P03-user-guide.md). Optional: **`p03-ingest-web-run.txt`** when live Firecrawl is used.

### P04 — Quality measurement and packaging (Ragas)

| | |
| --- | --- |
| **Plan** | [executions/implementation/P04-implementation-plan.md](./executions/implementation/P04-implementation-plan.md) |
| **Goal** | Ragas **context_precision** + **answer_relevancy** over pipeline rows; **`RetrievalBackboneService`** public API + **`consumer_demo.py`** |
| **Inputs** | Qdrant **`multi_domain_docs`** · scripts [`build/ragas_eval.py`](./build/ragas_eval.py), [`build/retrieval_service.py`](./build/retrieval_service.py), [`build/consumer_demo.py`](./build/consumer_demo.py) |
| **Output** | Evidence under [`executions/evidence/p04/`](./executions/evidence/p04/) |
| **Depends on** | P03 **PASS** |

**Status:** **Executed** — [validation/P04-validation.md](./validation/P04-validation.md) **PASS** (2026-03-31); [P04 user guide](./user-guides/P04-user-guide.md). **Case study (E2E narrative):** [case-study/README.md](./case-study/README.md) · [RUNBOOK](./case-study/RUNBOOK.md).

## Execution path (target)

1. Bring up **Qdrant** and **Ollama** (documented per phase).
2. Run **P01** ingest against sample data; capture evidence.
3. Run **P02** queries via **`build/query_pipeline.py`**; capture **Answer** / **Citations** under **`executions/evidence/p02/`** (see [P02 user guide](./user-guides/P02-user-guide.md)).
4. Run **P03** crawl-to-index path; validate parity with file ingest.
5. Run **P04** eval + packaging (**`ragas_eval.py`**, **`consumer_demo.py`**); record Ragas outputs under **`executions/evidence/p04/`** (see [P04 user guide](./user-guides/P04-user-guide.md)).
6. **Case study (optional):** walk the **Local knowledge spine** line-by-line in [case-study/RUNBOOK.md](./case-study/RUNBOOK.md) to tie **P01**–**P04** into one reviewer-facing path.

## Decision points

| Decision Point | Why It Matters | Chosen Path |
| --- | --- | --- |
| Local vs hosted vectors | Cost and reproducibility | Local Qdrant — [ADR-001](./architecture/adr/ADR-001-local-ollama-qdrant-zero-recurring-cost.md) |
| Orchestration framework | Consistency across phases | LlamaIndex — [ADR-002](./architecture/adr/ADR-002-llamaindex-orchestration-layer.md) |

## Reproducibility notes

- **Python 3.12** (plan target) and pinned dependencies under `build/`; P01/P02 validation used **3.13.11** (`p01-python-version.txt`, `p02-python-version.txt`).
- **`build/requirements.txt`:** **`llama-index-vector-stores-qdrant>=0.10.0`** is required with **qdrant-client 1.17+**; see comments in that file and **`p02-pip-freeze.txt`** for the resolved stack.
- **Docker** for Qdrant unless using a documented native install.
- **Ollama** models: **`nomic-embed-text`** (P01+P02 embed) and **`llama3.2`** (P02 LLM default) — see `p02-ollama-list.txt`.
