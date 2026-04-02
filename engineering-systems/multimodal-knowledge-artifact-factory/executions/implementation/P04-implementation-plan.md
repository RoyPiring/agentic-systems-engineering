# Implementation plan — P04: Multimodal study artifact assembly (AIRI)

| | |
|--|--|
| **System** | multimodal-knowledge-artifact-factory |
| **Last updated** | 2026-03 |
| **Series guide (filename only)** | `P04-Integrate_AIRI_for_Multimodal_Study_Artifact_Assembly.md` |
| **Depends on** | P01 **PASS** — parse + `lib` model; P02 **PASS** — `executions/evidence/p02/audio/*.wav`; P03 **PASS** — `knowledge_viewer` + section ↔ audio mapping ([ADR-004](../../architecture/adr/ADR-004-vibevoice-tts-and-airi-multimodal-assembly.md)) |

## Outcome

- **Static exports** — Rust **`export`** binary under `build/` (`cargo run --bin export` with documented args) writes **`flashcards.json`** (JSON array of term/definition objects) and **`quiz.md`** (questions derived from section headings / structure) into a documented directory under **`executions/evidence/`** (for example `executions/evidence/p04/exports/`).
- **Integration script** — **`build/integration.py`** resolves **relative** paths from the engineering-system root to: P02 WAVs, P03 viewer artifact paths (binary and/or source as documented), and P04 export outputs; documents environment variables or CLI flags used to launch **AIRI** (or the operator’s equivalent local command).
- **End-to-end narrative** — Repeatable command sequence (parser → TTS stub → optional viewer build → export → integration) captured in the execution record with transcripts under **`executions/evidence/`** (`p04-*` prefix).
- **Validation** — **`validation/P04-validation.md`** at **PASS** (or **PASS (conditional)** with explicit rationale if AIRI UI cannot be reproduced in CI) when this phase is accepted; system rollups updated.

## Roadmap

| Phase | Focus |
| ----- | ----- |
| **1** | Add **`serde`** / **`serde_json`**; new **`src/bin/export.rs`** + **`[[bin]]`**; implement flashcard + quiz writers; run once and capture listing / file hashes or small transcripts |
| **2** | **`integration.py`** — path discovery from repo layout; documented AIRI launch contract; smoke run without hardcoded absolute paths |
| **3** | Full pipeline ordering: sample markdown → P01 → P02 → export → integration; capture **AIRI / integration stdout or logs** in transcripts when the desktop app is available (no raster/UI image evidence required) |
| **4** | Execution record, evidence, **`validation/P04-validation.md`**, **`implementation.md`** / **`validation.md`** rollups |

## Phase 1 — Export binary (Rust)

| Step | Complete when |
| ---- | ------------- |
| 1.1 | **`Cargo.toml`**: `serde` + `serde_json` with `derive` as needed; new **`[[bin]] name = "export"`** pointing at **`src/bin/export.rs`** |
| 1.2 | Binary reads input markdown (default **`samples/complex-sample.md`** from `build/` cwd or CLI path arg) using **`mkaf_md_parse`** (`parse_markdown_blocks` / `blocks_to_sections`) |
| 1.3 | **`flashcards.json`**: valid JSON array; each card ties a **term** (e.g. section heading) to a **definition** (e.g. joined paragraphs); **`serde_json`** handles escaping |
| 1.4 | **`quiz.md`**: markdown with one section or list per heading (question from heading; answer body from following text — format documented in **`build/README.md`**) |
| 1.5 | Successful run recorded under **`executions/evidence/`** (e.g. `p04-export-run.txt`, optional `p04-export-listing.txt`) |

## Phase 2 — Python integration bridge

| Step | Complete when |
| ---- | ------------- |
| 2.1 | **`build/integration.py`** exists; **`python --version`** compatible with **`build/README.md`** |
| 2.2 | Script resolves paths to **`executions/evidence/p02/audio/`**, P04 export dir, and P03-related paths (viewer binary under `build/target/...` and/or `src/bin/knowledge_viewer.rs` as **documentation** anchors — no secrets) |
| 2.3 | Documented invocation of **AIRI** (executable name, config file, or env vars — whatever the operator’s install requires); script fails with a **clear message** if AIRI is not on `PATH` / expected location |
| 2.4 | Smoke: `python integration.py --help` (or dry-run flag if implemented) and one real run transcript in **`executions/evidence/`** when AIRI is available |

## Phase 3 — End-to-end pipeline

| Step | Complete when |
| ---- | ------------- |
| 3.1 | From documented cwd: run P01 CLI on sample → regenerate or reuse P01 stdout for P02 as needed |
| 3.2 | Run P02 stub pipeline → WAVs present under **`executions/evidence/p02/audio/`** |
| 3.3 | Run **`export`** → **`flashcards.json`** + **`quiz.md`** refreshed |
| 3.4 | Run **`integration.py`** → AIRI launches **or** documented **skip** with honest validation note |
| 3.5 | Optional terminal log or launch transcript of AIRI showing assembled assets under **`executions/evidence/`** when feasible |

## Phase 4 — Closeout

| Item | Complete when |
| ---- | ------------- |
| Summary | [Execution record](../execution-record.md) updated for P04 with commands actually run |
| Evidence | Transcripts and execution logs under [`../evidence/`](../evidence/) |
| Validation | [P04 validation](../../validation/P04-validation.md) **PASS** or **PASS (conditional)** with rationale |
| Rollups | Root [`implementation.md`](../../implementation.md) and [`validation.md`](../../validation.md) show P04 **Executed** |
| Domain index | If this slice merges, update the domain repo’s featured / index tables so strangers see **P04** status (same discipline as prior phases) |

## Done when

- [x] Phases 1–3 satisfied with observable artifacts and transcripts.
- [x] Phase 4 evidence and per-project validation **PASS (conditional)** (AIRI UI not observed on build host).
- [x] System rollups updated.

## Next

Series **P01–P04** complete after this phase **PASS**; further work is optional hardening (neural TTS, richer AIRI metadata), not a fifth project.
