# Business Context

## Problem Statement

Structured knowledge (research packets, specs) usually stays flat markdown: no audio layer, no
interactive navigation, and no packaged multimodal study artifacts. That caps reach, reuse, and
accessibility. This system proves a **local pipeline** that turns those sources into narrations,
interactive views, and study-ready exports—without recurring cloud spend.

## Why This Matters

- **Learners and readers** get audio and interactive formats instead of walls of text.
- **Builders** keep data and inference on-machine: privacy-friendly and reproducible for a portfolio
  story.
- **Reviewers** see an end-to-end pattern (ingest → structure → voice → UI → assembly) comparable
  in spirit to consumer knowledge tools, executed under explicit cost and scope locks.

## Objectives

- Ingest structured markdown and parse it into a usable internal representation (P01).
- Generate **local** audio narrations with VibeVoice (P02).
- Deliver **interactive knowledge views** with Dioxus (P03).
- Assemble **multimodal study artifacts** via AIRI integration (P04).
- Maintain **$0 recurring** cost: no paid APIs in the core path; one-time model footprint only.

## Success Criteria

| Metric | Target | Validation Method |
| --- | --- | --- |
| Parse fidelity | Parsed structure matches markdown intent; errors surfaced with context | P01 execution record + sample files |
| Audio output | Narration files produced locally without cloud TTS APIs | P02 execution record + artifacts |
| Interactive UI | Navigable Dioxus views over parsed content | P03 execution record + build/run proof |
| Multimodal assembly | AIRI consumes exports; companion workflow demonstrable | P04 execution record |
| Cost lock | **$0** recurring; only local compute + known one-time ~3GB model pull | Document in `validation.md` |
| Time box | ~**60 minutes** effort guidance per project (series design point) | Execution notes honesty |

## Constraints

- **Budget:** **$0 recurring**; no paid API calls in scope. One-time VibeVoice model download (~**3GB**)
  and local RAM/GPU expectations apply.
- **Time:** Series sized for **beginner** depth; **four** projects, ~**60 minutes** each as authored in
  the source spec.
- **Organizational:** Portfolio / lab context—no production SLA, multi-tenant product, or org-wide
  rollout claims.
- **Technical:** **Rust** toolchain, **Dioxus 0.7.3**, **pulldown-cmark 0.11**, local **VibeVoice**
  and **AIRI** desktop; development on a **local workstation** (Cursor/VS Code-class IDE).

## Scope

### In Scope

- Local pipeline execution from markdown through structured parsing.
- VibeVoice text-to-speech for local narrations.
- Dioxus-based interactive knowledge views.
- AIRI self-hosted companion for multimodal assembly workflows.
- Static study exports (e.g. flashcard JSON, quiz markdown) where the series defines them.

### Out Of Scope

- Cloud deployment and production CDN delivery.
- Video encoding/editing pipelines.
- Live end-user authentication or multi-tenant SaaS operation.
- Paid third-party inference or TTS APIs in the **core** path.

### Non-Goals

- Replacing full NotebookLM or any vendor product feature-for-feature.
- Guaranteeing minimum latency or scale for arbitrary hardware.
- Certifying security/compliance beyond “local operator machine” assumptions.

## Stakeholders

| Stakeholder | Need | Why It Matters |
| --- | --- | --- |
| Operator / builder | Repeatable local runbook | Can reproduce and extend the pipeline |
| Learner audience | Accessible formats | Audio + UI improve consumption of dense docs |
| Technical reviewer | Clear boundaries and evidence | Judgment visible without hand-wavy demos |

## Risks

- **Hardware floor:** TTS or UI builds may OOM or run slowly on under-spec machines; mitigate with
  documented minimums and graceful errors.
- **Model and dependency drift:** Pin versions in execution records and validation.
- **Integration fragility:** AIRI/version coupling; mitigate with explicit version matrix and
  failure notes in P04.
- **Scope creep:** Cloud or paid APIs tempting for speed—explicitly excluded to preserve the cost
  story.

## Related docs

- [System README](./README.md)
- [Architecture](./architecture.md)
- [Validation](./validation.md)
