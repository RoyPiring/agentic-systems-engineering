# Multimodal Knowledge Artifact Factory

**Local-first pipeline:** structured Markdown → parse (**P01**) → local audio chunks (**P02**, default **stub** WAV) → interactive **Knowledge Viewer** (**P03**, Dioxus) → multimodal assembly (**P04**, planned)—without recurring cloud spend.

## Why This Matters

Research and specs often stay stuck in flat text. This system shows how to turn those sources into structured output, then audio and UI, on your own machine—useful for learners, builders who care about privacy and cost, and reviewers who want an end-to-end pattern they can run.

## What This Proves

| Signal | What a reviewer learns | Evidence |
| ------ | ---------------------- | -------- |
| Problem framing | Why multimodal, local delivery matters | `business-context.md` |
| Architectural judgment | Parse → voice → UI → assembly, with ADRs | `architecture.md`, `architecture/adr/` |
| Delivery discipline | Phased implementation with runnable `build/` | `implementation.md` |
| Validation rigor | Checks, commands, and proof paths | `validation.md`, `validation/P01-validation.md`, `validation/P02-validation.md`, `validation/P03-validation.md` |

## Intended audience

- Recruiters and non-technical readers (start with `business-context.md`)
- Hiring managers scanning for scope and judgment
- Peer engineers who will open `build/` and run the crate

## How to read this

1. `business-context.md`
2. `architecture.md` (plus `architecture/diagrams/` and `architecture/adr/`)
3. `implementation.md`
4. `validation.md`
5. `build/` for the Rust CLI, optional Dioxus **Knowledge Viewer**, Python TTS bridge, and samples

## System summary

- **Problem:** Markdown knowledge stays hard to reuse as audio, UI, or packaged study assets.
- **Scope:** **P01–P03** shipped in this folder (parse, stub-audio bridge, Dioxus viewer); **P04** (export + AIRI integration) has a committed [implementation plan](./executions/implementation/P04-implementation-plan.md) and is **not executed** yet.
- **Outcome:** Runnable **P01–P03** trail with ADRs, per-project plans, execution record, and validation — **P04** completes multimodal assembly per that plan.
- **Constraints:** Local compute, explicit cost/time posture; no paid API calls in scope for the core story.

## Repository artifacts

- `business-context.md` — problem, objectives, constraints
- `architecture.md` — overview, components, ADR index
- `architecture/diagrams/` — Mermaid sources (standard five)
- `architecture/adr/` — decision records
- `implementation.md` — phased delivery narrative
- `validation.md` — rollup; per-project files under `validation/`
- `build/` — Rust crate (P01 CLI + P03 `knowledge_viewer` behind `--features viewer`; P04 adds `export` binary per plan), `tts_inference.py` (P02); P04 adds `integration.py` when built, samples
- `executions/` — execution record, `implementation/` (per-project plans), `evidence/` (transcripts)

## Cross-system references

Part of the **agentic-systems-engineering** portfolio domain; series details live alongside this folder in the same repository layout.
