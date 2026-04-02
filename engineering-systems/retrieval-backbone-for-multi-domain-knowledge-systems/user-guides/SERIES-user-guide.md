> ← [User guides](./README.md) · [System README](../README.md)

# Series user guide — Retrieval Backbone (P01–P04 shipped)

**Ordered path (as phases land):**

1. **P01** — [Document ingestion and vector indexing](./P01-user-guide.md): Unstructured → Ollama embeddings → Qdrant **`multi_domain_docs`**. Capture evidence per guide → [`executions/evidence/p01/`](../executions/evidence/p01/).
2. **P02** — [Citation-aware retrieval](./P02-user-guide.md): LlamaIndex + Ollama LLM over the same collection; **Answer** + **Citations**. Capture evidence → [`executions/evidence/p02/`](../executions/evidence/p02/).
3. **P03** — [Live web ingest (Firecrawl)](./P03-user-guide.md): **`build/ingest_web.py`** appends web chunks with **`source_url`**; query via P02 script. Evidence → [`executions/evidence/p03/`](../executions/evidence/p03/).
4. **P04** — [Ragas + packaged service](./P04-user-guide.md): **`ragas_eval.py`** (baseline + batch), **`consumer_demo.py`** (public API only). Evidence → [`executions/evidence/p04/`](../executions/evidence/p04/).

**Also see:** [User guides index](./README.md) · [Implementation](../implementation.md) · [build/README.md](../build/README.md)

**P03** — [validation/P03-validation.md](../validation/P03-validation.md) **PASS**. **P04** — [validation/P04-validation.md](../validation/P04-validation.md) **PASS**.
