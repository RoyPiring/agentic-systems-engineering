# ADR-003: Unstructured for heterogeneous document ingest

## Status

Accepted

## Context

**P01** must normalize **markdown, PDF, and HTML** (and similar office-derived exports) into a consistent chunk stream for embedding. Hand-rolled parsers per MIME type do not scale across the series and invite silent format regressions.

## Decision

Use **Unstructured** (library + documented partition strategies) as the default path from raw files to structured elements suitable for chunking and metadata attachment before **Qdrant** upsert.

## Alternatives considered

- **Manual per-type parsers** — Maximum control but high maintenance and uneven coverage across PDF encodings and HTML edge cases.
- **Vendor-only “smart” loaders** tied to a single cloud API — Conflicts with local-first and cost posture.
- **LlamaIndex readers only, no Unstructured** — Viable for some formats; rejected as the **canonical** ingest story here because the series explicitly centers Unstructured + Qdrant in **P01**.

## Consequences

**Positive:** One ingestion vocabulary across document types; easier to reproduce in validation.

**Negative / tradeoffs:** Heavy dependency footprint; version upgrades can change element boundaries—mitigate with pinned deps and golden samples.

**Follow-ups:** Record partition strategy and package versions in `executions/execution-record.md` and `validation/P01-validation.md` when P01 runs.
