# Implementation plan — P03: Interactive knowledge views (Dioxus)

| | |
|--|--|
| **System** | multimodal-knowledge-artifact-factory |
| **Last updated** | 2026-03 |
| **Series guide (filename only)** | `P03-Build_Interactive_Knowledge_Views_with_Dioxus.md` |
| **Depends on** | P01 **PASS** — structured parse CLI; P02 **PASS** — `executions/evidence/p02/audio/*.wav` (see [ADR-003](../../architecture/adr/ADR-003-dioxus-for-interactive-knowledge-views.md)) |

## Outcome

- **Dioxus 0.7.3** desktop app under `build/` with window title **Knowledge Viewer**, runnable via `cargo run` (default binary or explicit `--bin` once split).
- **Shared parse model** — markdown sections available to the UI as Rust data (refactor parser from a single `main.rs` into a `lib` target or module as needed so the CLI binary and UI binary both compile).
- **Rendered sections** — headings and paragraph text from parsed markdown appear in the UI (sample path or embedded fixture aligned with P01 sample).
- **Multimodal hook** — per-section control (e.g. **Play Narration**) that resolves to the correct **local** `.wav` under `executions/evidence/p02/audio/` (or documented relative path from the running app’s cwd).
- **Evidence** — build/run transcripts and at least one UI capture under `executions/evidence/` (e.g. `p03-*` files or a `p03-ui/` folder); execution record and validation updated to **PASS** when accepted.

## Roadmap

| Phase | Focus |
| ----- | ----- |
| **1** | Toolchain + crate layout: Dioxus desktop deps/features; optional `src/bin/knowledge_viewer.rs`; blank **Knowledge Viewer** window |
| **2** | Wire structured markdown into UI state; render `H`/`P`-style sections as Dioxus elements |
| **3** | **Play Narration** (or equivalent) per section; path to matching P02 audio; non-blocking click handler (log or local playback) |
| **4** | Clean build, evidence capture, `validation/P03-validation.md` **PASS**, rollups |

## Phase 1 — Toolchain and desktop shell

| Step | Complete when |
| ---- | ------------- |
| 1.1 | Stable Rust matches existing `build/` policy; `cargo build --release` still succeeds for the P01 CLI path (or default binary) after dependency adds |
| 1.2 | **Dioxus 0.7.3** declared in `Cargo.toml` with **desktop** feature set per upstream 0.7 desktop guidance |
| 1.3 | Parser logic **extracted** from a monolithic `main.rs` if required so a second binary (or feature-gated entry) can link the same structs/functions (e.g. `lib.rs` + `src/main.rs` CLI + `src/bin/knowledge_viewer.rs`) |
| 1.4 | Desktop entrypoint runs; **Knowledge Viewer** window opens without panic (blank UI acceptable for end of phase 1) |

## Phase 2 — Data → view

| Step | Complete when |
| ---- | ------------- |
| 2.1 | UI loads or receives the same structured content the series uses (file read of `samples/complex-sample.md` from `build/` or equivalent) |
| 2.2 | Component maps headings and paragraphs to visible layout (`h1`/`p`/`div` style elements per Dioxus patterns) |
| 2.3 | State updates re-render without crash when data changes (smoke with mock or reload) |

## Phase 3 — Audio affordances

| Step | Complete when |
| ---- | ------------- |
| 3.1 | Control appears beside (or under) each logical section |
| 3.2 | Handler resolves **correct** relative path into `../executions/evidence/p02/audio/` (from `build/` cwd) or documents the cwd contract if different |
| 3.3 | Click logs intended path or triggers playback **without** freezing the UI thread |

## Phase 4 — Closeout

| Item | Complete when |
| ---- | ------------- |
| Summary | [Execution record](../execution-record.md) updated for P03 with commands actually run |
| Evidence | Transcripts + at least one UI screenshot or equivalent under [`../evidence/`](../evidence/) |
| Validation | [P03 validation](../../validation/P03-validation.md) shows **PASS** |
| Rollups | Root [`implementation.md`](../../implementation.md) and [`validation.md`](../../validation.md) match P03 status |

## Done when

- [x] Phases 1–3 satisfied with observable UI + audio path behavior.
- [x] Phase 4 evidence and validation **PASS**.
- [x] System rollups updated.

## Next

**P04** — follow [P04-implementation-plan.md](./P04-implementation-plan.md); keep `executions/evidence/p02/audio/` and export paths stable and documented.
