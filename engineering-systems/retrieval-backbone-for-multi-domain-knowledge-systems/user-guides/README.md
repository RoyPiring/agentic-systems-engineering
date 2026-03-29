> ← [Retrieval Backbone — Multi-Domain Knowledge](../README.md) · [All Systems](../../README.md) · [Home](../../../README.md)

# User guides

## Start here

1. **First runnable phase:** [P01 — Ingest and index](./P01-user-guide.md) (Qdrant + Ollama + `build/ingest.py`).
2. **Second phase:** [P02 — Citation-aware query](./P02-user-guide.md) (`build/query_pipeline.py`) after P01 is **PASS**.
3. Read the [system README](../README.md) and [business context](../business-context.md).
4. Implementation detail: [P01 plan](../executions/implementation/P01-implementation-plan.md) · [P02 plan](../executions/implementation/P02-implementation-plan.md) · [P03 plan](../executions/implementation/P03-implementation-plan.md) · Toolchain layout: [`build/README.md`](../build/README.md).

**P04** runbook lands when that phase is validated.

**Evidence pairing:** Each phase that records transcripts under **`executions/evidence/p0X/`** should follow the matching **`P0X-user-guide.md`** so filenames and commands stay consistent with [validation](../validation.md).

## Index

| Phase | Guide | Status |
| --- | --- | --- |
| P01 | [P01-user-guide.md](./P01-user-guide.md) | **Ready** (validated path documented) |
| P02 | [P02-user-guide.md](./P02-user-guide.md) | **Ready** ([validation](../validation/P02-validation.md) **PASS**) |
| P03 | [P03-user-guide.md](./P03-user-guide.md) | **Ready** ([validation](../validation/P03-validation.md) **PASS**; evidence [`executions/evidence/p03/`](../executions/evidence/p03/)) |
| P04 | `P04-user-guide.md` | Not created yet |
| Series | [SERIES-user-guide.md](./SERIES-user-guide.md) | In progress — P01–P02 linked |
