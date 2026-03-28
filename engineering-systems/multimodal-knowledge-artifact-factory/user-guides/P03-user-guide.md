# User guide — P03: Knowledge Viewer (Dioxus desktop)

## What you get

A **desktop window** titled **Knowledge Viewer** (title includes the loaded file name). It loads **`samples/complex-sample.md`** by default, or a **markdown path you pass as the first argument**, shows sections, and can **play narration** if P02 already created `.wav` files in the expected folder for **that same source**.

## Getting ready (before you run)

1. **Same setup as P01** — Rust installed; terminal **current folder** = **`build/`** (see [P01](./P01-user-guide.md)).
2. **Windows:** **WebView2** is usually installed with Edge. If the app fails to open a window, install or update Edge / WebView2.
3. **Strongly recommended:** run [P02](./P02-user-guide.md) first so `../executions/evidence/p02/audio/` contains files like `p02-chunk-0000.wav`. The viewer still opens without them, but narration will not match real audio.

## Prerequisites (short list)

- **Rust** (same as P01).
- **Windows:** **WebView2** (typical with Edge).
- **P02** completed (recommended) so WAV paths exist.

## How to run

From **`build/`**:

```bash
cargo build --release --features viewer --bin knowledge_viewer
cargo run --release --features viewer --bin knowledge_viewer
```

**Optional — load another file** (path relative to **`build/`** or absolute). Use this for the **[case-study](../case-study/RUNBOOK.md)** after P01→P02 on **`script.md`**:

```bash
cargo run --release --features viewer --bin knowledge_viewer -- ../case-study/data/script.md
```

Keep **current working directory** = `build/` so default `samples/complex-sample.md` and `../executions/evidence/p02/audio/` resolve correctly.

## Windows: build fails with LNK1104

Long paths under `build/target/` sometimes trigger **LNK1104**. Mitigations:

- Set a short target dir for that shell, e.g. PowerShell: `$env:CARGO_TARGET_DIR = "C:\t\mkaf-tgt"` then rebuild.
- Or `cargo clean`, shorter clone path, antivirus exclusion for the repo.

See [`../build/README.md`](../build/README.md) for the full note.

## Success vs failure

- **Success:** Window opens; sections visible; narration control logs or plays without freezing the UI.
- **Failure:** Compile errors (check Dioxus **0.7.3** + `desktop` feature); runtime WebView issues (install/update WebView2).

## Next step

[Study exports + AIRI](./P04-user-guide.md) for packaging assets; the viewer binary path is also passed via `integration.py` when present.
