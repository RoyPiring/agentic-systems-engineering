> ← [User guides](./README.md) · [System README](../README.md)

# Series user guide — Retrieval Backbone (P01–P03 shipped; P04 pending)

**Ordered path (as phases land):**

1. **P01** — [Document ingestion and vector indexing](./P01-user-guide.md): Unstructured → Ollama embeddings → Qdrant **`multi_domain_docs`**. Capture evidence per guide → [`executions/evidence/p01/`](../executions/evidence/p01/).
2. **P02** — [Citation-aware retrieval](./P02-user-guide.md): LlamaIndex + Ollama LLM over the same collection; **Answer** + **Citations**. Capture evidence → [`executions/evidence/p02/`](../executions/evidence/p02/).
3. **P03** — [Live web ingest (Firecrawl)](./P03-user-guide.md): **`build/ingest_web.py`** appends web chunks with **`source_url`**; query via P02 script. Evidence → [`executions/evidence/p03/`](../executions/evidence/p03/).
4. **P04** — Quality measurement / packaging (guide pending).

**Also see:** [User guides index](./README.md) · [Implementation](../implementation.md) · [build/README.md](../build/README.md)

**P03** is **PASS** — see [validation/P03-validation.md](../validation/P03-validation.md). When **P04** validates, expand this file with the full end-to-end command order (Ragas + packaging) and link **`P04-user-guide.md`** when published.
