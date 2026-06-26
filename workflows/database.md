# Workflow: Database

> Schema, queries e migrations. Modo padrão: **Review**. Council se migration em produção.

## Trigger
`database` — migration, schema, query, SQL

## Modo sugerido

| Condição | Modo |
|----------|------|
| Query/índice pontual | Standard |
| Migration, schema change | **Review** |
| Migration em produção | **Technical Council** |

## Pipeline (Review)

```
Context Builder → Database → Backend → Critic → Validator → Entrega
```

## Skills
`context-builder`, `database`, `backend`, `critic`, `validator`, `risk-reviewer`

## Checklist
- `checklists/database.md`
- `checklists/review.md`

## Rules
- `rules/hierarchical-orchestration.md`
- `rules/database.md`
