---
name: data
description: >-
  [Legado — evoluída] Analytics, ETL e relatórios. Para demandas novas, o Orchestrator deve preferir data-analyst, etl-specialist e data-orchestrator.
---

# Data (compatibilidade)

> **Skill evoluída em v2.1.** Mantida para workflows e referências legadas. **Não remover.**

## Roteamento para skills especializadas

| Demanda legada | Skill preferida (v2.1+) |
|----------------|-------------------------|
| Análise exploratória, interpretação | `data-analyst` |
| Pipeline ETL/ELT | `etl-specialist` |
| Qualquer domínio de dados | `data-orchestrator` |
| SQL design/review | `sql-architect` |
| Otimização SQL | `query-optimizer` |
| Power BI | `powerbi-specialist` |
| Validação | `data-validator` |

## Objetivo (histórico)

Soluções de dados: pipelines, queries analíticas, dashboards.

## Quando o Orchestrator ainda invoca `data`

- Workflow legado referencia `data` explicitamente
- Demanda genérica "dados" sem subtipo claro — redirecionar internamente para `data-orchestrator`

## Responsabilidades mínimas se invocada diretamente

1. Classificar subtipo e delegar mentalmente à skill especializada
2. Atualizar Working Context
3. Não duplicar trabalho de data-orchestrator se já no pipeline

## Orquestração hierárquica

- **Único contato com usuário:** Orchestrator
- **Working Context:** reutilizar análises
- **Economia:** `rules/token-economy.md`

## Referências

- `docs/DATA_INTELLIGENCE.md`
- `skills/data-analyst/SKILL.md`
- `skills/data-orchestrator/SKILL.md`
