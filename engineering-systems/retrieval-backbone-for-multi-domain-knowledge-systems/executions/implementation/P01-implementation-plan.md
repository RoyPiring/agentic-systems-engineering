# Implementation plan — P01: Document ingestion and vector indexing (Unstructured and Qdrant)

| Field | Value |
| ----- | ----- |
| System | `retrieval-backbone-for-multi-domain-knowledge-systems` |
| Date | 2026-03-28 |
| Series guide (filename only) | `P01-Document_Ingestion_and_Vector_Indexing_Unstructured_and_Qdrant.md` |
| Depends on | None |

## Outcome

When this phase is done:

- **Qdrant** runs locally (Docker) and accepts HTTP traffic on port **6333**.
- **`build/ingest.py`** loads **Markdown and PDF** from **`build/data/`** via **Unstructured** (`UnstructuredReader`), embeds with **Ollama** `nomic-embed-text`, and upserts into collection **`multi_domain_docs`**.
- Evidence (logs, optional dashboard note, dependency capture) lives under **`executions/evidence/p01/`** with **`execution-record.md`** updated.

## Roadmap

| Phase | Focus |
| ----- | ----- |
| 1 | Qdrant + Ollama + Python **3.12** venv and pinned deps |
| 2 | **`build/data/`** + **`ingest.py`** load path (Unstructured readers) |
| 3 | Vector store wiring: **QdrantVectorStore** + **OllamaEmbedding**; index build |
| 4 | Evidence, validation **PASS**, rollups |

## Key commands (reference)

**Qdrant (Docker, bash):**

```bash
docker run -p 6333:6333 -p 6334:6334 -v "$(pwd)/qdrant_storage:/qdrant/storage:z" qdrant/qdrant
```

**Windows PowerShell volume:** `-v "${PWD}/qdrant_storage:/qdrant/storage"`

**Ollama:**

```bash
ollama pull nomic-embed-text
```

**Dependencies (venv active):**

```bash
pip install llama-index llama-index-readers-file qdrant-client unstructured llama-index-embeddings-ollama llama-index-vector-stores-qdrant
```

**Working directory:** Run **`ingest.py`** with cwd **`build/`** so **`./data`** resolves to **`build/data/`**.

---

## Phase 1 — Toolchain and services

| Step | Complete when |
| ---- | ------------- |
| 1.1 | `curl http://localhost:6333` returns JSON including Qdrant **version** |
| 1.2 | `ollama list` shows **nomic-embed-text** |
| 1.3 | Python **3.12** venv under `build/` (or documented path); packages install without error |

## Phase 2 — Ingest script skeleton

| Step | Complete when |
| ---- | ------------- |
| 2.1 | **`build/data/`** exists with at least one **`.md`** or **`.pdf`** sample |
| 2.2 | **`build/ingest.py`** uses `SimpleDirectoryReader` + `file_extractor` mapping **`.pdf`** and **`.md`** to `UnstructuredReader()` |
| 2.3 | `python ingest.py` (from **`build/`**) prints loaded document count with no crash on chosen sample |

## Phase 3 — Qdrant + embeddings

| Step | Complete when |
| ---- | ------------- |
| 3.1 | `Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")`; LLM unset for this phase if only indexing |
| 3.2 | `QdrantClient(url="http://localhost:6333")` and **`multi_domain_docs`** collection created via index build |
| 3.3 | Script prints success (e.g. **Vector indexing complete.**) and exits **0** |
| 3.4 | **`multi_domain_docs`** is verifiable via **Qdrant HTTP API** (e.g. collection info / points count) with transcript under **`executions/evidence/p01/`** — documented in validation |

## Phase 4 — Evidence and closeout

| Step | Complete when |
| ---- | ------------- |
| 4.1 | **`executions/execution-record.md`** has a **P01** summary (commands run, collection name, evidence pointers) |
| 4.2 | Transcripts under **`executions/evidence/p01/`** (e.g. `p01-pip-freeze.txt`, `p01-ingest-run.txt`, `p01-curl-qdrant.txt`) |
| 4.3 | **`validation/P01-validation.md`** set to **PASS** when accepted |
| 4.4 | **`implementation.md`** and root **`validation.md`** P01 rows match **Executed** / **PASS** |

---

## Done when

- [x] Phases 1–4 satisfied with proof in **`execution-record.md`** and **`executions/evidence/p01/`**
- [x] **`validation/P01-validation.md`** **PASS**
- [x] System rollups updated

## Next

**P02** needs a **stable Qdrant collection** (`multi_domain_docs` or agreed name), **Ollama** embed model available, and documented **chunk metadata** so citation-aware retrieval can point to stored nodes.

## Risks (from series guide)

- **PDF system deps:** Unstructured may require poppler/tesseract; mitigate with Markdown-only first run.
- **Ports 6333/6334:** Resolve conflicts or remap with documented URL changes in script + validation.
- **OOM on embed:** Reduce chunk size / batch size in LlamaIndex settings; record in validation.
