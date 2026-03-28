# User guide — Full series (P01 → P04)

This page is the **full path** through the **Multimodal Knowledge Artifact Factory** in this repo. You can run one phase at a time, or follow the order below to run everything.

## 0. From zero to your first command

1. **Get the repository** — clone **agentic-systems-engineering** (or your fork), then open:  
   **`engineering-systems/multimodal-knowledge-artifact-factory/`**  
   That is the **system root** (you should see `build/`, `executions/`, `validation/`).
2. **Install Rust and Python** — see the table in [`README.md`](./README.md) (“Start here”). Confirm `cargo --version` and `python --version` (or `py -3 --version` on Windows).
3. **Open a terminal in `build/`** — from the system root: `cd build`. Keep this folder as your working directory for the commands below unless a phase guide says otherwise.
4. **Smallest first success** — run P01 only (see [P01 — Parse markdown](./P01-user-guide.md)): `cargo build --release` then `cargo run --release -- samples/complex-sample.md`. You should see structured lines on the screen. After that, follow **Recommended order** below (section **2**) for the rest of the pipeline.

## 1. Layout (where things live)

- **`build/`** — run all Rust and Python commands here unless a guide says otherwise.
- **`executions/evidence/`** — per-project folders **`p01/`** … **`p04/`**: transcripts, **`p02/audio/`** stub WAVs, **`p04/exports/`** flashcards + quiz (safe to delete and regenerate; paths are defaults in code).
- **`user-guides/`** — how to run the system (this folder).
- **`case-study/`** — E2E scenario with **`data/script.md`**, optional **`artifacts/`** copies of exports.

## 2. Recommended order

| Step | Do this | See |
| ---- | -------- | --- |
| 1 | Parse markdown → structured stdout | [P01](./P01-user-guide.md) |
| 2 | Structured text → `.wav` chunks | [P02](./P02-user-guide.md) |
| 3 | (Optional) Desktop viewer | [P03](./P03-user-guide.md) |
| 4 | Flashcards + quiz export | [P04](./P04-user-guide.md) (export section) |
| 5 | Path map / AIRI | [P04](./P04-user-guide.md) (integration section) |

## 3. One-shot command chain (from `build/`)

After a clean build of binaries you need:

```bash
# P01 → P02 (pipe)
cargo run --release -- samples/complex-sample.md | python tts_inference.py --stdin

# P04 export (reuses sample on disk via default path)
cargo run --release --bin export

# Integration smoke (no AIRI required for --dry-run)
python integration.py --dry-run
```

Add P03 only when you need the UI:

```bash
cargo build --release --features viewer --bin knowledge_viewer
cargo run --release --features viewer --bin knowledge_viewer
# Optional: same markdown as your last P01→P02 run, e.g. case-study script:
# cargo run --release --features viewer --bin knowledge_viewer -- ../case-study/data/script.md
```

## 4. Dependencies between phases

- **P02** needs P01-shaped text (pipe or file).
- **P03** is nicer if **P02** WAVs exist under `executions/evidence/p02/audio/`.
- **P04 export** only needs the markdown file (default `samples/complex-sample.md`); it does not require P02/P03 to have run.
- **P04 integration** expects folders to exist; it reads **P02** and **P04 export** paths plus optional **P03** binary.

## 5. Troubleshooting

- **Rust link errors (LNK1104)** on Windows: short `CARGO_TARGET_DIR` or see [`../build/README.md`](../build/README.md).
- **AIRI missing:** use `--dry-run` for path checks; install AIRI and set **`AIRI_EXECUTABLE`** or PATH for a real launch.

## 6. Deeper reading

- Build reference: [`../build/README.md`](../build/README.md)
- Validation / proof: [`../validation.md`](../validation.md)
- Case study (E2E with `script.md`): [`../case-study/RUNBOOK.md`](../case-study/RUNBOOK.md) — optional **spoken MP3** for that script: [`../case-study/data/audio/README.md`](../case-study/data/audio/README.md) (Edge TTS; P02 stub in §1 is not speech)
