> ← [User guides](./README.md) · [System README](../README.md)

# Series user guide — Retrieval Backbone (in progress)

**Ordered path (as phases land):**

1. **P01** — [Document ingestion and vector indexing](./P01-user-guide.md): Unstructured → Ollama embeddings → Qdrant **`multi_domain_docs`**. Capture evidence per guide → [`executions/evidence/p01/`](../executions/evidence/p01/).
2. **P02** — [Citation-aware retrieval](./P02-user-guide.md): LlamaIndex + Ollama LLM over the same collection; **Answer** + **Citations**. Capture evidence → [`executions/evidence/p02/`](../executions/evidence/p02/).
3. **P03** — Web augmentation (guide pending).
4. **P04** — Quality measurement / packaging (guide pending).

**Also see:** [User guides index](./README.md) · [Implementation](../implementation.md) · [build/README.md](../build/README.md)

When **P03–P04** are validated, expand this file with the full end-to-end command order and links to each `P0X-user-guide.md`.
