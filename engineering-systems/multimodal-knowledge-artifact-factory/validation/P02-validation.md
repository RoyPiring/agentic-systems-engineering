# P02 validation — Local audio narrations (pipeline)

| | |
|--|--|
| **Plan** | [../executions/implementation/P02-implementation-plan.md](../executions/implementation/P02-implementation-plan.md) |
| **Result** | **PASS** (evidence under [../executions/evidence/](../executions/evidence/)) |

## Notes

Microsoft’s public **VibeVoice-TTS** quick path is **not** guaranteed from the main [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) repo (see their README). This validation proves **structured parser output → strip → chunk → `.wav`** using the repo’s default **standard-library** WAV path; neural TTS is an optional follow-on when your stack supports it.

## Checks

| # | Criterion | Pass when |
|---|-----------|-----------|
| 1 | Python | `python --version` captured; **3.10+** |
| 2 | Baseline | `tts_inference.py` runs with **no** undeclared pip deps for default path |
| 3 | Handoff | `H{n}:` / `P:` lines from parser reach chunker |
| 4 | Chunking | Multiple chunks; boundaries visible in log |
| 5 | Audio | Playable `.wav` per chunk; unique names |
| 6 | Edge | Empty structured input → warning, no WAV |
| 7 | Evidence | Transcripts + listing under `executions/evidence/` |

## How to run

From `build/`:

```bash
cargo run --release -- samples/complex-sample.md 1> ../executions/evidence/p01-stdout-for-p02.txt
python tts_inference.py --from-file ../executions/evidence/p01-stdout-for-p02.txt
```

(On PowerShell, `1>` keeps parser **stdout** only in the file; or pipe: `cargo run --release -- samples/complex-sample.md | python tts_inference.py --stdin`.)

## Results

| Check | Expected | Actual |
| ----- | -------- | ------ |
| Python | 3.10+ recorded | **PASS** — [`p02-python-version.txt`](../executions/evidence/p02-python-version.txt) |
| Baseline | Default path without extra installs | **PASS** — [`requirements-p02.txt`](../build/requirements-p02.txt), script in [`build/tts_inference.py`](../build/tts_inference.py) |
| Handoff + chunk | Chunks from P1 stdout | **PASS** — [`p01-stdout-for-p02.txt`](../executions/evidence/p01-stdout-for-p02.txt), [`p02-pipeline-run.txt`](../executions/evidence/p02-pipeline-run.txt) |
| Audio | WAV files on disk | **PASS** — [`p02-audio/`](../executions/evidence/p02-audio/), [`p02-audio-listing.txt`](../executions/evidence/p02-audio-listing.txt) |
| Edge | Empty input handled | **PASS** — [`p02-edge-empty-stderr.txt`](../executions/evidence/p02-edge-empty-stderr.txt) |

## Delivery

| | |
|--|--|
| **PR** | https://github.com/RoyPiring/agentic-systems-engineering/pull/3 |
| **Merge commit** | (short SHA on `main` after merge) |
