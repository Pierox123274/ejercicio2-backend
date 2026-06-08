$ErrorActionPreference = "Stop"
$Root = $PSScriptRoot

Write-Host "=== Instalacion Backend ===" -ForegroundColor Cyan
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Instala Python 3.11+ desde https://python.org" -ForegroundColor Red
    exit 1
}

Set-Location $Root
if (-not (Test-Path ".venv")) { python -m venv .venv }
.\.venv\Scripts\pip install -r requirements.txt
.\.venv\Scripts\python scripts\test_connection.py
Write-Host "Listo. Ejecuta: uvicorn main:app --reload --port 8001" -ForegroundColor Green
