# Despliega el backend en Hugging Face Spaces (gratis, sin tarjeta)

$ErrorActionPreference = "Stop"
$Root = $PSScriptRoot
$ApiUrl = "https://pierox123274-ejercicio2-api.hf.space/api/health"
$HfTokenFile = Join-Path $Root ".hf-token"

Write-Host "=== Despliegue Backend (Hugging Face) ===" -ForegroundColor Cyan

if (-not (Test-Path (Join-Path $Root ".venv"))) {
    python -m venv (Join-Path $Root ".venv")
    & (Join-Path $Root ".venv\Scripts\pip") install -r requirements.txt
}

if ($env:HF_TOKEN) {
    Write-Host "Token HF desde variable de entorno" -ForegroundColor Green
} elseif (Test-Path $HfTokenFile) {
    $env:HF_TOKEN = (Get-Content $HfTokenFile -Raw).Trim()
    Write-Host "Token HF cargado desde .hf-token" -ForegroundColor Green
} else {
    $hfCheck = & (Join-Path $Root ".venv\Scripts\python") -c "from huggingface_hub import HfApi; print(HfApi().whoami()['name'])" 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Falta login en Hugging Face:" -ForegroundColor Yellow
        Write-Host "  1. Crea token en https://huggingface.co/settings/tokens" -ForegroundColor White
        Write-Host "  2. Guardalo en: $HfTokenFile" -ForegroundColor White
        Write-Host "  3. O ejecuta: hf auth login" -ForegroundColor White
        exit 1
    }
    Write-Host "Usuario HF: $hfCheck" -ForegroundColor Green
}

Set-Location $Root
& (Join-Path $Root ".venv\Scripts\python") scripts\deploy_hf.py
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host ""
Write-Host "=== Backend desplegado ===" -ForegroundColor Green
Write-Host "  API: $ApiUrl" -ForegroundColor White
Write-Host "Espera 2-3 minutos a que Hugging Face construya el Space." -ForegroundColor Yellow
