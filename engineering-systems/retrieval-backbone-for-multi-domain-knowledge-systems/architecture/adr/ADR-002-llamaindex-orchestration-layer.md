# ADR-002: LlamaIndex as the retrieval orchestration layer

## Status

Accepted

## Context

The backbone must compose **parsing/chunking**, **vector retrieval**, **LLM synthesis**, and **citation-style provenance** across multiple projects without rewriting glue code each phase.

## Decision

Standardize on **LlamaIndex** for query engines / pipelines, retriever wiring, and integration points toward **Qdrant** and **Ollama**, while keeping ingestion utilities (e.g. **Unstructured**) as explicit preprocessing steps where the guides require them.

## Alternatives considered

- **Framework-free Python** — Maximum control but higher maintenance and inconsistent citation patterns across phases.
- **LangChain-only stack** — Viable ecosystem; not chosen for this series because the curriculum centers on LlamaIndex patterns for RAG composition.
- **Vendor-specific RAG SaaS** — Fastest demo; conflicts with local-first and reproducibility goals.

## Consequences

**Positive:** Shared abstractions for retrievers, nodes, and query engines; easier to show end-to-end traceability in code.

**Negative / tradeoffs:** Framework upgrades can break APIs—pin versions in execution evidence.

**Follow-ups:** Record pinned versions per phase in `executions/execution-record.md` and validation artifacts.
