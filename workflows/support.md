# Workflow: Suporte

> Triagem e resolução. Modo padrão: **Standard**. Council se incidente.

## Trigger
`support` — suporte, ticket, triagem

## Modo

| Condição | Modo |
|----------|------|
| Dúvida/triagem | Standard |
| Incidente produção | **Council** → ver `incident.md` |

## Pipeline (Standard)

```
Support → Bug Hunter* → [resolução] → Entrega
```

## Skills
`support`, `bug-hunter`

## Rules
- `rules/hierarchical-orchestration.md`
