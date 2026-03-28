# User guide — P02: Local audio chunks (stub WAV)

## What you get

**Python** turns the structured text from P01 into short **`.wav`** sound files. By default this repo uses a **stub** backend (no extra `pip` packages). Run this before P03 if you want **Play Narration** to find real audio files.

## Getting ready (before you run)

1. **Finish “Getting ready” in [P01](./P01-user-guide.md)** — same system root and **`build/`** folder.
2. **Python 3.10+** — run `python --version` or `py -3 --version` (Windows). Install Python if the command is missing.
3. You will either **pipe** P01 output into this script or **save** P01 output to a file first (the commands below show both).

## Prerequisites (short list)

- **Python 3.10+**
- P01-style text: lines starting with `H` (headings) or `P` (paragraphs), from a pipe or a saved file.

## How to run

From **`build/`**:

### Option A — saved P01 stdout

```bash
cargo run --release -- samples/complex-sample.md > ../executions/evidence/p01/p01-stdout-for-p02.txt
python tts_inference.py --from-file ../executions/evidence/p01/p01-stdout-for-p02.txt
```

### Option B — pipe

```bash
cargo run --release -- samples/complex-sample.md | python tts_inference.py --stdin
```

**Optional:** `--output-dir` to change where WAVs go (default is `../executions/evidence/p02/audio/` relative to `build/`).

## Success vs failure

- **Success:** Messages list chunks; files like `p02-chunk-0000.wav` appear under `executions/evidence/p02/audio/`.
- **Empty input** (no `H`/`P` lines): warning on stderr; **no** WAV files.

## Outputs

- Mono **16-bit PCM**, **22050 Hz** WAV files suitable for players and P03.

## Real spoken audio (optional — not P02 stub)

The **`stub`** backend only makes **placeholder tones** (beeps), not speech. If you want **actual narration** of markdown text:

| Approach | Notes |
| -------- | ----- |
| **Case study — Edge TTS** | From **`build/`**: `pip install edge-tts`, then `python ../case-study/tools/generate_edge_narration.py --one-file` — writes **`case-study/data/audio/script-narration-full.mp3`** for [`../case-study/data/script.md`](../case-study/data/script.md). No API key; Microsoft-hosted voice. See [`../case-study/data/audio/README.md`](../case-study/data/audio/README.md). |
| **OpenAI TTS** | Needs **`OPENAI_API_KEY`**; use the Codex **`text_to_speech.py`** flow (see your speech skill / OpenAI Audio API). Chunks must be ≤ 4096 characters per request. |
| **Neural in-repo** | **`vibevoice`** in `tts_inference.py` is **not** wired; see [`../build/README.md`](../build/README.md). |

Those MP3 paths are **separate** from **`executions/evidence/p02/audio/`** — the shipped P01→P02→P03 pipeline still expects **stub (or future) WAV chunks** there unless you integrate a new backend into `tts_inference.py`.

## Next step

Open [P03 — Knowledge Viewer](./P03-user-guide.md) (viewer expects WAVs under `executions/evidence/p02/audio/` when using the default sample).
