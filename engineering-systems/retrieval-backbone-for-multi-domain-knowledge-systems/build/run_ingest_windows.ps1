#Requires -Version 5.1
<#
.SYNOPSIS
  Run P01 ingest on Windows when the repo path is long enough to hit MAX_PATH DLL load failures
  (spacy / charset-normalizer). Maps this directory to R: via subst, runs venv Python, then removes the mapping.

.DESCRIPTION
  From repo root, paths can exceed Windows limits; native extensions then fail with
  "The filename or extension is too long." Running with a short drive letter avoids that.

.PARAMETER RemainingArguments
  Passed through to ingest.py (e.g. --collection other).
#>
$ErrorActionPreference = "Stop"
$buildRoot = $PSScriptRoot
if (-not (Test-Path -LiteralPath (Join-Path $buildRoot "venv\Scripts\python.exe"))) {
    Write-Error "venv not found under $buildRoot. Create it: python -m venv venv; .\venv\Scripts\pip install -r requirements.txt"
}
subst.exe R: /d 2>$null
subst.exe R: $buildRoot
if ($LASTEXITCODE -ne 0) { Write-Error "subst failed; try another free drive letter or enable Windows long paths." }
try {
    $py = "R:\venv\Scripts\python.exe"
    $script = "R:\ingest.py"
    & $py $script @args
    exit $LASTEXITCODE
} finally {
    subst.exe R: /d 2>$null
}
