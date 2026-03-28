# Implementation plan — P02: Local audio narrations (VibeVoice)

| | |
|--|--|
| **System** | multimodal-knowledge-artifact-factory |
| **Last updated** | 2026-03 |
| **Series guide (filename only)** | `P02-Generate_Local_Audio_Narrations_using_VibeVoice.md` |
| **Depends on** | P01 — structured `H{n}:` / `P:` output from `build/` CLI (**PASS**) |

## Outcome

- **`build/tts_inference.py`** — Python bridge from P01 structured lines to **chunked** synthesis. **Shipped default:** `--backend stub` (stdlib **mono PCM WAV**, no PyTorch/HF) because [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) **removed/disabled public TTS-1.5B quick try** (see their README). **`--backend vibevoice`** is reserved and exits with an explicit message until a supported neural stack is integrated by an operator.
- **Chunked inference** — Feeds **stripped** plain text derived from the P01 stream (no raw `##` / `**` artifacts in spoken input); chunks respect `--max-chunk-chars` (default 400).
- **Audible proof** — One or more **`.wav`** files under **`executions/evidence/p02/audio/`** with **unique names** (`p02-chunk-NNNN.wav`); run transcripts under **`executions/evidence/p02/`** (`p02-pipeline-run.txt`, etc.).

## Roadmap

| Phase | Focus |
| ----- | ----- |
| **1** | Python 3.10+ recorded; `tts_inference.py`; **stub** baseline (optional venv for future neural deps) |
| **2** | Read P01 output (pipe from `cargo run` or intermediate text file); chunk + strip for TTS |
| **3** | Synthesize per chunk → `.wav`; happy path + one edge case (oversized chunk or empty input) |
| **4** | Evidence, execution summary, `validation/P02-validation.md` → **PASS**, rollups |

## Phase 1 — Environment and model load

| Step | Complete when |
| ---- | ------------- |
| 1.1 | Python **3.10+**; `python --version` captured in [`../evidence/p02/`](../evidence/p02/) (`p02-python-version.txt`) |
| 1.2 | **`requirements-p02.txt`** in [`build/`](../../build/) documents deps (**stub** needs none); optional `build/.venv` for future neural stacks |
| 1.3 | **`tts_inference.py`** in [`build/`](../../build/) next to `Cargo.toml`; **`--backend stub`** runs without extra packages |
| 1.4 | Neural VibeVoice-1.5B: **deferred** — upstream TTS path unavailable; stub proves pipeline (see validation notes) |

## Phase 2 — Text path from P01

| Step | Complete when |
| ---- | ------------- |
| 2.1 | Script accepts **structured lines** from P01 (stdin pipe from `cargo run --release -- <file.md>` **or** a saved `.txt` transcript of that stdout) |
| 2.2 | **Chunking** implemented (paragraph / line-boundary strategy per guide); logs show chunk boundaries |
| 2.3 | **Strip** markdown artifacts from spoken text (regex or reuse normalized tokens from `H:`/`P:` lines) |

## Phase 3 — Audio output

| Step | Complete when |
| ---- | ------------- |
| 3.1 | Each chunk produces a **`.wav`** with a **unique** filename (index or timestamp); files live under **`executions/evidence/`** (e.g. `p02/audio/` subfolder) |
| 3.2 | **Stub:** mono **16-bit PCM**, **22050 Hz** (documented in `build/README.md` and script) |
| 3.3 | At least one **negative or edge** case exercised (e.g. empty chunk, single very short input) and logged |

## Phase 4 — Closeout

| Item | Complete when |
| ---- | ------------- |
| Summary | [Execution record](../execution-record.md) updated for P02 |
| Evidence | Toolchain, install logs, run transcripts, optional dir listing of `.wav` under [`../evidence/`](../evidence/) |
| Validation | [P02 validation](../../validation/P02-validation.md) shows **PASS** |
| Rollups | Root [`implementation.md`](../../implementation.md) and [`validation.md`](../../validation.md) match P02 status |

## Done when

- [x] Stub pipeline + chunking + `.wav` generation proven with evidence files.
- [x] Per-project validation **PASS**.
- [x] System rollups updated.

## Next

**P03** — [P03-implementation-plan.md](./P03-implementation-plan.md): Dioxus interactive view consumes text + audio artifacts; keep paths stable under `executions/evidence/`.
