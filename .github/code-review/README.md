# Code review artifacts

| File | Purpose |
| ---- | -------- |
| **[codereview.md](./codereview.md)** | **code-reviewer** agent: plan alignment, code quality, architecture, severity-rated findings. |
| **[CHECKLIST.md](./CHECKLIST.md)** | Portfolio gates: public voice, breadcrumbs, evidence layout, ADR honesty. |

## Per-slice folders: `YYYY-MM-DD-<engineering-system-folder>/`

Same folder name as [pull-requests/](../pull-requests/) and [changelog/](../changelog/) for that **date + series**.

- **`README.md`** — hub linking PR body file(s), changelog, and the canonical briefs above.
- **`PRE_MERGE_REVIEW.md`** — optional; add when you record a pre-merge review (one file per slice, or split by project if needed).

**Master index:** [SLICE_LAYOUT.md](../SLICE_LAYOUT.md)

**Example — two PRs same day / same system:** [2026-03-29 retrieval hub](./2026-03-29-retrieval-backbone-for-multi-domain-knowledge-systems/README.md) (P02 [PR #7](https://github.com/RoyPiring/agentic-systems-engineering/pull/7) + P03 follow-on; P03 validation **PASS**).

**Example — P04 same system, new calendar slice:** [2026-04-01 retrieval hub](./2026-04-01-retrieval-backbone-for-multi-domain-knowledge-systems/README.md) (Ragas + packaged service; P04 validation **PASS**).

**Automation:** [.github/workflows/ai-pr-review.yml](../workflows/ai-pr-review.yml) only posts an LLM stub **comment** when `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` is set. There is **no** keyless script that executes this checklist — reviewers use the markdown briefs locally or in the IDE. [.github/workflows/docs-lint.yml](../workflows/docs-lint.yml) enforces markdown + links + required system files.
