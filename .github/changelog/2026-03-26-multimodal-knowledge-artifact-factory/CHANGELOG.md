# Changelog — multimodal-knowledge-artifact-factory — 2026-03-26

All entries for this **engineering system** on **this date**. Multiple project phases merged the same day live in this single file (no duplicate changelog paths per PR).

## P01 — Markdown parse pipeline

**PR:** #2  
**Type:** Engineering System — Update

**Summary:** Delivers **P01** of the Multimodal Knowledge Artifact Factory series: a Rust CLI under `build/` that parses Markdown with `pulldown-cmark` and emits structured `H{n}:` / `P:` lines for downstream TTS and UI. Includes execution record, per-project validation **PASS**, and run transcripts under `executions/evidence/`. Per-project plans live under `executions/implementation/`.

**Projects (this PR):** P01: Markdown parse pipeline (**shipped**); P02–P04: — (not in this PR).

**Evidence:**

- `executions/execution-record.md` — P01 summary
- `executions/implementation/P01-implementation-plan.md`
- `executions/evidence/` — `rust-toolchain.txt`, `p01-cargo-build.txt`, `complex-sample-run.txt`, `p01-negative-missing-file.txt`
- `validation/P01-validation.md` — **PASS**; rollup in `validation.md`

## P02 — Local audio bridge

**PR:** #3  
**Type:** Engineering System — Update

**Summary:** Delivers **P02** of the Multimodal Knowledge Artifact Factory series: `build/tts_inference.py` consumes parser structured output (`H{n}:` / `P:`), chunks text, and writes `.wav` evidence under `executions/evidence/p02-audio/` (default standard-library WAV path). Execution record, validation **PASS**, and rollout docs updated. Intended to merge via PR from `feature/multimodal-knowledge-artifact-factory-p02`.

**Projects (this PR):** P01: Markdown parse pipeline (**prior merge**); P02: Local audio bridge / chunked WAV (**this PR**); P03–P04: — (not in this PR).

**Evidence:**

- `executions/execution-record.md` — P02 summary
- `executions/implementation/P02-implementation-plan.md`
- `executions/evidence/` — `p01-stdout-for-p02.txt`, `p02-pipeline-run.txt`, `p02-audio/`, `p02-audio-listing.txt`, `p02-python-version.txt`, edge-case transcripts
- `validation/P02-validation.md` — **PASS**; rollup in `validation.md`
