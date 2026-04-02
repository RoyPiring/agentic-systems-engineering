#Requires -Version 5.1
<#
.SYNOPSIS
  Runs the linear case-study sequence from build/ (P01 ingest -> P03 synthetic web -> P02 spot queries -> P04 Ragas + consumer).
.DESCRIPTION
  Prerequisite: Qdrant reachable (default localhost:6333), Ollama running with models pulled, Python venv activated OR python on PATH.
  Does not write to executions/evidence/ — capture transcripts separately when closing validation.
#>
$ErrorActionPreference = "Stop"
$SystemRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$Build = Join-Path $SystemRoot "build"
if (-not (Test-Path $Build)) { throw "build/ not found: $Build" }
Set-Location $Build

function Invoke-Step {
    param([string]$Label, [scriptblock]$Action)
    Write-Host "==> $Label" -ForegroundColor Cyan
    & $Action
    if ($LASTEXITCODE -ne 0) { throw "Step failed: $Label (exit $LASTEXITCODE)" }
}

Invoke-Step "P01 ingest" { python ingest.py }
Invoke-Step "P03 synthetic web ingest" { python ingest_web.py --synthetic-evidence }
Invoke-Step "P02 query (markdown)" {
    python query_pipeline.py --query "What vector database does the indexed documentation say is used locally in this series?"
}
Invoke-Step "P02 query (web)" {
    python query_pipeline.py --query "According to the indexed documentation about Python environment variables, what does PEP 405 describe?"
}
Invoke-Step "P04 Ragas baseline" { python ragas_eval.py --mode baseline }
Invoke-Step "P04 Ragas batch" { python ragas_eval.py --mode batch --sleep-between 2 }
Invoke-Step "P04 consumer demo" { python consumer_demo.py }
Invoke-Step "P04 consumer (PDF topic)" { python consumer_demo.py --query "What does the corpus say about PDF ingestion?" }

Write-Host "Case study script finished OK." -ForegroundColor Green
