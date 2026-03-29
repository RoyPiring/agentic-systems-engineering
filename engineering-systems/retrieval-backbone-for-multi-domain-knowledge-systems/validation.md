> ← [Retrieval Backbone — Multi-Domain Knowledge](./README.md) · [All Systems](../README.md) · [Home](../../README.md)

# Validation

Roll-up of proof for this engineering system. Each per-project file moves from **Pending** to **PASS** (or **PASS (conditional)**) when work is accepted.

| Project | Plan | Validation | Result |
| --- | --- | --- | --- |
| P01 | [executions/implementation/P01-implementation-plan.md](./executions/implementation/P01-implementation-plan.md) | [validation/P01-validation.md](./validation/P01-validation.md) | **PASS** |
| P02 | [executions/implementation/P02-implementation-plan.md](./executions/implementation/P02-implementation-plan.md) | [validation/P02-validation.md](./validation/P02-validation.md) | **PASS** |
| P03 | [executions/implementation/P03-implementation-plan.md](./executions/implementation/P03-implementation-plan.md) | [validation/P03-validation.md](./validation/P03-validation.md) | **PASS** |
| P04 | [executions/implementation/P04-implementation-plan.md](./executions/implementation/P04-implementation-plan.md) | [validation/P04-validation.md](./validation/P04-validation.md) | **Pending** |

## Operator runbooks (evidence pairing)

Each phase that records **`executions/evidence/p0X/`** transcripts should follow the matching runbook so commands and filenames stay consistent with [implementation plans](./executions/implementation/) and validation.

| Project | User guide |
| --- | --- |
| P01 | [user-guides/P01-user-guide.md](./user-guides/P01-user-guide.md) |
| P02 | [user-guides/P02-user-guide.md](./user-guides/P02-user-guide.md) |
| P03 | [user-guides/P03-user-guide.md](./user-guides/P03-user-guide.md) |
| P04 | *when published* |

## Validation summary

**P01:** [P01 validation](./validation/P01-validation.md) **PASS** with transcripts under [`executions/evidence/p01/`](./executions/evidence/p01/). **P02:** [P02 validation](./validation/P02-validation.md) **PASS** with transcripts under [`executions/evidence/p02/`](./executions/evidence/p02/) and [P02 user guide](./user-guides/P02-user-guide.md). **P03:** [P03 validation](./validation/P03-validation.md) **PASS** — [`executions/evidence/p03/`](./executions/evidence/p03/) (artifacts listed in [`evidence/p03/README.md`](./executions/evidence/p03/README.md); live Firecrawl ingest transcript optional). **P04** not started. Success criteria: [business-context.md](./business-context.md); boundaries: [architecture.md](./architecture.md).

## Expected vs actual

| Check | Expected | Actual | Δ |
| --- | --- | --- | --- |
| P01 index | Chunks + vectors in Qdrant | Collection `multi_domain_docs`, 2 points (sample.md); dim 768 | **PASS** |
| P02 answers | Citations map to stored nodes | **PASS** — [`p02-query-run.txt`](./executions/evidence/p02/p02-query-run.txt); collection [`p02-qdrant-collection.txt`](./executions/evidence/p02/p02-qdrant-collection.txt) | — |
| P03 web | Web-shaped content indexed; citations show **`source_url`** | **PASS** — [`p03-query-web-citation.txt`](./executions/evidence/p03/p03-query-web-citation.txt) + full set in [`evidence/p03/README.md`](./executions/evidence/p03/README.md) | Optional **`p03-ingest-web-run.txt`** with live Firecrawl |
| P04 quality | Ragas scores recorded | — | Pending |

## Evidence artifacts

Transcripts and logs live under [`executions/evidence/p01/`](./executions/evidence/p01/) … **`p04/`**. Capture them using the steps and suggested filenames in **`user-guides/P0X-user-guide.md`** for each phase (portfolio standard—see [Multimodal Knowledge Artifact Factory](../multimodal-knowledge-artifact-factory/validation.md) for a fully closed example).

## Negative testing

| Failure Scenario | What Was Tested | Result | Recovery |
| --- | --- | --- | --- |
| P01 empty data / bad Qdrant | Scripted checks | Documented in `executions/evidence/p01/p01-negative-edge.txt` | **PASS** |

## Security validation

Local trust boundaries and URL/crawl policy are documented in [architecture.md](./architecture.md) and will be exercised per phase.

## Cost validation

| Cost Driver | Constraint | Observed | Variance |
| --- | --- | --- | --- |
| Third-party APIs | $0 recurring default | P01–P02: local Ollama + Qdrant only (no required OpenAI in script path) | On track |

## Reproducibility assessment

**Partial** — `build/requirements.txt` + `p01-pip-freeze.txt` + `p02-pip-freeze.txt` + `p03-pip-freeze.txt` captured; Windows long-path + Python 3.13 noted in P01/P02 validation. Re-run on 3.12/Linux for full cross-platform parity if required.

## Limitations

**P01**–**P03** closed with evidence; **P04** remains planned until executed.

### P03 operator environment (no separate evidence sidecar)

- **Firecrawl:** **`p03-firecrawl-health.txt`** records the health probe (ok or failure). **`p03-ingest-web-run.txt`** is optional when you run a live scrape/crawl (registry auth may block `ghcr.io/mendableai/firecrawl` on some networks).
- **Synthetic path:** **`ingest_web.py --synthetic-evidence`** indexes one document with **`source_url`** metadata when Firecrawl is unavailable — same Qdrant append + citation contract as the live path; not a separate script.
- **Windows / P01 file ingest:** Long clone paths can break spaCy/Unstructured DLL loads; use **`run_ingest_windows.ps1`** or OS long-path support — see [P01 validation](./validation/P01-validation.md) and **`build/README.md`**.
