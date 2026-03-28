> ← [Multimodal Knowledge Artifact Factory](../README.md) · [All Systems](../../../engineering-systems/README.md) · [Home](../../../README.md)

# Build

Application code, scripts, configs, and infrastructure-as-code produced while executing the series (**P01–P04**).

Aligned with the series **Repository Packaging (RP)** manifest: runnable artifacts live here—not in the narrative docs at the engineering-system root.

## P01 — Markdown parse (`mkaf_md_parse`)

**Prerequisites:** Rust stable (`cargo`, `rustc`).

From this directory:

```bash
cargo build --release
cargo run --release
cargo run --release -- samples/complex-sample.md
```

- Default input path (no args): `samples/complex-sample.md` (relative to current working directory).
- Missing or unreadable files: message on stderr and exit code `1`.

## P02 — Local audio bridge (`tts_inference.py`)

**Prerequisites:** Python 3.10+ (stdlib only for `--backend stub`).

Microsoft’s **VibeVoice-TTS-1.5B** “quick try” is **disabled** in the upstream repo and **TTS inference code was removed** from [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) (see their README). This series step still implements the **parse → strip → chunk → WAV** pipeline; default **`stub`** writes short valid `.wav` files for reproducible proof. Operators who obtain a supported neural stack can extend the script’s backend hook.

From this directory:

```bash
# Save P01 stdout, then generate WAV chunks under executions/evidence/p02/audio/
cargo run --release -- samples/complex-sample.md > ../executions/evidence/p01/p01-stdout-for-p02.txt
python tts_inference.py --from-file ../executions/evidence/p01/p01-stdout-for-p02.txt

# Or pipe directly
cargo run --release -- samples/complex-sample.md | python tts_inference.py --stdin
```

- **Output:** `../executions/evidence/p02/audio/p02-chunk-0000.wav`, … (unique names per chunk).
- **Stub WAV format:** mono **16-bit PCM**, **22050 Hz** (valid files for players / downstream tests).
- **Optional deps:** `requirements-p02.txt` documents that stub mode needs no packages.

## P03 — Knowledge Viewer (`knowledge_viewer`, Dioxus 0.7.3 desktop)

**Prerequisites:** Same Rust stable toolchain; **Windows:** WebView2 (bundled with Edge). Build the UI with the **`viewer`** Cargo feature (optional dependency so the P01 CLI stays lightweight).

From this directory:

```bash
# Parser CLI (default binary)
cargo build --release
cargo run --release -- samples/complex-sample.md

# Desktop viewer (separate binary)
cargo build --release --features viewer --bin knowledge_viewer
cargo run --release --features viewer --bin knowledge_viewer

# Optional: load a different markdown file (path relative to build/ or absolute)
cargo run --release --features viewer --bin knowledge_viewer -- ../case-study/data/script.md
```

**Windows:** If the viewer build fails with MSVC **LNK1104** on `build_script_build-….exe`, try `cargo clean`, a shorter clone path, antivirus exclusion for the repo, or a short target directory for that shell only, for example `$env:CARGO_TARGET_DIR = "C:\t\mkaf-tgt"` (PowerShell) before `cargo build`.

- **Dioxus in `Cargo.toml`:** use `dioxus = { version = "0.7.3", optional = true, features = ["desktop"] }` — keep **default** crate features enabled so `macro` / `launch` / `html` / `signals` are available. Turning **`default-features = false`** on `dioxus` without adding those features breaks `#[component]`, `rsx!`, and `LaunchBuilder`.

- **Crate layout:** `src/lib.rs` — shared `parse_markdown_blocks` / `blocks_to_sections` / `list_p02_wavs_sorted`; `src/main.rs` — P01 CLI; `src/bin/knowledge_viewer.rs` — Dioxus app.
- **Data:** Default markdown is `samples/complex-sample.md`. **Optional first CLI argument** overrides that path (e.g. case-study `script.md`). Maps **Play Narration** to sorted files under `../executions/evidence/p02/audio/` — run P02 on the **same** markdown first so section order matches chunk order.
- **Evidence:** See [`../executions/evidence/p03/`](../executions/evidence/p03/) for commands and notes (`p03-*.txt`).

## P04 — Study exports (`export`) + AIRI bridge (`integration.py`)

**Prerequisites:** Same Rust stable toolchain; **Python 3.10+** for `integration.py`.

### Static exports (Rust)

From this directory:

```bash
cargo build --release --bin export
cargo run --release --bin export
# Optional: custom input and output directory (paths relative to cwd)
cargo run --release --bin export -- samples/complex-sample.md ../executions/evidence/p04/exports
```

- **Default input:** `samples/complex-sample.md`
- **Default output directory:** `../executions/evidence/p04/exports/`
- **Writes:** `flashcards.json` (array of `{ "term", "definition" }` per parsed section) and `quiz.md` (one question block per section; answers inside `<details>` for self-testing).

### Integration script (Python)

```bash
python integration.py --help
python integration.py --print-env
python integration.py --dry-run
# Launch AIRI when installed (binary on PATH or AIRI_EXECUTABLE set):
python integration.py
```

- Resolves **engineering-system root** as the parent of `build/`.
- Prints or exports **`MKAF_*`** paths: `MKAF_ROOT`, `MKAF_P02_AUDIO`, `MKAF_P04_EXPORTS`, `MKAF_VIEWER_SOURCE`, `MKAF_VIEWER_BINARY` (empty until `knowledge_viewer` release binary exists).
- Without AIRI on PATH, non–dry-run exits **2** with a clear message.

## Rules

- Prefer real, runnable content over empty placeholders.
- Do not commit secrets; use environment variables or secret stores documented in `architecture.md` / `validation.md`.
- Keep paths and run instructions discoverable from `implementation.md` and the relevant `executions/P0X-*` records.
