> ← [Home](../README.md)

# Engineering Systems — Full Index

All engineering systems in this repository. Each system has five required documents: README, business-context, architecture, implementation, validation.

## Systems

Slot numbers match [ROADMAP.md](../ROADMAP.md).

| # | System | Scope | Tech Stack | Status |
|---|--------|-------|-----------|--------|
| 1 | [retrieval-backbone-for-multi-domain-knowledge-systems](./retrieval-backbone-for-multi-domain-knowledge-systems/) | Citation-aware RAG: Unstructured + Qdrant → LlamaIndex + Ollama → web ingest (Firecrawl) → Ragas | Python, Qdrant, LlamaIndex, Ollama | 🔨 **P01–P03** [PASS](./retrieval-backbone-for-multi-domain-knowledge-systems/validation.md); **P04** planned |
| 10 | [multimodal-knowledge-artifact-factory](./multimodal-knowledge-artifact-factory/) | Local pipeline: markdown → parse → audio → Dioxus viewer → study exports | Rust, Python, Dioxus | ✅ P01–P04 on `main` |

## How systems are added

Systems enter via feature branch and pull request. The PR must pass CI (markdown lint, link check, structure validation) and the review-gate checklist before merge. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full process.
