# Workflow: Performance

> Investigação e otimização. Modo padrão: **Review**. Council se performance crítica em produção.

## Trigger
`performance` — lento, timeout, profiling, otimizar

## Modo sugerido

| Condição | Modo |
|----------|------|
| Otimização pontual | Review |
| Gargalo em produção | **Technical Council** |

## Pipeline (Review)

```
Performance → Database* → Backend* → Critic → Validator → Entrega
```

## Pipeline (Council)

```
Conselho (performance, database, backend, devops) → Decision Maker
    → Implementation Planner → [Impl] → Validator → Entrega
```

## Passos (Review)

| # | Skill | Ação |
|---|-------|------|
| 1 | performance | Medir baseline, identificar gargalo |
| 2 | database | Queries, índices, N+1 (se aplicável) |
| 3 | backend | Lógica, cache, async (se aplicável) |
| 4 | critic | Validar que resolve causa, não sintoma |
| 5 | validator | Validar melhoria mensurável |

## Checklists
- `checklists/performance.md`
- `checklists/review.md`

## Rules
- `rules/hierarchical-orchestration.md`
- `rules/performance.md`
