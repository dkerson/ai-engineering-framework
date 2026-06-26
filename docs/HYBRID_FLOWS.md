# Fluxos Híbridos

> Demandas que misturam desenvolvimento, banco, BI, suporte e QA.

## Princípio

Nem toda demanda é só dev. Nem toda é só dados. O **Orchestrator** detecta múltiplos domínios e convoca `hybrid-flow-planner` antes de executar.

## Domínios

```
┌─────────────────────┐
│  Orchestrator       │
└──────────┬──────────┘
           │
    ┌──────┴──────┬──────────────┬─────────────┐
    ▼             ▼              ▼             ▼
Development  Data Intel.   Business/Ops    QA/Validation
```

## Critérios para Hybrid Flow

- task + banco
- banco + frontend
- Power BI + SQL
- relatório + API
- divergência + regra de negócio
- procedure + tela
- indicador + financeiro
- SQL + performance + deploy
- dados + implantação/suporte

## Fluxos documentados

### Relatório financeiro Umbra

```
Orchestrator → task-analyst → business-data-analyst → semantic-layer-specialist
  → sql-architect → backend → report-ux-reviewer → react → qa → data-validator → code-review
```

### Divergência Irisys

```
Orchestrator → context-builder → task-analyst → business-rule-mapper → data-orchestrator
  → sql-architect → data-validator → backend → bug-hunter → qa → cross-domain-decision-maker
```

### Power BI lento

```
Orchestrator → data-orchestrator → powerbi-specialist → dax-specialist → query-optimizer → data-validator
```

### Procedure por task

```
Orchestrator → task-analyst → requirement-reviewer → business-rule-mapper → data-orchestrator
  → sql-architect → dba-reviewer → impact-analysis → data-validator → backend → qa → code-review
```

## Regras

1. Plano único no Working Context
2. Menor conjunto de skills
3. Sem releitura entre skills
4. `cross-domain-decision-maker` em conflitos (não mostrar debate ao usuário)
5. Technical Council só se risco arquitetural — não por default em híbridos

## Skills de governança híbrida

| Skill | Papel |
|-------|-------|
| hybrid-flow-planner | Plano consolidado |
| cross-domain-decision-maker | Decisão entre domínios |
| report-implementation-planner | Relatórios end-to-end |
| data-orchestrator | Sub-plano de dados |

## Referências

- `workflows/hybrid-flows.md`
- `examples/data/hybrid-task-database-frontend.md`
- `context/working-context.md` (seção Data Intelligence)
