# ADR-002: Parse markdown with pulldown-cmark in Rust

## Status

Accepted

## Context

The pipeline ingests **structured markdown** and must turn it into an internal representation suitable for downstream steps (TTS scripts, UI data, export formats). The stack is Rust-first (Dioxus app, local binaries), so the parser should be safe, fast, and easy to wire into the same crate graph.

## Decision

Use **pulldown-cmark** (0.11 per series spec) as the CommonMark parser and AST/event source for the ingestion stage.

## Alternatives considered

- **Hand-rolled regex / line splitters** — Fast to prototype but brittle for nested lists, code fences, and links; high long-term defect rate.
- **Python BeautifulSoup / markdown libs** — Rich ecosystem but splits the core pipeline across two runtimes and complicates a single reproducible `cargo` story.
- **comrak or other Rust parsers** — Viable; pulldown-cmark is widely used, well maintained, and matches the locked series tooling list.

## Consequences

**Positive:** Single-language core, streaming-friendly events, good CommonMark coverage.  
**Negative / tradeoffs:** Custom extensions (if needed later) may require extra preprocessing.  
**Follow-ups:** Define the internal struct model (post-parse) in `implementation.md` when P01 lands in `build/`.
