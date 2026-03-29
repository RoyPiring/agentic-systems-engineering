# Implementation plan — P03: Live web content integration (Firecrawl)

| Field | Value |
| ----- | ----- |
| System | `retrieval-backbone-for-multi-domain-knowledge-systems` |
| Date | 2026-03-29 |
| Series guide (filename only) | `P03-Live_Web_Content_Integration_Firecrawl.md` |
| Depends on | P02 validation **PASS**; **`build/ingest.py`** and **`build/query_pipeline.py`** working; Qdrant **`multi_domain_docs`**; **Ollama** `nomic-embed-text` + `llama3.2` |

## Outcome

When this phase is done:

- **`build/ingest_web.py`** crawls **targeted** URLs via **Firecrawl** (local instance), maps each page to **LlamaIndex** `Document` objects with **`source_url`** (or equivalent) in **`metadata`**.
- New chunks embed with **`OllamaEmbedding(model_name="nomic-embed-text")`** — **same model and dimension as P01** — and **append** to the existing Qdrant collection **`multi_domain_docs`** (no accidental collection wipe).
- **`build/query_pipeline.py`** answers at least one query whose grounding **requires** web-ingested content, with **Citations** showing the **live URL** from node metadata.
- Evidence under **`executions/evidence/p03/`** and **`executions/execution-record.md`** updated; **`validation/P03-validation.md`** **PASS**.

## Roadmap

| Phase | Focus |
| ----- | ----- |
| 1 | **Firecrawl** local (Docker), health check, **`ingest_web.py`** client + constrained test crawl |
| 2 | **LlamaIndex** `Document` build from crawl markdown + **provenance metadata** |
| 3 | **Qdrant** append / index update; dimension and collection parity with P01 |
| 4 | **End-to-end** query + URL citations, evidence, validation **PASS**, rollups |

## Key commands (reference)

**Firecrawl (local, series guide):**

```bash
docker run -d -p 3002:3002 ghcr.io/mendableai/firecrawl
curl http://localhost:3002/health
```

**Python client (extend `build/requirements.txt`):**

```bash
pip install firecrawl-py
```

**Prerequisites (same as P01/P02):**

- Qdrant **`http://localhost:6333`**, collection **`multi_domain_docs`**
- Ollama **`nomic-embed-text`** (embed) — **must match P01 indexing**

**Working directory:** Run **`ingest_web.py`** with cwd **`build/`** (same convention as **`ingest.py`** / **`query_pipeline.py`**).

---

## Phase 1 — Firecrawl wiring and constrained crawl

| Step | Complete when |
| ---- | ------------- |
| 1.1 | **Firecrawl** container up; **`curl http://localhost:3002/health`** returns **`{"status":"ok"}`** (or documented equivalent) — capture in **`p03-firecrawl-health.txt`** |
| 1.2 | **`build/ingest_web.py`** exists; **`FirecrawlApp(api_url="http://localhost:3002")`** (or current SDK constructor) connects without auth errors for local mode |
| 1.3 | **Crawl/scrape** config sets **strict limits** (e.g. **`limit`** / **`maxDepth`** per series guide — avoid unconstrained domains) |
| 1.4 | **Dry run:** script prints **clean markdown** (or mapped text) for a **small** public docs URL to stdout — transcript **`p03-firecrawl-sample.txt`** |

**Common mistakes:** Unbounded crawl → rate limits / huge payloads. JS-heavy pages → add **`waitFor`** / scrape options if needed. Cloud Firecrawl tier → prefer **local** image to keep **$0** posture.

## Phase 2 — LlamaIndex documents and metadata

| Step | Complete when |
| ---- | ------------- |
| 2.1 | Each scraped page becomes a **`Document`**; **body** = markdown text field from Firecrawl (not raw full JSON dumped as text) |
| 2.2 | **`metadata`** includes **`source_url`** (and optional **`domain`**) from Firecrawl metadata — **required** for downstream citations |
| 2.3 | Spot-check in Python or log: **`doc.metadata["source_url"]`** matches the crawled page URL |

**Common mistakes:** Wrong field used for text → noise in index. Reserved LlamaIndex keys → use custom keys like **`source_url`**. Missing URL → citations cannot attribute web sources.

## Phase 3 — Append to Qdrant (same vector space as P01)

| Step | Complete when |
| ---- | ------------- |
| 3.1 | **`Settings.embed_model`** (or equivalent) = **`OllamaEmbedding(model_name="nomic-embed-text")`** — **same as P01** |
| 3.2 | **`QdrantVectorStore`** / index load targets **existing** **`multi_domain_docs`** — **append** new nodes; **no** recreate-collection path on default run |
| 3.3 | **`ingest_web.py`** completes with exit **0**; **`GET /collections/multi_domain_docs`** shows **increased** **`points_count`** (or vectors count) — capture **`p03-qdrant-after-web.txt`** |

**Common mistakes:** Different embed model → **dimension mismatch**. New collection or drop → loses P01/P02 corpus unless explicitly intentional (not this phase).

## Phase 4 — Unified retrieval proof and closeout

| Step | Complete when |
| ---- | ------------- |
| 4.1 | Run **`query_pipeline.py`** with a question **answerable only from** newly ingested web content (per series guide intent) |
| 4.2 | **Answer** is grounded; **Citations** / source node print path surfaces **`source_url`** (e.g. **`node.metadata.get("source_url", "N/A")`**) — transcript **`p03-query-web-citation.txt`** |
| 4.3 | **`executions/execution-record.md`** — **P03** summary (commands, Firecrawl note, evidence pointers) |
| 4.4 | **`executions/evidence/p03/`** — health, crawl sample, Qdrant before/after optional, query transcript, **`p03-pip-freeze.txt`** if deps changed |
| 4.5 | **`validation/P03-validation.md`** **PASS**; **`implementation.md`** and root **`validation.md`** P03 rows **Executed** / **PASS** |
| 4.6 | **`user-guides/P03-user-guide.md`** added or updated so an operator can repeat the phase (prereqs, cwd, commands) |

**Common mistakes:** High **temperature** → model ignores context — use **low** temp for eval-style runs. Citations show only node ids → extend print loop to include **`source_url`**.

---

## Done when

- [ ] Phases 1–4 satisfied with proof in **`execution-record.md`** and **`executions/evidence/p03/`**
- [ ] **`validation/P03-validation.md`** **PASS**
- [ ] System rollups and **P03** user guide updated

## Next

**P04** (series): **Ragas** (or equivalent) measurement and packaging over a documented eval set — needs a stable **local + web** corpus and the same **`query_pipeline.py`** surface.
