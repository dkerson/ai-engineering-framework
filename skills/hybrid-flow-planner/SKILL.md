---
name: hybrid-flow-planner
description: >-
  Monta plano único consolidado para demandas que cruzam desenvolvimento, dados, BI e operações. Invocado pelo Orchestrator quando múltiplos domínios são detectados.
---

# Hybrid Flow Planner

## Objetivo

Identificar domínios envolvidos e montar o **menor pipeline** que cobre dev + dados + BI + QA sem repetir análise.

## Quando usar

Critérios (qualquer um):

- task + banco
- banco + frontend
- Power BI + SQL
- relatório + API
- divergência + regra de negócio
- procedure + tela
- indicador + financeiro
- SQL + performance + deploy
- dados + implantação/suporte

## Quando NÃO usar

- Domínio único (só SQL, só React) → Orchestrator ou data-orchestrator direto
- Technical Council já convocado para arquitetura macro

## Responsabilidades

1. Listar domínios: Development · Data Intelligence · Business/Operations · QA/Validation
2. Escolher menor conjunto de skills (ver `docs/HYBRID_FLOWS.md`)
3. Definir ordem: análise de negócio → dados → implementação → validação
4. Compartilhar Working Context — proibir releitura
5. Evitar Technical Council sem necessidade
6. Gerar plano único no Working Context
7. Delegar subdomínio dados ao `data-orchestrator`

## Domínios lógicos

| Domínio | Skills típicas |
|---------|----------------|
| Development | backend, api, react, database |
| Data Intelligence | data-orchestrator, sql-architect, powerbi-specialist, ... |
| Business/Operations | task-analyst, business-rule-mapper, support |
| QA/Validation | data-validator, qa, bug-hunter, code-review |

## Orquestração hierárquica

- **Único contato com usuário:** Orchestrator principal
- **Não substitui** Orchestrator — produz plano para ele executar

## Integração

- **Upstream:** orchestrator, task-analyst
- **Downstream:** data-orchestrator, report-implementation-planner, implementation-planner

## Referências

- `docs/HYBRID_FLOWS.md`
- `workflows/hybrid-flows.md`
- `examples/data/hybrid-task-database-frontend.md`
