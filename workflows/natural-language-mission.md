# Workflow: Natural Language Mission

> Entrada universal para linguagem natural. Preserva SIL, COS e Orchestrator.

## Trigger

Qualquer pedido em linguagem natural — especialmente sem especificação técnica.

Exemplos: "Transforme o Umbra", "Modernize o Irisys", "Analise o KB", "Esse dashboard está ruim", "Quero vender mais".

## Pipeline

```text
Usuário
  → mission-translator (Translation Brief)
  → goal-recognition (objetivo real)
  → mission-builder (Mission Package + Confidence)
  → prompt-builder (Structured Prompt — interno)
  → SIL (Mission Brief)
  → capability-resolver (COS)
  → orchestrator (modo + execução)
  → domains / skills
  → Mission Report + Mission Memory (FOS)
```

## Primeira resposta (obrigatória)

Template: `templates/mission/nlme-first-response.md`

Apresentar missão, objetivo, capabilities, domínios, plano e roadmap **antes** de investigar código.

## Escalonamento

| Confidence | Ação |
|------------|------|
| ≥ 60 | Executar após resposta inicial |
| < 60 | Perguntas mínimas → retomar pipeline |

## Modo operacional

Definido em Mission Package → validado pelo Orchestrator (`workflows/modes.md`).

## Referências

- `docs/Natural-Language-Missions.md`
- `workflows/strategic-mission.md` (missões amplas — compatível)
- `rules/natural-language-mission-engine.md`
