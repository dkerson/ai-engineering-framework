# Workflow: Fluxos Híbridos

> Demandas que cruzam desenvolvimento, dados, BI e operações.

## Quando usar Hybrid Flow

Orchestrator detecta **mais de um domínio** ou critérios:

- task + banco
- banco + frontend
- Power BI + SQL
- relatório + API
- divergência + regra de negócio
- procedure + tela
- indicador + financeiro
- SQL + performance + deploy
- dados + implantação/suporte

## Domínios lógicos

| Domínio | Skills |
|---------|--------|
| **Development** | backend, api, react, database, flutter |
| **Data Intelligence** | data-orchestrator, sql-architect, powerbi-specialist, ... |
| **Business/Operations** | task-analyst, business-rule-mapper, support, product-owner |
| **QA/Validation** | data-validator, qa, bug-hunter, code-review, validator |

## Processo

```
1. Orchestrator classifica domínios
2. hybrid-flow-planner → plano único mínimo
3. data-orchestrator (se dados envolvidos)
4. Execução na ordem do plano — Working Context compartilhado
5. cross-domain-decision-maker se conflito entre domínios
6. data-validator + qa antes de entregar
7. Evitar Technical Council salvo risco arquitetural
```

## Regras do Hybrid Flow

1. Identificar domínios envolvidos
2. Menor conjunto possível de skills
3. Não convocar Council sem necessidade
4. Compartilhar Working Context
5. Não repetir análise
6. Plano único consolidado
7. Validar código **e** dados

## Pipelines de referência

Ver `docs/HYBRID_FLOWS.md` e `examples/data/hybrid-task-database-frontend.md`

## Skills de planejamento

- `hybrid-flow-planner` — plano macro
- `report-implementation-planner` — relatórios end-to-end
- `data-orchestrator` — sub-plano de dados
- `cross-domain-decision-maker` — decisões entre domínios
