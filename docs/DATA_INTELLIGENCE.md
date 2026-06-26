# Data Intelligence — Guia do Domínio

> AI Engineering Framework v2.1+ — equipe de Dados/BI (SQL, Power BI, relatórios Umbra/Irisys).

## Visão

O domínio **Data Intelligence** complementa Development sem substituí-lo. O **Orchestrator principal** continua decidindo tudo; quando detecta dados, invoca o **data-orchestrator** como sub-orquestrador.

```
Orchestrator principal
       ↓ (domínio dados)
data-orchestrator
       ↓
sql-architect · query-optimizer · powerbi-specialist · data-validator · ...
```

## Casos de uso

| Demanda | Skills principais |
|---------|-------------------|
| Otimizar SQL | sql-architect, query-optimizer, data-validator |
| Power BI lento | powerbi-specialist, dax-specialist, query-optimizer |
| Relatório web | semantic-layer-specialist, sql-architect, backend, react, report-ux-reviewer |
| Divergência | business-rule-mapper, sql-architect, data-validator, bug-hunter |
| Procedure/indicador | sql-architect, dba-reviewer, impact-analysis |
| ETL | etl-specialist, data-quality-reviewer |

## Skills do domínio

| Skill | Papel |
|-------|-------|
| **data-orchestrator** | Sub-orquestrador de dados |
| data-analyst | Análise e interpretação |
| business-data-analyst | Negócio → métricas |
| sql-architect | Design/review SQL |
| query-optimizer | Performance SQL |
| dba-reviewer | Segurança em produção |
| data-validator | Consistência banco/API/tela/BI |
| powerbi-specialist | Modelo e performance PBI |
| dax-specialist | Medidas DAX |
| dashboard-designer | Estrutura de dashboard |
| report-ux-reviewer | UX de relatório web |
| etl-specialist | Pipelines ETL |
| semantic-layer-specialist | Camada semântica |
| data-quality-reviewer | Qualidade de dados |

## Camada semântica

`context/semantic-layer/` — templates para CTe, MDFe, financeiro, viagem, etc. **Preencher com o time; não inventar regras.**

## Artefatos

| Tipo | Caminho |
|------|---------|
| Templates | `templates/data/` |
| Checklists | `checklists/data/` |
| Rules | `rules/data/` |
| Exemplos | `examples/data/` |
| Workflows | `workflows/data-*.md` |

## Economia de tokens (SQL)

Ordem obrigatória: consulta → erro → tabela → joins → filtros → agregações → procedures → plano → índices → API/tela.

Ver `rules/data/query-performance.md`.

## Segurança em banco

Toda alteração exige impacto, rollback e validação segura. Ver `rules/data/safe-database-changes.md`.

## Resposta final

`templates/data/final-response-data.md`

## Compatibilidade

A skill legada `data` foi preservada e roteia para especializadas. Workflows antigos continuam válidos.
