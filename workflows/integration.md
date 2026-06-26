# Workflow: Integração

> Webhooks e sistemas terceiros. Modo padrão: **Review**. Council se integração crítica.

## Trigger
`integration` — integrar, webhook, terceiro

## Modo sugerido

| Condição | Modo |
|----------|------|
| Integração simples | Review |
| Pagamento, ERP, API sensível | **Technical Council** |

## Pipeline (Review)

```
Context Builder → Software Architect → API → Backend → Critic → Validator → Entrega
```

## Pipeline (Council)

```
Conselho → Decision Maker → Implementation Planner → API → Backend → Validator → Entrega
```

## Skills
`software-architect`, `api`, `backend`, `risk-reviewer`, `critic`, `validator`

## Checklist
- `checklists/api.md`
- `checklists/review.md`

## Rules
- `rules/hierarchical-orchestration.md`
- `rules/security.md`
