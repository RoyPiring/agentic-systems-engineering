# Implementation

How this system is phased from a working **parse path** through media and UI. Per-project plans live in [`executions/implementation/`](./executions/implementation/) (`P0X-implementation-plan.md`); run evidence lives in [`executions/evidence/`](./executions/evidence/). **Operators** should start with [`user-guides/README.md`](./user-guides/README.md) and [`user-guides/SERIES-user-guide.md`](./user-guides/SERIES-user-guide.md). This page is the rolling **system** view.

## Strategy

Work moves **P01 → P04**: Markdown → structured text → audio/UI → assembly. Each phase stays testable on its own.

## Phases

### P01 — Foundation

| | |
|--|--|
| **Plan** | [executions/implementation/P01-implementation-plan.md](./executions/implementation/P01-implementation-plan.md) |
| **Goal** | Rust binary under `build/` turns `.md` into structured lines (`H{n}:`, `P:`) for downstream use |
| **Inputs** | CLI path or default `samples/complex-sample.md` (cwd = `build/`) |
| **Output** | Structured stdout; stderr + exit `1` on read errors |

**Artifacts:** `build/Cargo.toml`, `build/src/main.rs` (CLI), `build/src/lib.rs` (shared parse for P03), `build/samples/complex-sample.md`, [`build/README.md`](./build/README.md).

**Status:** **Executed** — [`validation/P01-validation.md`](./validation/P01-validation.md) **PASS**.

### P02 — Core build

| | |
|--|--|
| **Plan** | [executions/implementation/P02-implementation-plan.md](./executions/implementation/P02-implementation-plan.md) |
| **Goal** | Python **`build/tts_inference.py`** implements P01 → strip → chunk → **`.wav`** (default **`stub`** backend; neural VibeVoice-TTS deferred per upstream repo status) |
| **Inputs** | P01 CLI stdout (pipe) or saved structured transcript (`--from-file`) |
| **Output** | Playable `.wav` under `executions/evidence/p02/audio/` + transcripts |

**Status:** **Executed** — [`validation/P02-validation.md`](./validation/P02-validation.md) **PASS**; evidence under [`executions/evidence/`](./executions/evidence/).

**Depends on:** P01 **PASS** — [`validation/P01-validation.md`](./validation/P01-validation.md).

### P03 — Interactive views

| | |
|--|--|
| **Plan** | [executions/implementation/P03-implementation-plan.md](./executions/implementation/P03-implementation-plan.md) |
| **Goal** | **Dioxus 0.7.3** desktop **Knowledge Viewer**: render parsed markdown sections (default `samples/complex-sample.md`, **optional CLI path** e.g. case-study `script.md`); per-section control targeting P02 **`.wav`** files under `executions/evidence/p02/audio/` |
| **Inputs** | Same markdown sample contract as P01; P02 audio artifacts on disk |
| **Output** | Runnable desktop UI; evidence under `executions/evidence/`; [validation/P03-validation.md](./validation/P03-validation.md) **PASS** |

**Status:** **Executed** — [`validation/P03-validation.md`](./validation/P03-validation.md) **PASS**; evidence under [`executions/evidence/`](./executions/evidence/) (`p03-*.txt`).

**Depends on:** P01 **PASS** — [validation/P01-validation.md](./validation/P01-validation.md); P02 **PASS** — [validation/P02-validation.md](./validation/P02-validation.md).

### P04 — Multimodal assembly (AIRI)

| | |
|--|--|
| **Plan** | [executions/implementation/P04-implementation-plan.md](./executions/implementation/P04-implementation-plan.md) |
| **Goal** | Rust **`export`** binary → **`flashcards.json`** + **`quiz.md`**; **`build/integration.py`** maps paths and launches **AIRI** when installed |
| **Inputs** | P01 sample markdown; P02 WAVs under `executions/evidence/p02/audio/`; P03 viewer source/binary paths for handoff |
| **Output** | `executions/evidence/p04/exports/`; integration script; transcripts `p04-*`; [validation/P04-validation.md](./validation/P04-validation.md) **PASS (conditional)** |
| **Status** | **Executed** — export + integration + E2E slice evidenced; AIRI desktop launch **not** observed (see validation) |

End-to-end proof will live under [`executions/evidence/`](./executions/evidence/); roll-up in [`validation.md`](./validation.md).

## How to run (P01)

1. Install Rust.  
2. `cd build`  
3. `cargo build --release`  
4. `cargo run --release -- samples/complex-sample.md`  

## How to run (P02)

1. Python **3.10+** on `PATH`.  
2. From `build/`: save P01 stdout or pipe — see [build/README.md](./build/README.md).  
3. `python tts_inference.py --from-file ../executions/evidence/p01/p01-stdout-for-p02.txt` (or `--stdin`).  

## How to run (P03)

1. From `build/`: `cargo run --release --features viewer --bin knowledge_viewer` (after `cargo build --release --features viewer --bin knowledge_viewer` if needed).  
2. Requires **WebView2** on Windows; keep cwd as `build/` so `samples/` and `../executions/evidence/p02/audio/` resolve.  
3. Details: [build/README.md](./build/README.md).  

## How to run (P04)

1. From `build/`: `cargo build --release --bin export` then `cargo run --release --bin export` (writes under `../executions/evidence/p04/exports/`).  
2. `python integration.py --dry-run` to verify paths; install **AIRI** and set **`AIRI_EXECUTABLE`** or PATH, then `python integration.py` to launch.  
3. Details: [build/README.md](./build/README.md) § P04.

## Decisions

| Topic | Choice |
| ----- | ------ |
| Crate location | `build/`, not repo root |
| Parser | `pulldown-cmark` **0.11** (ADR-002); shared in `src/lib.rs` for CLI + viewer |
| Default sample | `samples/complex-sample.md` |
| P03 UI | Dioxus **0.7.3** desktop; binary `knowledge_viewer`, feature `viewer` (ADR-003) |
| P02 audio default | **stub** WAV (stdlib Python); neural VibeVoice deferred per upstream |
| P04 export | **`serde`** / **`serde_json`**; binary `export`; outputs under `executions/evidence/p04/exports/` |
| P04 integration | **`build/integration.py`**; **`MKAF_*`** env vars for AIRI |

## Reproduce

Use stable Rust; run commands from `build/`. Per-phase evidence and commands: [`executions/execution-record.md`](./executions/execution-record.md). Status roll-up: [`validation.md`](./validation.md) and `validation/P01-validation.md` … `P04-validation.md`.
