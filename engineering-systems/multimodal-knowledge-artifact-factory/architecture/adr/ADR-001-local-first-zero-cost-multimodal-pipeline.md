# ADR-001: Run the multimodal pipeline locally with zero recurring API cost

## Status

Accepted

## Context

The series targets a **$0 recurring cost** lock: structured markdown (research packets, specs) should become audio, interactive views, and study exports without paid cloud APIs or hosted inference. Operators have a local workstation with enough RAM/GPU for a ~3GB TTS model download (VibeVoice) and can run desktop tooling (AIRI).

## Decision

Keep **all inference and assembly on the local machine** — no mandatory network calls for core pipeline steps. Treat cloud delivery, CDN, and auth as explicitly out of scope for this portfolio system.

## Alternatives considered

- **Hosted TTS / LLM APIs** — Lowest operational burden but violates cost lock and makes reproducibility depend on vendor keys and quotas.
- **Hybrid (local parse + cloud voice)** — Reduces local GPU needs but reintroduces recurring cost and data egress considerations.
- **Full cloud NotebookLM-style SaaS** — Matches consumer UX but is out of scope and not reproducible on a reviewer’s laptop.

## Consequences

**Positive:** Predictable spend, privacy-friendly, portfolio story is “runs on your machine.”  
**Negative / tradeoffs:** Hardware floor for TTS; no built-in global scale or multi-tenant isolation.  
**Follow-ups:** Document minimum hardware and cold-start (model download) in `validation.md` and execution records.
