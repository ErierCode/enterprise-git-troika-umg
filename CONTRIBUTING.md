# Guía de contribución

## Ramas
- `feature/<id>-descripcion`
- `bugfix/<id>-descripcion`
- `hotfix/<id>-descripcion`
- `docs/<id>-descripcion`

## Flujo
1. Actualizar `develop`.
2. Crear rama desde `develop`.
3. Hacer cambios pequeños.
4. Commit descriptivo.
5. Push.
6. Pull Request hacia `develop`.
7. Revisión.
8. Correcciones.
9. Merge.

## Commits
Formato:
`tipo: descripción AB#ID`

Tipos:
`feat`, `fix`, `docs`, `test`, `refactor`, `chore`

Ejemplo:
`feat: agregar registro de pacientes AB#25`

## Reglas
- No trabajar directamente sobre `main`.
- No subir `.env` ni secretos.
- Todo PR requiere revisión.
- Resolver comentarios antes del merge.
