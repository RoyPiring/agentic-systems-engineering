# Execution record

Single log for **P01 through P04**. For each project add `## P0X` sections: **summary** of what ran (phase table, key commands, evidence links)—not a full duplicate of `implementation/P0X-implementation-plan.md`.

## Series intent

**Retrieval Backbone — Multi-Domain Knowledge:** citation-aware RAG backbone across markdown, PDF, and web-derived content with local inference, Qdrant indexing, and measured quality (series overview: *Retrieval Backbone — Multi-Domain Knowledge*).

## P01 — Document ingestion and vector indexing

**Status:** **Executed** (2026-03-28) on branch `feature/retrieval-backbone-for-multi-domain-knowledge-systems`.

**What ran**

| Step | Command / artifact |
| --- | --- |
| Qdrant | `docker run -d --name qdrant-p01 -p 6333:6333 -p 6334:6334 qdrant/qdrant:latest` (operator-local; not committed) |
| Ollama | `ollama pull nomic-embed-text` |
| Python | **3.13.11** venv under `build/venv` (plan target 3.12; see `p01-python-version.txt`) |
| Ingest | Windows long-path mitigation: `build/run_ingest_windows.ps1` → `ingest.py`; collection **`multi_domain_docs`**; sample `build/data/sample.md` → **2** document nodes, exit **0** |
| Deps | `pip install -r build/requirements.txt`; `charset-normalizer` rebuilt from sdist (`--no-binary charset-normalizer`) to avoid DLL **MAX_PATH** on this host |

**Evidence:** `executions/evidence/p01/` — `p01-curl-qdrant.txt`, `p01-qdrant-collection.txt`, `p01-ollama-list.txt`, `p01-ingest-run.txt`, `p01-pip-freeze.txt`, `p01-python-version.txt`, `p01-negative-edge.txt`. Validation: **`validation/P01-validation.md`** **PASS**.
