# Implementation plan — P02: Local audio narrations (VibeVoice)

| | |
|--|--|
| **System** | multimodal-knowledge-artifact-factory |
| **Last updated** | 2026-03 |
| **Series guide (filename only)** | `P02-Generate_Local_Audio_Narrations_using_VibeVoice.md` |
| **Depends on** | P01 — structured `H{n}:` / `P:` output from `build/` CLI (**PASS**) |

## Outcome

- **`build/tts_inference.py`** — Python bridge that loads **VibeVoice** (1.5B-class local TTS) per upstream install docs, runs on **CPU or GPU** as available, and fails loudly on OOM or missing deps.
- **Chunked inference** — Feeds **stripped** plain text derived from the P01 stream (no raw `##` / `**` artifacts in spoken input); chunks respect a safe size for the model context / RAM.
- **Audible proof** — One or more **`.wav`** files written under **`executions/evidence/`** (or a dedicated subfolder there) with **unique names** (chunk index or timestamp); transcripts of CLI runs stored as `.txt` alongside.

## Roadmap

| Phase | Focus |
| ----- | ----- |
| **1** | Python 3.11+ venv, VibeVoice deps, baseline model load (no OOM) |
| **2** | Read P01 output (pipe from `cargo run` or intermediate text file); chunk + strip for TTS |
| **3** | Synthesize per chunk → `.wav`; happy path + one edge case (oversized chunk or empty input) |
| **4** | Evidence, execution summary, `validation/P02-validation.md` → **PASS**, rollups |

## Phase 1 — Environment and model load

| Step | Complete when |
| ---- | ------------- |
| 1.1 | Python **3.11+**; `python --version` captured in [`../evidence/`](../evidence/) (e.g. `p02-python-version.txt`) |
| 1.2 | **venv** under `build/.venv` (or documented path); `requirements.txt` or `pyproject` lists VibeVoice-related deps you actually installed |
| 1.3 | **`tts_inference.py`** exists in [`build/`](../../build/) next to `Cargo.toml`; baseline code path **loads model weights** without crash (log in evidence) |
| 1.4 | Validation checkpoint: load succeeds without OOM on your machine (note RAM / device: CPU vs GPU in evidence) |

## Phase 2 — Text path from P01

| Step | Complete when |
| ---- | ------------- |
| 2.1 | Script accepts **structured lines** from P01 (stdin pipe from `cargo run --release -- <file.md>` **or** a saved `.txt` transcript of that stdout) |
| 2.2 | **Chunking** implemented (paragraph / line-boundary strategy per guide); logs show chunk boundaries |
| 2.3 | **Strip** markdown artifacts from spoken text (regex or reuse normalized tokens from `H:`/`P:` lines) |

## Phase 3 — Audio output

| Step | Complete when |
| ---- | ------------- |
| 3.1 | Each chunk produces a **`.wav`** with a **unique** filename (index or timestamp); files live under **`executions/evidence/`** (e.g. `p02-audio/` subfolder) |
| 3.2 | Sample rate / encoding matches what the inference stack expects (document choice in evidence; avoid guessing Hz) |
| 3.3 | At least one **negative or edge** case exercised (e.g. empty chunk, single very short input) and logged |

## Phase 4 — Closeout

| Item | Complete when |
| ---- | ------------- |
| Summary | [Execution record](../execution-record.md) updated for P02 |
| Evidence | Toolchain, install logs, run transcripts, optional dir listing of `.wav` under [`../evidence/`](../evidence/) |
| Validation | [P02 validation](../../validation/P02-validation.md) shows **PASS** |
| Rollups | Root [`implementation.md`](../../implementation.md) and [`validation.md`](../../validation.md) match P02 status |

## Done when

- [ ] Model load + chunking + `.wav` generation proven with evidence files.
- [ ] Per-project validation **PASS**.
- [ ] System rollups updated.

## Next

**P03** (Dioxus / interactive view) will consume text + audio artifacts; keep paths stable and documented under `executions/evidence/`.
