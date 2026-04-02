# Sample corpus — P01 smoke

This file exercises **Markdown** ingestion for the retrieval backbone.

## Section A

Vector databases store embeddings for similarity search. **Qdrant** is used locally in this series.

## Section B

**Ollama** runs `nomic-embed-text` for embeddings without cloud API keys.

## Section C — PDF and mixed file types

**Unstructured** can partition **PDF** documents into elements for the same Qdrant collection as Markdown. After you add a `.pdf` under `data/`, run `ingest.py` so eval batches can retrieve PDF-sourced chunks alongside Markdown and web pages.
