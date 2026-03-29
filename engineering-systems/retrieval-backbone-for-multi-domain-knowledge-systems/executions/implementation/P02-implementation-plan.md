# Implementation plan — P02: Citation-aware retrieval pipeline (LlamaIndex and Ollama)

| Field | Value |
| ----- | ----- |
| System | `retrieval-backbone-for-multi-domain-knowledge-systems` |
| Date | 2026-03-28 |
| Series guide (vault, filename only) | `P02-Citation-Aware_Retrieval_Pipeline_LlamaIndex_and_Ollama.md` |
| Depends on | P01 validation **PASS**; Qdrant **`multi_domain_docs`** populated; chunk metadata compatible with citation display |

## Outcome

When this phase is done:

- **`build/query_pipeline.py`** connects **LlamaIndex** to the **existing** local **Qdrant** store (same collection and embedding model as P01).
- **Global `Settings`** use **Ollama** for **LLM** (`llama3.2`) and **embeddings** (`nomic-embed-text`) — no paid OpenAI defaults.
- A **query engine** retrieves with **`similarity_top_k` = 3**, returns **natural-language answers**, and prints a **Citations** section from **`source_nodes`** (IDs, text snippets, safe metadata such as filename via `.get()`).
- Evidence lives under **`executions/evidence/p02/`** with **`executions/execution-record.md`** updated.

## Roadmap

| Phase | Focus |
| ----- | ----- |
| 1 | Ollama + LlamaIndex **Settings**; **QdrantVectorStore** + **VectorStoreIndex** load from existing collection |
| 2 | **Query engine**; extract **`response`** + **`source_nodes`** |
| 3 | Custom **text QA prompt**; terminal layout: answer + **Citations** |
| 4 | End-to-end run, evidence, validation **PASS**, rollups |

## Key commands (reference)

**Ollama (models):**

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

**Dependencies (extend P01 venv; cwd `build/`):**

```bash
pip install llama-index llama-index-vector-stores-qdrant llama-index-llms-ollama llama-index-embeddings-ollama qdrant-client
```

**Qdrant:** Same as P01 — `http://localhost:6333`, collection **`multi_domain_docs`**.

**Working directory:** Run **`query_pipeline.py`** with cwd **`build/`** so paths and env match P01 ingest.

---

## Phase 1 — LlamaIndex + Qdrant wiring (local-only)

| Step | Complete when |
| ---- | ------------- |
| 1.1 | **`build/query_pipeline.py`** exists; imports LlamaIndex, Ollama LLM/embed, Qdrant client / vector store |
| 1.2 | `Settings.llm` = **Ollama** `llama3.2`; `Settings.embed_model` = **Ollama** `nomic-embed-text` (must match P01 indexing model) |
| 1.3 | `QdrantClient` targets **`http://localhost:6333`**; **`QdrantVectorStore`** + **`VectorStoreIndex`** load the **existing** index (no accidental empty collection) |
| 1.4 | Script runs without missing-dependency errors; Qdrant connection does not time out |

**Common mistakes:** OpenAI auth errors → set **Settings** before index use. Wrong embed model → zero/incorrect retrieval vs P01.

## Phase 2 — Query engine and source nodes

| Step | Complete when |
| ---- | ------------- |
| 2.1 | **`VectorStoreIndex.as_query_engine(similarity_top_k=3)`** (or equivalent) configured |
| 2.2 | Helper (or inline flow) runs **`query_engine.query(...)`** and reads **`response.response`** (text) and **`response.source_nodes`** |
| 2.3 | For a test question, **`source_nodes`** length is **≤ 3** and non-empty when the corpus supports it |

**Common mistakes:** `similarity_top_k` too high for local LLM context. Treating result as plain string — use response object fields.

## Phase 3 — Citation-aware prompt and output

| Step | Complete when |
| ---- | ------------- |
| 3.1 | Custom **text QA** (or response synthesizer) prompt instructs the model to **cite** context (e.g. source name / chunk id) per series guide |
| 3.2 | Stdout (or structured print) separates **Answer** from a **Citations** section |
| 3.3 | Citations loop **`source_nodes`**: node id, text snippet, metadata via **`.get()`** (avoid **KeyError** on missing filename) |

**Common mistakes:** Vague prompt → sloppy citations. Missing metadata keys → use safe access.

## Phase 4 — Evidence and closeout

| Step | Complete when |
| ---- | ------------- |
| 4.1 | **`executions/execution-record.md`** has a **P02** summary (commands, query example, evidence pointers) |
| 4.2 | Transcripts under **`executions/evidence/p02/`** (e.g. `p02-query-run.txt`, `p02-ollama-list.txt`, optional `p02-pip-freeze.txt`) |
| 4.3 | **`validation/P02-validation.md`** set to **PASS** when accepted |
| 4.4 | **`implementation.md`** and root **`validation.md`** P02 rows match **Executed** / **PASS** |

---

## Done when

- [ ] Phases 1–4 satisfied with proof in **`execution-record.md`** and **`executions/evidence/p02/`**
- [ ] **`validation/P02-validation.md`** **PASS**
- [ ] System rollups updated

## Next

**P03** (series): broaden ingestion sources (e.g. live web); this **`query_pipeline.py`** remains the retrieval/citation surface for evaluation.

## Risks (from series guide)

- **Paid API slip:** LlamaIndex defaults to cloud LLM/embed if **Settings** not set — mitigate by setting **Settings** at startup and documenting in validation.
- **Embed mismatch:** Retrieval model must match P01 **`nomic-embed-text`**.
- **Ollama down:** Connection refused on **`localhost:11434`** — verify service before runs.
- **Empty retrieval:** If answers ignore corpus, print raw **`source_nodes`** before synthesis to verify vector search.

## Source

Curriculum steps and checkpoints are derived from the vault production doc:

`02-BUILD/04-Project-Library/06-Agentic/Retrieval-Backbone-For-Multi-Domain-Knowledge-Systems/documents/projects/03-production/P02-Citation-Aware_Retrieval_Pipeline_LlamaIndex_and_Ollama.md`

(Path is relative to the **09-tech-learning-builder** workspace, not this portfolio repo.)
