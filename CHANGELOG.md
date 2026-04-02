> ← [Home](./README.md)

# Changelog

All notable changes to this portfolio are documented here in reverse-chronological order. Detailed entries live under [`.github/changelog/`](.github/changelog/README.md), grouped by **date + engineering-system folder** (one `CHANGELOG.md` per folder; multiple projects the same day share that file). **Index:** [`.github/SLICE_LAYOUT.md`](.github/SLICE_LAYOUT.md).

---

## 2026-04-01

### Retrieval Backbone — Multi-Domain Knowledge (P04)

Ragas quality measurement (**context_precision**, **answer_relevancy**) with injected Ollama; **`RetrievalBackboneService`** packaged API + **`consumer_demo.py`**; evidence **`p04/*`**, validation **PASS**; **Local knowledge spine** case study (**`case-study/`** RUNBOOK + SCENARIO + tools + diagram); **Ragas dry-dataset** CI workflow; slot **#1** series complete (**P01–P04**).

- **PR:** *(add link when opened)*
- [Changelog](.github/changelog/2026-04-01-retrieval-backbone-for-multi-domain-knowledge-systems/CHANGELOG.md)
- [Pre-merge review — P04](.github/code-review/2026-04-01-retrieval-backbone-for-multi-domain-knowledge-systems/PRE_MERGE_REVIEW_P04.md)
- [PR body — P04](.github/pull-requests/2026-04-01-retrieval-backbone-for-multi-domain-knowledge-systems/PR_BODY_P04.md)

---

## 2026-03-29

### Retrieval Backbone — Multi-Domain Knowledge (P02)

Citation-aware query pipeline (`query_pipeline.py`), LlamaIndex + Ollama + Qdrant; evidence `p02/*`, validation PASS; dependency alignment for qdrant-client 1.17+. Small multimodal doc alignment (operator runbooks / validation pairing).

- **PR [#7](https://github.com/RoyPiring/agentic-systems-engineering/pull/7)**
- [Changelog](.github/changelog/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/CHANGELOG.md) (see **P02** section)
- [Pre-merge review — P02](.github/code-review/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/PRE_MERGE_REVIEW.md)
- [PR body — P02](.github/pull-requests/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/PR_BODY.md)

### Retrieval Backbone — Multi-Domain Knowledge (P03)

Web ingest (`ingest_web.py`, Firecrawl v1, Qdrant append, `source_url` citations); `--synthetic-evidence` when Firecrawl is unavailable; evidence `p03/*`, validation **PASS**. Domain indexes and multimodal cross-link updated.

- **PR [#8](https://github.com/RoyPiring/agentic-systems-engineering/pull/8)**
- [Changelog](.github/changelog/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/CHANGELOG.md) (see **P03** section)
- [Pre-merge review — P03](.github/code-review/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/PRE_MERGE_REVIEW_P03.md)
- [PR body — P03](.github/pull-requests/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/PR_BODY_P03.md)

---

## 2026-03-28

### Retrieval Backbone — Multi-Domain Knowledge (P01)

Document ingestion and vector indexing: Unstructured + Ollama embeddings + Qdrant; evidence and validation PASS; portfolio slot **#1** aligned.

- **PR [#6](https://github.com/RoyPiring/agentic-systems-engineering/pull/6)**
- [Changelog](.github/changelog/2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems/CHANGELOG.md)
- [Pre-merge review](.github/code-review/2026-03-28-retrieval-backbone-for-multi-domain-knowledge-systems/PRE_MERGE_REVIEW.md)

### Multimodal Knowledge Artifact Factory (full series)

Full series P01–P04 merged: local markdown pipeline through parse, TTS bridge, Dioxus desktop viewer, study exports, and AIRI integration. Case study, user guides, and per-project evidence layout complete.

- **PR #5** — Full series squash merge
- **Tag:** `v1.0.0-multimodal-knowledge-artifact-factory`
- [Changelog](.github/changelog/2026-03-28-multimodal-knowledge-artifact-factory/CHANGELOG.md)

---

## 2026-03-27

### Multimodal Knowledge Artifact Factory (P03 — Knowledge Viewer)

Dioxus 0.7.3 desktop Knowledge Viewer: shared parser, section navigation, Play Narration → P02 WAV mapping. PR workflow and validation PASS.

- **PR #4**
- [Changelog](.github/changelog/2026-03-27-multimodal-knowledge-artifact-factory/CHANGELOG.md)

---

## 2026-03-26 — Multimodal (P01 + P02)

**P01:** Rust CLI parser (`pulldown-cmark 0.11`), scaffold, architecture with ADRs, first evidence artifacts. **P02:** Python `tts_inference.py` stub pipeline → chunked WAV under `executions/evidence/p02-audio/`. CI (markdownlint + link check + structure validation) configured.

- **PR #2** — P01
- **PR #3** — P02
- [Changelog (both sections)](.github/changelog/2026-03-26-multimodal-knowledge-artifact-factory/CHANGELOG.md)
