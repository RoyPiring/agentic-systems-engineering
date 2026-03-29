> ← [Home](./README.md)

# Changelog

All notable changes to this portfolio are documented here in reverse-chronological order. Detailed entries live under [`.github/changelog/`](.github/changelog/README.md), grouped by **date + engineering-system folder** (one `CHANGELOG.md` per folder; multiple projects the same day share that file). **Index:** [`.github/SLICE_LAYOUT.md`](.github/SLICE_LAYOUT.md).

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

## 2026-03-27 — Multimodal (P03 — Knowledge Viewer)

Dioxus 0.7.3 desktop Knowledge Viewer: shared parser, section navigation, Play Narration → P02 WAV mapping. PR workflow and validation PASS.

- **PR #4**
- [Changelog](.github/changelog/2026-03-27-multimodal-knowledge-artifact-factory/CHANGELOG.md)

---

## 2026-03-26 — Multimodal (P01 + P02)

**P01:** Rust CLI parser (`pulldown-cmark 0.11`), scaffold, architecture with ADRs, first evidence artifacts. **P02:** Python `tts_inference.py` stub pipeline → chunked WAV under `executions/evidence/p02-audio/`. CI (markdownlint + link check + structure validation) configured.

- **PR #2** — P01
- **PR #3** — P02
- [Changelog (both sections)](.github/changelog/2026-03-26-multimodal-knowledge-artifact-factory/CHANGELOG.md)
