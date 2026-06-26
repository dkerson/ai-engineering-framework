# Workflow: Incidente

> Pipeline para incidentes em produção. Modo obrigatório: **Technical Council**.

## Trigger
`incident` — produção, urgente, downtime, incidente

## Modo

**Technical Council** — sempre. Incidente em produção é critério obrigatório de conselho.

## Pipeline

```
Risk Reviewer → Conselho (bug-hunter, backend, devops, deployment) → Decision Maker
    → Implementation Planner → [Fix] → Validator → Release Notes → Entrega
```

## Passos

| # | Skill | Ação |
|---|-------|------|
| 1 | risk-reviewer | Classificar risco (Crítico) |
| 2 | bug-hunter | Diagnóstico, causa raiz |
| 3 | backend/devops/deployment | Fix + rollback plan |
| 4 | decision-maker | Consolidar ação |
| 5 | implementation-planner | Plano de correção |
| 6 | [skill técnica] | Implementar fix |
| 7 | validator | Validar correção |
| 8 | release-notes | Comunicar correção |

## Regras

- Orchestrator mostra **somente decisão consolidada** ao usuário
- Prioridade: restaurar serviço → causa raiz → prevenção
- Working Context obrigatório

## Checklists
- `checklists/bug.md`
- `checklists/deploy.md`

## Rules
- `rules/hierarchical-orchestration.md`
- `rules/security.md`
