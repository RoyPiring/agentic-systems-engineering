# Build

Application code, scripts, configs, and infrastructure-as-code produced while executing the series (P01–P04).

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
# Save P01 stdout, then generate WAV chunks under executions/evidence/p02-audio/
cargo run --release -- samples/complex-sample.md > ../executions/evidence/p01-stdout-for-p02.txt
python tts_inference.py --from-file ../executions/evidence/p01-stdout-for-p02.txt

# Or pipe directly
cargo run --release -- samples/complex-sample.md | python tts_inference.py --stdin
```

- **Output:** `../executions/evidence/p02-audio/p02-chunk-0000.wav`, … (unique names per chunk).
- **Stub WAV format:** mono **16-bit PCM**, **22050 Hz** (valid files for players / downstream tests).
- **Optional deps:** `requirements-p02.txt` documents that stub mode needs no packages.

## Rules

- Prefer real, runnable content over empty placeholders.
- Do not commit secrets; use environment variables or secret stores documented in `architecture.md` / `validation.md`.
- Keep paths and run instructions discoverable from `implementation.md` and the relevant `executions/P0X-*` records.
