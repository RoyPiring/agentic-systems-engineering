# ADR-001: Local Ollama and Qdrant for zero recurring API cost

## Status

Accepted

## Context

The series targets **$0 recurring spend** on third-party inference and hosted vector SaaS. Operators can run **Docker** (or native installs) for **Qdrant** and **Ollama** on a workstation-class machine.

## Decision

Use **local Qdrant** as the vector database and **Ollama** as the default provider for **LLM completion** and **text embeddings** in the retrieval path, unless a phase explicitly documents an optional alternative.

## Alternatives considered

- **OpenAI (or other cloud) APIs** — Low operational overhead but recurring cost and external data handling.
- **Managed Pinecone / Weaviate Cloud** — Strong ops story but violates the default “no paid tier required” posture.
- **In-process FAISS-only** — Simple for demos but weaker multi-session service story and fewer production-like ops patterns than Qdrant.

## Consequences

**Positive:** Reproducible portfolio narrative; no API keys for core flows; clear cost guardrails.

**Negative / tradeoffs:** Local RAM/CPU constraints; operator must manage models (`ollama pull`) and container lifecycle.

**Follow-ups:** Document minimum resources in per-phase validation and `build/README.md` as code lands.
