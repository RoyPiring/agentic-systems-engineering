## Engineering System: retrieval-backbone-for-multi-domain-knowledge-systems

### What This PR Adds

**P03** — Live web content: **`build/ingest_web.py`** (Firecrawl **v1** API, scrape or bounded crawl, **`source_url`** / **`domain`** / **`ingest_kind: web`** metadata, Qdrant append with **`nomic-embed-text`**). **`--synthetic-evidence`** indexes one fixed markdown document with real URL metadata when Firecrawl is unavailable (same metadata contract as live crawl). **`build/README.md`** committed-tree table; **`firecrawl-py`** in **`requirements.txt`**. Evidence **`executions/evidence/p03/`** (manifest **[`README.md`](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/evidence/p03/README.md)**); **[P03 validation](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/validation/P03-validation.md)** **PASS**; **[P03 user guide](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/user-guides/P03-user-guide.md)**; **[P03 implementation plan](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/implementation/P03-implementation-plan.md)**. **`query_pipeline.py`** surfaces **`source_url:`** in Citations when node metadata includes it.

**Rollups:** **`README.md`**, **`implementation.md`**, **`validation.md`**, **`business-context.md`**, **`architecture.md`**, **`execution-record.md`**, **`user-guides/README.md`**, **`user-guides/SERIES-user-guide.md`**, **`validation/README.md`**, **`case-study/`** (R3). **Domain root:** **`README.md`**, **`ROADMAP.md`**, **`engineering-systems/README.md`** (slot **#1** = P01–P03 **PASS**).

**Docs-only (other system):** **Multimodal Knowledge Artifact Factory** — **`validation.md`** “Related portfolio system — Retrieval Backbone” pointer.

### Source

- Series (title): **Retrieval Backbone — Multi-Domain Knowledge**
- **Projects in this PR:** **P03** (+ **P01** / **P02** on `main`)

### Suggested branch / title

- **Branch:** `feature/retrieval-backbone-for-multi-domain-knowledge-systems-p03` → **`main`**
- **Title:** `feat(retrieval-backbone): P03 web ingest (Firecrawl) + validation PASS`

### Review Gate Checklist

- [x] **Code review (plan + quality):** [PRE_MERGE_REVIEW_P03.md](../../code-review/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/PRE_MERGE_REVIEW_P03.md) (against [codereview.md](../../code-review/codereview.md) + [P03 plan](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/implementation/P03-implementation-plan.md))
- [x] **Portfolio checklist:** [CHECKLIST.md](../../code-review/CHECKLIST.md)
- [x] All five required files present for **retrieval** system: README, business-context, architecture, implementation, validation
- [x] README supports 90-second orientation; **P03** outcome + text proof pointer updated
- [x] Tradeoffs / failure modes — **P03** (crawler, synthetic scope) in `architecture.md` + **`validation.md`** Limitations
- [x] Validation: **P01** + **P02** + **P03** **PASS**; **P04** **Pending**
- [x] No private-workspace paths in reader-facing portfolio text
- [x] Execution record — [`executions/execution-record.md`](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/execution-record.md) **P03** section
- [x] Evidence — [`executions/evidence/p03/`](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/evidence/p03/)
- [x] Changelog: second **`##` section** in [CHANGELOG.md](../../changelog/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/CHANGELOG.md) (same folder as P02 — **2026-03-29** slice) — *paste PR link into P03 section after open*
- [ ] **CI:** Documentation Quality workflow green on this PR
- [x] Issue templates present (existing `.github/ISSUE_TEMPLATE/`)

### Evidence Summary

- **Plan:** `engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/implementation/P03-implementation-plan.md`
- **Transcripts:** `executions/evidence/p03/` — **`p03-firecrawl-health.txt`**, **`p03-qdrant-collections.json`**, **`p03-qdrant-after-web.txt`**, **`p03-ingest-web-synthetic.txt`**, **`p03-ingest-web-dry-run.txt`**, **`p03-query-web-citation.txt`**, **`p03-pip-freeze.txt`** (manifest **[README.md](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/evidence/p03/README.md)**). Optional supplement: **`p03-ingest-web-run.txt`** (live Firecrawl).
- **Validation:** `validation/P03-validation.md` — **PASS** (2026-03-29; **V1–V7** ↔ files above — not **PASS (conditional)**); `validation.md` rollup updated

### Follow-ups (non-blocking)

- Capture **`p03-ingest-web-run.txt`** from live Firecrawl scrape/crawl (optional supplement)
- **P04** — separate PR (Ragas / packaging)
- Optional **`FEATURE_SYSTEMS.md`** at domain root if the portfolio adopts that index (Appendix K)

### `gh pr create` (example)

```bash
gh pr create --base main --head feature/retrieval-backbone-for-multi-domain-knowledge-systems-p03 \
  --title "feat(retrieval-backbone): P03 web ingest (Firecrawl) + validation PASS" \
  --body-file .github/pull-requests/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/PR_BODY_P03.md
```

After the PR exists, add **PR #** and link in the **P03** section of [CHANGELOG.md](../../changelog/2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/CHANGELOG.md) and under **2026-03-29** in the repo-root **`CHANGELOG.md`**.
