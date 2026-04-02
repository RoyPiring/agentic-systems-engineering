# Implementation plan — P04: Quality Measurement and Service Packaging (Ragas)

| Field | Value |
| ----- | ----- |
| System | retrieval-backbone-for-multi-domain-knowledge-systems |
| Date | 2026-03-30 |
| Series guide (filename only) | P04-Quality_Measurement_and_Service_Packaging_Ragas.md |
| Depends on | P01–P03 |

## Outcome

When this phase is done:

- Ragas evaluates the LlamaIndex RAG path with **explicit Ollama** LLM and embeddings (no paid default routing); **baseline and batch** runs produce **context precision** and **answer relevancy**, with transcripts under `executions/evidence/p04/`.
- A single **packaged** Python surface in `build/` exposes a documented **query → answer + citations** API; paths and endpoints come from **environment or injected config**; clients and pipeline state stay **instance-scoped**.
- A **consumer script** uses only that public API; **validation** and **rollups** reflect the shipped contract (series project guide checkpoints satisfied).

## Roadmap

| Phase | Focus |
| ----- | ----- |
| 1 | Setup / toolchain / prerequisites |
| 2 | Core build from the guide |
| 3 | Integration / smoke / edge case |
| 4 | Docs, evidence, validation closeout |

---

## Phase 1 — Prerequisites

| Step | Complete when |
| ---- | ------------- |
| 1.1 | Toolchain matches series guide (Python 3.12, `ragas`, LlamaIndex stack, Qdrant client, `build/` deps) |
| 1.2 | Ollama (Llama 3.2, nomic-embed-text), Qdrant, and P03-related services (e.g. Firecrawl) are reachable as in prior projects; `build/`, `executions/evidence/p04/`, and `validation/P04-validation.md` paths are ready |
| 1.3 | Series guide read; risks logged (Ragas OpenAI defaults, Ragas dataset schema, local batch timeouts) |

## Phase 2 — Baseline Ragas

| Step | Complete when |
| ---- | ------------- |
| 2.1 | `build/` script runs the existing pipeline, emits **question**, **answer**, and **retrieved contexts** (citation/source nodes preserved); rows match Ragas **contexts-as-list-of-strings** shape |
| 2.2 | **One** Ragas metric completes with **injected** Ollama LLM and embeddings — no cloud API-key authentication failure from defaults |
| 2.3 | Observable artifact in `executions/evidence/p04/` (e.g. baseline stdout or `p04-ragas-baseline.txt`) |

## Phase 3 — Batch evaluation and service API

| Step | Complete when |
| ---- | ------------- |
| 3.1 | **Happy path:** batch queries span markdown, PDF, and web-derived content; **context precision** and **answer relevancy** aggregated; results recorded with proof in `executions/evidence/p04/` |
| 3.2 | **Expected vs actual:** documented scores (or pass/fail against a stated threshold) match what the guide requires for a quantitative baseline |
| 3.3 | **Smoke / edge:** separate script instantiates the backbone **only** via the new API; optional throttle/retry if a batch hits local Ollama limits once; refactor stays in `build/` — one cohesive class/module, no hardcoded absolute paths, no shared mutable globals across queries |

## Phase 4 — Closeout

| Step | Complete when |
| ---- | ------------- |
| 4.1 | `execution-record.md` updated (**summary** of what ran, not a dump of this table) |
| 4.2 | Run transcripts in `executions/evidence/p04/` with clear names (build logs, toolchain, etc.; see SOP Appendix N) |
| 4.3 | `validation/P04-validation.md` at **PASS** when the work is accepted |
| 4.4 | `implementation.md` and root `validation.md` rollups match this project |

---

## Done when

- [x] Phases 1–4 steps satisfied with proof in the execution record, `executions/evidence/p04/` (transcripts), and this plan updated as needed
- [x] Per-project validation **PASS**
- [x] System rollups updated

## Next

Series complete (4 of 4); portfolio sustainment — optional CI-triggered Ragas per series reflection.
