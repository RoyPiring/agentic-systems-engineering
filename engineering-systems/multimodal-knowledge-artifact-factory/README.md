# Multimodal Knowledge Artifact Factory

**Local-first pipeline:** structured Markdown → parse (**P01**) → local audio chunks (**P02**, default **stub** WAV) → interactive **Knowledge Viewer** (**P03**, Dioxus) → study exports + AIRI handoff (**P04**)—without recurring cloud spend.

## Why This Matters

Research and specs often stay stuck in flat text. This system shows how to turn those sources into structured output, then audio and UI, on your own machine—useful for learners, builders who care about privacy and cost, and reviewers who want an end-to-end pattern they can run.

## What This Proves

| Signal | What a reviewer learns | Evidence |
| ------ | ---------------------- | -------- |
| Problem framing | Why multimodal, local delivery matters | `business-context.md` |
| Architectural judgment | Parse → voice → UI → assembly, with ADRs | `architecture.md`, `architecture/adr/` |
| Delivery discipline | Phased implementation with runnable `build/` | `implementation.md` |
| Validation rigor | Checks, commands, and proof paths | `validation.md`, `validation/P01-validation.md` … `validation/P04-validation.md` |

## Intended audience

- Recruiters and non-technical readers (start with `business-context.md`)
- Hiring managers scanning for scope and judgment
- Operators who need **setup first** (clone, install Rust/Python, open the right folder) → start with [**Start here** in `user-guides/README.md`](./user-guides/README.md), then [**SERIES-user-guide.md**](./user-guides/SERIES-user-guide.md) or a single phase guide (**P01–P04**)
- Peer engineers who will open `build/` and run the crate

## How to read this

1. **To run the system:** [`user-guides/README.md`](./user-guides/README.md) → per-phase guides or [`user-guides/SERIES-user-guide.md`](./user-guides/SERIES-user-guide.md) end-to-end
2. `business-context.md`
3. `architecture.md` (plus `architecture/diagrams/` and `architecture/adr/`)
4. `implementation.md`
5. `validation.md`
6. `build/` for the Rust CLI, optional Dioxus **Knowledge Viewer**, Python TTS bridge, and samples

## System summary

- **Problem:** Markdown knowledge stays hard to reuse as audio, UI, or packaged study assets.
- **Scope:** **P01–P04** implemented in this folder: parse, stub-audio bridge, Dioxus viewer, **`export`** study assets + **`integration.py`** AIRI bridge. **AIRI** desktop launch is operator-dependent; validation is **PASS (conditional)** until AIRI is proven locally.
- **Outcome:** End-to-end local pipeline through static exports and path handoff; see [validation/P04-validation.md](./validation/P04-validation.md).
- **Constraints:** Local compute, explicit cost/time posture; no paid API calls in scope for the core story.

## Repository artifacts

- `business-context.md` — problem, objectives, constraints
- `architecture.md` — overview, components, ADR index
- `architecture/diagrams/` — Mermaid sources (standard five)
- `architecture/adr/` — decision records
- `implementation.md` — phased delivery narrative
- `validation.md` — rollup; per-project files under `validation/`
- `build/` — Rust crate (P01 CLI, P03 `knowledge_viewer` with `--features viewer` and **optional markdown path** CLI arg, P04 `export` binary), `tts_inference.py` (P02), `integration.py` (P04), samples
- `executions/` — execution record, `implementation/` (per-project plans), `evidence/` — **per-project layout** **`p01/`** … **`p04/`** (transcripts; **`p02/audio/`** WAVs; **`p04/exports/`** JSON/quiz); details in [`executions/README.md`](./executions/README.md)
- `user-guides/` — **operator** runbooks: **`P01-user-guide.md` … `P04-user-guide.md`** and **`SERIES-user-guide.md`** (full pipeline)
- `case-study/` — **by-design** E2E scenario: [README](./case-study/README.md), [RUNBOOK](./case-study/RUNBOOK.md), [REQUIREMENTS](./case-study/REQUIREMENTS.md); optional **`artifacts/`** copies of P04 exports; optional **spoken** MP3 of `script.md` under [`case-study/data/audio/`](./case-study/data/audio/README.md) (Edge TTS helper in `case-study/tools/`)

**Path mirror (vs some Project Library copies):** this tree uses **`executions/`** (plural), not **`execution/`**, and lives under **`engineering-systems/`**. **`integration.py`** env vars (**`MKAF_*`**, **`AIRI_EXECUTABLE`**) and viewer-binary caveats → [`build/README.md`](./build/README.md) § P04.

## Cross-system references

Part of the **agentic-systems-engineering** portfolio domain; series details live alongside this folder in the same repository layout.
