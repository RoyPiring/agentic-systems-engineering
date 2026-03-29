# Changelog — retrieval-backbone-for-multi-domain-knowledge-systems — 2026-03-29

## P02 — Citation-aware retrieval (LlamaIndex and Ollama)

**PR:** [#7](https://github.com/RoyPiring/agentic-systems-engineering/pull/7)  
**Type:** Engineering System — Incremental slice (same system as 2026-03-28 P01)

### P02 — Summary

Delivers **P02** for **retrieval-backbone-for-multi-domain-knowledge-systems**: **`build/query_pipeline.py`** (LlamaIndex + Ollama **`llama3.2`** + **`nomic-embed-text`**, Qdrant **`multi_domain_docs`**, citation-style QA prompt, **Answer** + **Citations** output). **`build/requirements.txt`** updated for **qdrant-client 1.17+** compatibility (**`llama-index-vector-stores-qdrant>=0.10`**). Evidence under **`executions/evidence/p02/`**; **`validation/P02-validation.md`** **PASS** (2026-03-29). Operator **[P02 user guide](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/user-guides/P02-user-guide.md)**; rollups (**`implementation.md`**, **`validation.md`**, **`README.md`**, **`business-context.md`**, **`architecture.md`**, **`execution-record.md`**, case-study **R1/R2** rows). **Multimodal** system: small alignment only — **operator runbooks** row in **`architecture.md`** and evidence-pairing table in **`validation.md`** (portfolio consistency).

### P02 — Projects in this PR

- P01 — unchanged from **PASS** on `main`; still prerequisite for P02
- P02 — Citation-aware retrieval — **shipped in this PR**
- P03 — not in this PR
- P04 — not in this PR

### P02 — Evidence

P02 **PASS** with transcripts under `engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/evidence/p02/` (`p02-query-run.txt`, `p02-ollama-list.txt`, `p02-curl-qdrant.txt`, `p02-qdrant-collection.txt`, `p02-pip-freeze.txt`, `p02-python-version.txt`) and rollup in `validation/P02-validation.md`.

---

## P03 — Live web content (Firecrawl)

**PR:** [#8](https://github.com/RoyPiring/agentic-systems-engineering/pull/8)  
**Type:** Engineering System — Incremental slice (same system folder as P01/P02 above)

### P03 — Summary

Delivers **P03**: **`build/ingest_web.py`** (firecrawl-py **v1**, scrape or bounded crawl → LlamaIndex **`Document`** with **`source_url`** → append Qdrant **`multi_domain_docs`**; **`nomic-embed-text`** parity with P01). **`--synthetic-evidence`** for validation when Firecrawl is unreachable. **`firecrawl-py`** in **`requirements.txt`**. Evidence **`executions/evidence/p03/`**; **`validation/P03-validation.md`** **PASS** (2026-03-29). Operator **[P03 user guide](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/user-guides/P03-user-guide.md)**; rollups and domain discovery (**`README.md`**, **`ROADMAP.md`**, **`engineering-systems/README.md`**) for slot **#1** through P03. **Multimodal** **`validation.md`**: related-system pointer to retrieval limitations.

### P03 — Projects in this PR

- P01 — prerequisite; **PASS** on `main`
- P02 — prerequisite; **PASS** on `main`
- P03 — Live web ingest — **shipped in this PR**
- P04 — not in this PR

### P03 — Evidence

P03 **PASS** with transcripts under `engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/evidence/p03/` (manifest **`evidence/p03/README.md`**) and rollup in `validation/P03-validation.md`. Committed files: **`p03-firecrawl-health.txt`**, **`p03-qdrant-collections.json`**, **`p03-qdrant-after-web.txt`**, **`p03-ingest-web-synthetic.txt`**, **`p03-ingest-web-dry-run.txt`**, **`p03-query-web-citation.txt`**, **`p03-pip-freeze.txt`**. Operator caveats in system **`validation.md`** (**Limitations → P03**). Optional live crawl: **`p03-ingest-web-run.txt`**.

**PR body:** [PR_BODY_P03.md](../../pull-requests/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/PR_BODY_P03.md) · **Pre-merge:** [PRE_MERGE_REVIEW_P03.md](../../code-review/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/PRE_MERGE_REVIEW_P03.md)
