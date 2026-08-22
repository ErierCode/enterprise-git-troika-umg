# Enterprise Git Troika Lab

Repositorio de simulación para practicar un flujo Git empresarial con ramas, Pull Requests, Code Review, trazabilidad, Git Hooks y políticas.

## Inicio rápido

### Windows PowerShell
```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\setup-repo.ps1
```

### Git Bash / Linux / macOS
```bash
bash scripts/setup-repo.sh
```

Luego:
```bash
git status
git branch
git config core.hooksPath
```

## Flujo objetivo
Azure Boards → Feature Branch → Commit → Push → Pull Request → Code Review → Policies → Merge
