> ← [All Systems](../../engineering-systems/README.md) · [Home](../../README.md)

# Multimodal Knowledge Artifact Factory

**Problem:** Structured research and specs stay stuck as flat markdown — no audio, no interactive navigation, no packaged study assets.

**Approach:** Local Rust + Python pipeline: parse → stub audio → Dioxus desktop viewer → study exports — zero recurring cloud cost.

**Outcome:** End-to-end local pipeline validated across 4 project phases with per-phase evidence, expected-vs-actual tables, and negative case coverage.

---

## What This Proves

| Signal | What a reviewer learns | Evidence |
| ------ | ---------------------- | -------- |
| Problem framing | Why multimodal, local delivery matters | [business-context.md](./business-context.md) |
| Architectural judgment | Parse → voice → UI → assembly, with ADRs | [architecture.md](./architecture.md), [architecture/adr/](./architecture/adr/) |
| Delivery discipline | Phased implementation with runnable `build/` | [implementation.md](./implementation.md) |
| Validation rigor | Checks, commands, and proof paths | [validation.md](./validation.md), [validation/P01-validation.md](./validation/P01-validation.md) … [validation/P04-validation.md](./validation/P04-validation.md) |

---

## Knowledge Viewer (P03)

*Screenshot will be added after next local build. To see the viewer now: follow [user-guides/P03-user-guide.md](./user-guides/P03-user-guide.md).*

<!-- When captured, replace the line above with:
![Dioxus Knowledge Viewer — parsed sections with audio mapping](./executions/evidence/p03/p03-viewer-screenshot.png)
-->

---

## Intended Audience

- **Recruiters and non-technical readers** — start with [business-context.md](./business-context.md)
- **Hiring managers** scanning for scope and judgment — [business-context.md](./business-context.md) → [architecture.md](./architecture.md)
- **Operators** who want to run it — start with [**user-guides/README.md**](./user-guides/README.md) ("Start here"), then [SERIES-user-guide.md](./user-guides/SERIES-user-guide.md)
- **Peer engineers** reviewing depth — [architecture.md](./architecture.md) → [validation.md](./validation.md) → [executions/evidence/](./executions/evidence/)

## How to read this

1. **To run the system:** [user-guides/README.md](./user-guides/README.md) → per-phase guides or [user-guides/SERIES-user-guide.md](./user-guides/SERIES-user-guide.md) end-to-end
2. [business-context.md](./business-context.md)
3. [architecture.md](./architecture.md) (plus [architecture/diagrams/](./architecture/diagrams/) and [architecture/adr/](./architecture/adr/))
4. [implementation.md](./implementation.md)
5. [validation.md](./validation.md)
6. [build/](./build/) — Rust crate, Python TTS bridge, samples

---

## System Summary

- **Problem:** Markdown knowledge stays hard to reuse as audio, UI, or packaged study assets.
- **Scope:** P01–P04 implemented: parse, stub-audio bridge, Dioxus viewer, `export` study assets + `integration.py` AIRI bridge. AIRI desktop launch is operator-dependent; validation is **PASS (conditional)** until AIRI is proven locally.
- **Outcome:** End-to-end local pipeline through static exports and path handoff; see [validation/P04-validation.md](./validation/P04-validation.md).
- **Constraints:** Local compute, explicit cost/time posture; no paid API calls in scope for the core story.

## Repository Artifacts

- [business-context.md](./business-context.md) — problem, objectives, constraints
- [architecture.md](./architecture.md) — overview, components, ADR index
- [architecture/diagrams/](./architecture/diagrams/) — Mermaid sources (standard five)
- [architecture/adr/](./architecture/adr/) — decision records (4 ADRs)
- [implementation.md](./implementation.md) — phased delivery narrative
- [validation.md](./validation.md) — rollup; per-project files under [validation/](./validation/)
- [build/](./build/) — Rust crate (P01 CLI, P03 `knowledge_viewer`, P04 `export` binary), `tts_inference.py` (P02), `integration.py` (P04), samples
- [executions/](./executions/) — execution record, per-project plans under `implementation/`, evidence under `evidence/p01/`…`p04/`
- [user-guides/](./user-guides/) — operator runbooks: P01–P04 phase guides and `SERIES-user-guide.md`
- [case-study/](./case-study/) — end-to-end scenario with requirements, runbook, and verification checklist

---

## Related Systems

*Links to related systems in this repository will be added as more systems are published.*
