# Execution record

Single log for **P01 through P04**. For each project add `## P0X` sections: **summary** of what ran (phase table, key commands, evidence links)—not a full duplicate of `implementation/P0X-implementation-plan.md`.

## Series intent

**Retrieval Backbone — Multi-Domain Knowledge:** citation-aware RAG backbone across markdown, PDF, and web-derived content with local inference, Qdrant indexing, and measured quality (series overview: *Retrieval Backbone — Multi-Domain Knowledge*).

## P01 — Document ingestion and vector indexing

**Status:** **Executed** (2026-03-28) on branch `feature/retrieval-backbone-for-multi-domain-knowledge-systems`.

### What ran — P01

| Step | Command / artifact |
| --- | --- |
| Qdrant | `docker run -d --name qdrant-p01 -p 6333:6333 -p 6334:6334 qdrant/qdrant:latest` (operator-local; not committed) |
| Ollama | `ollama pull nomic-embed-text` |
| Python | **3.13.11** venv under `build/venv` (plan target 3.12; see `p01-python-version.txt`) |
| Ingest | Windows long-path mitigation: `build/run_ingest_windows.ps1` → `ingest.py`; collection **`multi_domain_docs`**; sample `build/data/sample.md` → **2** document nodes, exit **0** |
| Deps | `pip install -r build/requirements.txt`; `charset-normalizer` rebuilt from sdist (`--no-binary charset-normalizer`) to avoid DLL **MAX_PATH** on this host |

**Evidence:** `executions/evidence/p01/` — `p01-curl-qdrant.txt`, `p01-qdrant-collection.txt`, `p01-ollama-list.txt`, `p01-ingest-run.txt`, `p01-pip-freeze.txt`, `p01-python-version.txt`, `p01-negative-edge.txt`. Validation: **`validation/P01-validation.md`** **PASS**.

## P02 — Citation-aware retrieval pipeline

**Status:** **Executed** (2026-03-29) on branch `feature/retrieval-backbone-for-multi-domain-knowledge-systems-p02`.

### What ran — P02

| Step | Command / artifact |
| --- | --- |
| Code | `build/query_pipeline.py` — `Settings` → **Ollama** LLM (`llama3.2`) + **Ollama** embed (`nomic-embed-text`); `VectorStoreIndex.from_vector_store` + `as_query_engine(similarity_top_k=3, text_qa_template=…)`; stdout **Answer** / **Citations** |
| Deps | `pip install -r build/requirements.txt` (vector store **≥0.10** for qdrant-client **1.17+**); see `p02-pip-freeze.txt` |
| Models | `ollama pull llama3.2` (in addition to P01 `nomic-embed-text`) |

**Evidence:** `executions/evidence/p02/` — `p02-query-run.txt`, `p02-ollama-list.txt`, `p02-curl-qdrant.txt`, `p02-qdrant-collection.txt`, `p02-pip-freeze.txt`, `p02-python-version.txt`. Operator runbook: **`user-guides/P02-user-guide.md`**. Validation: **`validation/P02-validation.md`** **PASS**.

## P03 — Live web content (Firecrawl)

**Status:** **Executed** (2026-03-29) — plan: [`executions/implementation/P03-implementation-plan.md`](./implementation/P03-implementation-plan.md). **`build/ingest_web.py`** (Firecrawl v1 scrape/crawl → **`source_url`** → Qdrant append; **`--synthetic-evidence`** when Firecrawl unavailable) and **`build/query_pipeline.py`** **`source_url`** citations. Operator runbook: [`user-guides/P03-user-guide.md`](../user-guides/P03-user-guide.md).

### What ran — P03

| Step | Command / artifact |
| --- | --- |
| Qdrant | Operator-local container on **6333** (e.g. `qdrant-p03-evidence`); see `p03-qdrant-collections.json`, `p03-qdrant-after-web.txt` |
| Ingest | `python ingest_web.py --synthetic-evidence` (no Firecrawl); optional `--dry-run` — `p03-ingest-web-synthetic.txt`, `p03-ingest-web-dry-run.txt` |
| Query | `python query_pipeline.py --query "…PEP 405…PYPREFIX…"` — `p03-query-web-citation.txt` (**`source_url:`** in Citations) |
| Firecrawl | Not running on host — `p03-firecrawl-health.txt` (see [validation.md](../validation.md) **Limitations**) |

**Evidence:** `executions/evidence/p03/` — **`README.md`**, transcripts above, **`p03-pip-freeze.txt`**. Validation: **`validation/P03-validation.md`** **PASS**.

## P04 — Quality measurement and service packaging (Ragas)

**Status:** **Executed** (2026-03-31) on branch `feature/retrieval-backbone-p04-ragas-quality-service` (PR to `main`). Plan: [`executions/implementation/P04-implementation-plan.md`](./implementation/P04-implementation-plan.md). **`build/retrieval_service.py`** (packaged API), **`build/ragas_eval.py`**, **`build/consumer_demo.py`**; **`query_pipeline.py`** delegates to the service.

### What ran — P04

| Step | Command / artifact |
| --- | --- |
| Qdrant | Reused existing Docker container **`qdrant-p01`** (`docker start qdrant-p01`); **`multi_domain_docs`** — see `p04-docker-qdrant.txt`, `p04-curl-qdrant-collection.txt` |
| Ingest | `python ingest.py` (updated `data/sample.md` Section C); `python ingest_web.py --synthetic-evidence` (web slice) |
| Ragas | `python ragas_eval.py --mode baseline`; `python ragas_eval.py --mode batch --sleep-between 2` — **`qwen3:8b`** judge via **`OLLAMA_EVAL_LLM_MODEL`** (default); generation **`llama3.2`** |
| Consumer | `python consumer_demo.py` — `p04-consumer-demo.txt` |
| Deps | `p04-pip-freeze.txt` (includes **ragas**, **langchain-ollama**) |

**Evidence:** `executions/evidence/p04/` — **`README.md`**, transcripts above. Validation: **`validation/P04-validation.md`** **PASS**.

### Case study — Local knowledge spine (E2E)

**Status:** **Documented** with this P04 slice. Linear operator path: [`case-study/RUNBOOK.md`](../case-study/RUNBOOK.md) (scenario: [`SCENARIO.md`](../case-study/SCENARIO.md), requirements: [`REQUIREMENTS.md`](../case-study/REQUIREMENTS.md)); optional helpers under [`case-study/tools/`](../case-study/tools/); diagram source [`case-study/diagrams/e2e-flow.mmd`](../case-study/diagrams/e2e-flow.mmd). **CI:** `.github/workflows/retrieval-backbone-ragas-dry.yml` exercises `ragas_eval.py --mode batch --synthetic-rows --dry-dataset` on PR/push to `main` when `build/` changes.
