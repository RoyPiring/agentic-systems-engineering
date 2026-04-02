## Engineering System: retrieval-backbone-for-multi-domain-knowledge-systems

### What This PR Adds

**P04** — Quality measurement and service packaging: **`build/ragas_eval.py`** (baseline + batch Ragas, **context_precision** + **answer_relevancy**, explicit Ollama / LangChain-Ollama injection — no required OpenAI default); **`build/retrieval_service.py`** (**`RetrievalBackboneService`** — documented query → answer + citations, env/injected config); **`build/consumer_demo.py`** (smoke using public API only); **`query_pipeline.py`** delegates to the service. Evidence **`executions/evidence/p04/`**; **[P04 validation](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/validation/P04-validation.md)** **PASS**; **[P04 user guide](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/user-guides/P04-user-guide.md)**; **[P04 implementation plan](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/implementation/P04-implementation-plan.md)**. **[ADR-004](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/architecture/adr/ADR-004-ragas-for-retrieval-quality-measurement.md)** for Ragas scope.

**Case study (E2E):** **Local knowledge spine** — [`case-study/README.md`](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/case-study/README.md), [`SCENARIO.md`](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/case-study/SCENARIO.md), [`RUNBOOK.md`](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/case-study/RUNBOOK.md), [`REQUIREMENTS.md`](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/case-study/REQUIREMENTS.md), [`data/queries.md`](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/case-study/data/queries.md), [`diagrams/e2e-flow.mmd`](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/case-study/diagrams/e2e-flow.mmd), optional [`tools/`](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/case-study/tools/).

**CI:** [`.github/workflows/retrieval-backbone-ragas-dry.yml`](../../workflows/retrieval-backbone-ragas-dry.yml) — `python ragas_eval.py --mode batch --synthetic-rows --dry-dataset` on PR/push when retrieval **`build/`** changes.

**Rollups:** **`README.md`**, **`implementation.md`**, **`validation.md`**, **`business-context.md`**, **`architecture.md`**, **`execution-record.md`**, **`user-guides/`**, **`case-study/`** (R1–R4). **Domain root:** **`README.md`**, **`ROADMAP.md`**, **`engineering-systems/README.md`**, **`OPERATING_REQUIREMENTS.md`**, **`.gitignore`** (slot **#1** = **P01–P04** **PASS**).

**Docs alignment (portfolio):** Multimodal **P03/P04** plans + **P03** validation — text-transcript evidence only (no UI-capture requirement). Historical **`.github`** PR/review markdown — removed optional screenshot bullets.

### Source

- Series (title): **Retrieval Backbone — Multi-Domain Knowledge**
- **Projects in this PR:** **P04** + case-study closeout (+ **P01**–**P03** already on `main` or carried on branch base)

### Suggested branch / title

- **Branch:** `feature/retrieval-backbone-p04-ragas-quality-service` → **`main`**
- **Title:** `feat(retrieval-backbone): P04 Ragas eval + service API + case study E2E`

### Review Gate Checklist

- [x] **Code review (plan + quality):** [PRE_MERGE_REVIEW_P04.md](../../code-review/2026-04-01-retrieval-backbone-for-multi-domain-knowledge-systems/PRE_MERGE_REVIEW_P04.md) (against [codereview.md](../../code-review/codereview.md) + [P04 plan](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/implementation/P04-implementation-plan.md))
- [x] **Portfolio checklist:** [CHECKLIST.md](../../code-review/CHECKLIST.md)
- [x] All five required files present for **retrieval** system: README, business-context, architecture, implementation, validation
- [x] README supports 90-second orientation; **P04** outcome + **case-study** pointers
- [x] Validation: **P01**–**P04** **PASS**
- [x] No private-workspace paths in reader-facing portfolio text
- [x] Execution record — [`executions/execution-record.md`](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/execution-record.md) **P04** + case study subsection
- [x] Evidence — [`executions/evidence/p04/`](../../../engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/evidence/p04/)
- [ ] **Changelog:** [CHANGELOG.md](../../changelog/2026-04-01-retrieval-backbone-for-multi-domain-knowledge-systems/CHANGELOG.md) — paste **PR #** after open; repo-root [CHANGELOG.md](../../../CHANGELOG.md)
- [ ] **CI:** Documentation Quality + **Retrieval Backbone — Ragas dry dataset** green on this PR
- [x] Issue templates present (existing `.github/ISSUE_TEMPLATE/`)

### Evidence Summary

- **Plan:** `engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/executions/implementation/P04-implementation-plan.md`
- **Transcripts:** `executions/evidence/p04/` — per **`README.md`** in that folder (**`p04-ragas-baseline.txt`**, **`p04-ragas-batch.txt`**, **`p04-consumer-demo.txt`**, toolchain captures)
- **Validation:** `validation/P04-validation.md` — **PASS**

### Follow-ups (non-blocking)

- Optional: expand **Ragas dry** workflow `paths:` if you want the workflow to run on **`case-study/**`** edits only (currently **`build/`** + workflow file)

### `gh pr create` (example)

```bash
gh pr create --base main --head feature/retrieval-backbone-p04-ragas-quality-service \
  --title "feat(retrieval-backbone): P04 Ragas eval + service API + case study E2E" \
  --body-file .github/pull-requests/2026-04-01-retrieval-backbone-for-multi-domain-knowledge-systems/PR_BODY_P04.md
```

**PR:** *(paste PR # after open — e.g. `**PR [#N](https://github.com/RoyPiring/agentic-systems-engineering/pull/N)**`)*
