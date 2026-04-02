#!/usr/bin/env bash
# Linear case-study sequence from build/ (P01 -> P03 synthetic -> P02 queries -> P04).
# Prerequisite: Qdrant + Ollama up, venv activated or python on PATH.
# Does not write executions/evidence/ — capture transcripts when validating.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SYSTEM_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
BUILD="$SYSTEM_ROOT/build"

cd "$BUILD"

step() {
  echo "==> $1"
  shift
  "$@"
}

step "P01 ingest" python ingest.py
step "P03 synthetic web ingest" python ingest_web.py --synthetic-evidence
step "P02 query (markdown)" python query_pipeline.py --query "What vector database does the indexed documentation say is used locally in this series?"
step "P02 query (web)" python query_pipeline.py --query "According to the indexed documentation about Python environment variables, what does PEP 405 describe?"
step "P04 Ragas baseline" python ragas_eval.py --mode baseline
step "P04 Ragas batch" python ragas_eval.py --mode batch --sleep-between 2
step "P04 consumer demo" python consumer_demo.py
step "P04 consumer (PDF topic)" python consumer_demo.py --query "What does the corpus say about PDF ingestion?"

echo "Case study script finished OK."
