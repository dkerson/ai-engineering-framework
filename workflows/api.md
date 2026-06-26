# Workflow: API

> Contratos e endpoints. Modo padrão: **Standard**. Review se mudança de contrato.

## Trigger
`api` — endpoint, REST, GraphQL, contrato

## Modo sugerido

| Condição | Modo |
|----------|------|
| Endpoint simples | Standard |
| Novo contrato, breaking change | Review |
| API crítica (pagamento, auth) | **Technical Council** |

## Pipeline (Standard)

```
API → Backend → QA → Entrega
```

## Pipeline (Review)

```
Context Builder → API → Backend → Critic → Validator → Entrega
```

## Skills
`api`, `backend`, `qa`, `critic`, `validator`

## Checklist
- `checklists/api.md`
- `checklists/review.md`

## Rules
- `rules/hierarchical-orchestration.md`
- `rules/api.md`
