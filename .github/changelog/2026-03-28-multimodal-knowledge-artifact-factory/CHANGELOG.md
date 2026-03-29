# Changelog — multimodal-knowledge-artifact-factory — 2026-03-28

## P01–P04 — Full series closure

**PR:** #5  
**Type:** Engineering System — Update

### Summary

Completes the **P01–P04** series on the multimodal feature branch: **P04** study exports and AIRI integration bridge, operator **`user-guides/`** (per-phase + series), evidence reorganized under **`executions/evidence/p01/`…`p04/`**, and a **`case-study/`** pack (requirements, data, runbook, optional narration audio) for end-to-end review. Domain root indexes (**`README.md`**, **`FEATURE_SYSTEMS.md`**, **`engineering-systems/README.md`**) describe the full shipped depth.

### Projects (this PR)

- P01: Scaffold pipeline and parse Markdown content
- P02: Local audio narrations (stub WAV; optional Edge TTS for case study)
- P03: Knowledge Viewer (Dioxus desktop; optional markdown path argument)
- P04: AIRI handoff + study artifact export (`export` binary, `integration.py`)

### Evidence

- Transcripts and artifacts under **`engineering-systems/multimodal-knowledge-artifact-factory/executions/evidence/p01/`** … **`p04/`** (including **`p02/audio/`**, **`p04/exports/`** where applicable).
- Rollup: **`validation.md`**, per-phase **`validation/P0X-validation.md`**, **`executions/execution-record.md`**.
- Case study: **`case-study/README.md`**, **`REQUIREMENTS.md`**, **`RUNBOOK.md`**, **`data/`**.
