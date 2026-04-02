> ← [User guides](./README.md) · [System README](../README.md)

# User guide — P04: Ragas quality measurement and packaged service

**Validation:** [P04-validation.md](../validation/P04-validation.md) — **PASS** with evidence under [`../executions/evidence/p04/`](../executions/evidence/p04/) (see **[README.md](../executions/evidence/p04/README.md)**).

## What you get

| Artifact | Role |
| --- | --- |
| **`build/retrieval_service.py`** | **`RetrievalBackboneConfig`** (env or `from_mapping`) + **`RetrievalBackboneService.query()`** → **`QueryResult`** (`answer`, `contexts` for Ragas, structured **`citations`**) |
| **`build/query_pipeline.py`** | CLI wrapper over the same service (P02 UX preserved) |
| **`build/ragas_eval.py`** | Baseline / batch Ragas over the **live** pipeline; **`--synthetic-rows`** when Qdrant is unavailable |
| **`build/consumer_demo.py`** | Smoke test using **only** the public service imports |

**Cost posture:** RAG generation uses **Ollama** (`llama3.2` by default). Ragas **judge** LLM is also local via **`langchain-ollama`** — default **`qwen3:8b`** (`OLLAMA_EVAL_LLM_MODEL`) because it follows JSON and free-form prompts more reliably than some small models; no OpenAI key is required on the default path.

## Prerequisites

1. **P01–P03** complete: **`multi_domain_docs`** populated (re-run **`ingest.py`** after updating `data/sample.md`; run **`ingest_web.py --synthetic-evidence`** or live Firecrawl for web-style chunks).
2. **Qdrant** reachable (**`QDRANT_URL`**, default `http://localhost:6333`). You can reuse an existing container (e.g. start **`qdrant-p01`** if it already maps **6333**).
3. **Ollama:** **`nomic-embed-text`**, **`llama3.2`** (generation), and **`qwen3:8b`** (recommended judge) — `ollama pull …`.
4. **Python venv under `build/`:** `pip install -r requirements.txt`.

## How to run

Working directory: **`build/`**.

1. **Consumer API smoke** (no direct Qdrant imports in the demo script):

   ```bash
   python consumer_demo.py
   python consumer_demo.py --query "What does the corpus say about PDF ingestion?"
   ```

2. **Ragas baseline** (one query, both metrics):

   ```bash
   python ragas_eval.py --mode baseline
   ```

3. **Ragas batch** (markdown / PDF-topic / web-style questions; optional throttle):

   ```bash
   python ragas_eval.py --mode batch --sleep-between 2
   ```

4. **No Qdrant** (fixed rows + Ragas only — CI / blocked Docker):

   ```bash
   python ragas_eval.py --mode batch --synthetic-rows
   ```

5. **Inspect dataset JSON without calling judge LLMs:**

   ```bash
   python ragas_eval.py --mode batch --dry-dataset
   ```

## Environment reference

| Variable | Purpose |
| --- | --- |
| `QDRANT_URL`, `QDRANT_COLLECTION` | Vector store |
| `OLLAMA_EMBED_MODEL` | Embeddings (must match P01) |
| `OLLAMA_LLM_MODEL` | **Answer generation** in the backbone |
| `OLLAMA_EVAL_LLM_MODEL` | **Ragas** judge (`context_precision` uses JSON mode; `answer_relevancy` plain) |
| `OLLAMA_EVAL_TIMEOUT` | Judge HTTP timeout (seconds) |
| `RAG_SIMILARITY_TOP_K` | Retrieval depth for the service |

## Evidence

Capture transcripts per **[P04 validation](../validation/P04-validation.md)** and **[evidence/p04/README.md](../executions/evidence/p04/README.md)**.

## Next

Series complete (4/4). Optional: add CI that runs **`--synthetic-rows`** on a schedule; optional full re-run against **`llama3.2`** judge only if you accept possible **NaN** metrics when JSON parsing fails.
