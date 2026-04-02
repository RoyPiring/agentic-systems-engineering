# Runbook — Local knowledge spine (case study)

**Before you start:** Open [../user-guides/README.md](../user-guides/README.md). Confirm **Python 3.12+**, **Docker** (Qdrant), and **Ollama** are available. Deep troubleshooting lives in per-phase guides ([SERIES](../user-guides/SERIES-user-guide.md), [P01](../user-guides/P01-user-guide.md)–[P04](../user-guides/P04-user-guide.md)) and [../build/README.md](../build/README.md).

**Paths:** This document assumes repo root is **agentic-systems-engineering**. Adjust if your clone layout differs.

```text
engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/
```

---

## Case study run — linear path (copy-paste)

**Goal:** Execute **P01 → P04** once, using committed **`build/data/sample.md`** and **synthetic web ingest** (no live Firecrawl required).

### 0. Services

**Qdrant** (operator-local; example):

```bash
docker run -d --name qdrant-p01 -p 6333:6333 -p 6334:6334 qdrant/qdrant:latest
# or: docker start qdrant-p01
```

**Ollama** — pull models used by the reference stack:

```bash
ollama pull nomic-embed-text
ollama pull llama3.2
ollama pull qwen3:8b
```

(`qwen3:8b` is the default **Ragas judge** via `OLLAMA_EVAL_LLM_MODEL`; see [P04 user guide](../user-guides/P04-user-guide.md).)

### 1. Python environment + P01 ingest

```bash
cd engineering-systems/retrieval-backbone-for-multi-domain-knowledge-systems/build
python -m venv venv
# Windows: venv\Scripts\activate
# Unix:    source venv/bin/activate
pip install -r requirements.txt
python ingest.py
```

**Windows long paths / ingest DLL issues:** use [../build/README.md](../build/README.md) P01 section (`run_ingest_windows.ps1`, `charset-normalizer` note).

### 2. P03 web slice (synthetic — no Firecrawl)

```bash
python ingest_web.py --synthetic-evidence
```

(For live Firecrawl instead, see [P03 user guide](../user-guides/P03-user-guide.md) and [../build/README.md](../build/README.md) P03 section.)

### 3. P02 manual queries (spot-check citations)

```bash
python query_pipeline.py --query "What vector database does the indexed documentation say is used locally in this series?"
python query_pipeline.py --query "According to the indexed documentation about Python environment variables, what does PEP 405 describe?"
```

Expect **Answer** + **Citations**; web rows may show **`source_url:`**.

### 4. P04 — Ragas + packaged consumer

```bash
python ragas_eval.py --mode baseline
python ragas_eval.py --mode batch --sleep-between 2
python consumer_demo.py
python consumer_demo.py --query "What does the corpus say about PDF ingestion?"
```

**If Qdrant is down** (CI / blocked Docker): `python ragas_eval.py --mode batch --synthetic-rows` (fixed rows + Ragas only). **Inspect dataset without judge calls:** `python ragas_eval.py --mode batch --synthetic-rows --dry-dataset`

---

## Evidence capture (portfolio)

When closing a validation pass, save transcripts under **`../executions/evidence/p04/`** (and P01–P03 as needed). Filenames and checks are defined in [../validation/P04-validation.md](../validation/P04-validation.md) and [../user-guides/P04-user-guide.md](../user-guides/P04-user-guide.md). Example mapping:

| Transcript | Typical source |
| ---------- | -------------- |
| `p04-docker-qdrant.txt` | `docker ps` / start transcript |
| `p04-curl-qdrant-collection.txt` | `curl` to `GET /collections/multi_domain_docs` |
| `p04-ollama-list.txt` | `ollama list` |
| `p04-python-version.txt` | `python --version` |
| `p04-pip-freeze.txt` | `pip freeze` |
| `p04-ragas-baseline.txt` | stdout from `ragas_eval.py --mode baseline` |
| `p04-ragas-batch.txt` | stdout from `ragas_eval.py --mode batch …` |
| `p04-consumer-demo.txt` | stdout from `consumer_demo.py` |

Update **`../executions/execution-record.md`** with a short **`## P04`** summary when you record a full run.

**Automation:** [tools/run_case_study.ps1](./tools/run_case_study.ps1) / [tools/run_case_study.sh](./tools/run_case_study.sh) run the same Python sequence (assumes Qdrant + Ollama already up and venv active).

---

## Phase references (detail on demand)

End-to-end order matches [../user-guides/SERIES-user-guide.md](../user-guides/SERIES-user-guide.md).

### 0. Data

- [data/README.md](./data/README.md) — corpus location and optional PDF.

### 1. P01 — Ingest and index

[../user-guides/P01-user-guide.md](../user-guides/P01-user-guide.md) · [../executions/implementation/P01-implementation-plan.md](../executions/implementation/P01-implementation-plan.md)

**Expected:** Vectors in **`multi_domain_docs`**; evidence [../executions/evidence/p01/](../executions/evidence/p01/).

### 2. P02 — Citation-aware retrieval

[../user-guides/P02-user-guide.md](../user-guides/P02-user-guide.md) · [../executions/implementation/P02-implementation-plan.md](../executions/implementation/P02-implementation-plan.md)

**Expected:** [../executions/evidence/p02/](../executions/evidence/p02/).

### 3. P03 — Live web (Firecrawl or synthetic)

[../user-guides/P03-user-guide.md](../user-guides/P03-user-guide.md) · [../executions/implementation/P03-implementation-plan.md](../executions/implementation/P03-implementation-plan.md)

**Expected:** [../executions/evidence/p03/](../executions/evidence/p03/).

### 4. P04 — Ragas and packaging

[../user-guides/P04-user-guide.md](../user-guides/P04-user-guide.md) · [../executions/implementation/P04-implementation-plan.md](../executions/implementation/P04-implementation-plan.md)

**Expected:** [../executions/evidence/p04/](../executions/evidence/p04/) · [../validation/P04-validation.md](../validation/P04-validation.md) **PASS**.

---

## Verification

| ID | Requirement | Evidence (file / observation) |
| --- | --- | --- |
| R1 | Indexed corpus | **PASS** — [validation/P01-validation.md](../validation/P01-validation.md); e.g. [p01-ingest-run.txt](../executions/evidence/p01/p01-ingest-run.txt), [p01-qdrant-collection.txt](../executions/evidence/p01/p01-qdrant-collection.txt) |
| R2 | Cited answers | **PASS** — [validation/P02-validation.md](../validation/P02-validation.md); e.g. [p02-query-run.txt](../executions/evidence/p02/p02-query-run.txt) |
| R3 | Web slice (if in scope) | **PASS** — [validation/P03-validation.md](../validation/P03-validation.md); [p03-query-web-citation.txt](../executions/evidence/p03/p03-query-web-citation.txt); manifest [README](../executions/evidence/p03/README.md); caveats [validation.md](../validation.md#limitations) |
| R4 | Measured quality | **PASS** — [validation/P04-validation.md](../validation/P04-validation.md); e.g. [p04-ragas-batch.txt](../executions/evidence/p04/p04-ragas-batch.txt), [p04-consumer-demo.txt](../executions/evidence/p04/p04-consumer-demo.txt) |
