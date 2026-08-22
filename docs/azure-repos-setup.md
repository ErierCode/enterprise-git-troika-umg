# Configuración rápida en Azure Repos

1. Azure DevOps → Repos → Files.
2. Crear/seleccionar repositorio.
3. Copiar URL HTTPS.

Desde local:
```bash
git remote add origin <URL_DEL_REPO>
git push -u origin main
git push -u origin develop
```

## Policies
Azure DevOps → Project Settings → Repositories → Policies

Sobre `main`:
- Minimum number of reviewers: 1
- Check for linked work items
- Check for comment resolution
- Build validation (para el Módulo 5)
