# ADR-004: Use VibeVoice for local TTS and AIRI for multimodal assembly

## Status

Accepted

## Context

The series must produce **local audio narrations** and **multimodal study artifacts** (e.g. packaged outputs learners can use offline). P00 locks **VibeVoice** (ASR / 1.5B TTS path) and **AIRI** as a self-hosted desktop companion for assembly and orchestration of multimodal assets.

## Decision

- **P02:** Generate narrations with **VibeVoice** on the local machine (accepting one-time model weight download and GPU/RAM requirements).
- **P04:** Integrate **AIRI** for multimodal study artifact assembly and handoff of outputs (alongside static exports such as flashcard JSON and quiz markdown where specified in project guides).

## Alternatives considered

- **System `say`/OS TTS** — Zero ML footprint but poor control over voice quality and timing for “study-grade” narration.
- **Cloud-only speech APIs** — Rejected under ADR-001 cost and locality constraints.
- **Custom FFmpeg-only video pipeline** — Out of scope per P00 (no video encoding/editing focus).

## Consequences

**Positive:** Demonstrates realistic local ML + desktop integration patterns aligned with NotebookLM-style outcomes.  
**Negative / tradeoffs:** Model download size; environment sensitivity (CUDA/ROCm/CPU fallback) must be validated honestly in `validation.md`.  
**Follow-ups:** Version-pin inference scripts in `build/` and record observed latency and resource use per execution record.
