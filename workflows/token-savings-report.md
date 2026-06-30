# Token Savings Report Workflow

> Tipo: `token-savings-report` / `framework-operating-system`

## Objetivo

Gerar um relatorio sob demanda sobre economia de tokens, desperdicios evitados e eficiencia operacional do framework.

## Modo sugerido

**Fast** quando apenas gerar relatorio a partir dos ledgers existentes.

**Standard** quando tambem atualizar template, rule, ledger ou report versionado.

## Pipeline

```
Orchestrator
→ Surface Routing + Execution Banner
→ Token Savings Report rule
→ ler TOKEN_METRICS / MISSION_LEDGER / SKILL_USAGE
→ gerar report usando template
→ registrar aprendizado util se aplicavel
→ entrega
```

## Gatilhos

- "gera um report de economia de tokens"
- "quanto economizamos de token"
- "eficiencia do framework"
- "token economy report"
- "token savings report"

## Regras

- Nao medir token real se os dados nao existem.
- Usar `EXECUTION_METRICS.md` para percentual estimado, retries evitados e erros evitados.
- Nao inventar custo em dolar ou porcentagem sem fonte.
- Declarar se o relatorio e medido, estimado ou qualitativo.
- Preferir leitura dos ledgers a varrer o projeto.
- Usar `templates/token-savings-report.md`.

## Fontes

- `framework/operating-system/TOKEN_METRICS.md`
- `framework/operating-system/MISSION_LEDGER.md`
- `framework/operating-system/SKILL_USAGE.md`
- `framework/operating-system/EXECUTION_METRICS.md`
- `rules/token-savings-report.md`

## Entrega

Relatorio em Markdown, preferencialmente em:

`framework/operating-system/reports/TOKEN_SAVINGS_REPORT.md`
