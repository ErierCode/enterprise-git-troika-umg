$ErrorActionPreference = "Continue"
Write-Host "== Inicializando laboratorio Enterprise Git =="

if (-not (Test-Path ".git")) {
    git init -b main
}

git config core.hooksPath .githooks
git add .

git rev-parse --verify HEAD *> $null
if ($LASTEXITCODE -ne 0) {
    git commit -m "chore: inicializar laboratorio enterprise"
}

git show-ref --verify --quiet refs/heads/develop
if ($LASTEXITCODE -ne 0) {
    git branch develop
}

git branch
Write-Host "HooksPath: $(git config core.hooksPath)"
