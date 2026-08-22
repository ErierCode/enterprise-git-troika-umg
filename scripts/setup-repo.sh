#!/bin/sh
set -e
echo "== Inicializando laboratorio Enterprise Git =="

if [ ! -d ".git" ]; then
  git init -b main
fi

git config core.hooksPath .githooks
chmod +x .githooks/pre-commit .githooks/commit-msg 2>/dev/null || true
git add .

if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  git commit -m "chore: inicializar laboratorio enterprise"
fi

if ! git show-ref --verify --quiet refs/heads/develop; then
  git branch develop
fi

git branch
echo "HooksPath: $(git config core.hooksPath)"
