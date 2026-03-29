# Architecture Decision Records

Add one file per decision: `ADR-NNN-kebab-case-title.md` (NNN = sequence, zero-padded).

Copy `_ADR-TEMPLATE.md` when creating a new ADR, then remove the underscore prefix from your new file name.

Summaries in root `architecture.md` should link here; keep the ADR body as the source of truth for rationale and alternatives.

## Index

| ADR | Title |
| --- | --- |
| [ADR-001](./ADR-001-local-ollama-qdrant-zero-recurring-cost.md) | Local Ollama and Qdrant for zero recurring API cost |
| [ADR-002](./ADR-002-llamaindex-orchestration-layer.md) | LlamaIndex as the retrieval orchestration layer |
| [ADR-003](./ADR-003-unstructured-for-heterogeneous-document-ingest.md) | Unstructured for heterogeneous document ingest |
| [ADR-004](./ADR-004-ragas-for-retrieval-quality-measurement.md) | Ragas for retrieval and answer quality measurement |
