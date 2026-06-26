# Workflow: Financeiro

> Faturamento e billing. Modo padrão: **Review**. Council se pagamentos.

## Trigger
`finance` — faturamento, custo, billing

## Modo

| Condição | Modo |
|----------|------|
| Relatório/análise | Standard |
| Pagamentos, billing | Review/**Council** |

## Pipeline (Review)

```
Finance → Risk Reviewer → Functional Spec → Validator → Entrega
```

## Skills
`finance`, `risk-reviewer`, `functional-spec`, `validator`

## Rules
- `rules/hierarchical-orchestration.md`
