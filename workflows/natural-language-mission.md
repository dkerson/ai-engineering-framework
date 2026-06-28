# Workflow: Natural Language Mission

> Entrada para linguagem natural ambigua, estrategica, multi-dominio ou de maior risco. Preserva SIL, COS e Orchestrator.

## Trigger

Usar quando o pedido exigir interpretacao de objetivo, planejamento, roadmap, auditoria, transformacao, produto/design/growth/data, arquitetura, seguranca, banco, producao ou multiplos dominios.

Antes deste workflow, o Orchestrator deve avaliar Fast Path em `rules/token-budget-policy.md`.

Nao usar NLME completo para confirmacoes, status, comandos diretos, explicacoes simples, docs estreitas, typo ou mudanca pequena de baixo risco.

Exemplos: "Transforme o Umbra", "Modernize o Irisys", "Analise o KB", "Esse dashboard esta ruim", "Quero vender mais".

## Pipeline

```text
Usuario
  -> mission-translator (Translation Brief)
  -> goal-recognition (objetivo real)
  -> mission-builder (Mission Package + Confidence)
  -> prompt-builder (Structured Prompt - interno)
  -> SIL (Mission Brief)
  -> capability-resolver (COS)
  -> orchestrator (modo + execucao)
  -> domains / skills
  -> Mission Report + Mission Memory (FOS)
```

## Primeira resposta (obrigatoria)

Template: `templates/mission/nlme-first-response.md`

Apresentar missao, objetivo, capabilities, dominios, plano e roadmap antes de investigar codigo.

## Escalonamento

| Confidence | Acao |
|------------|------|
| >= 60 | Executar apos resposta inicial |
| < 60 | Perguntas minimas -> retomar pipeline |

## Modo operacional

Definido em Mission Package -> validado pelo Orchestrator (`workflows/modes.md`).

## Referencias

- `docs/Natural-Language-Missions.md`
- `workflows/strategic-mission.md` (missoes amplas - compativel)
- `rules/natural-language-mission-engine.md`
- `rules/token-budget-policy.md`
