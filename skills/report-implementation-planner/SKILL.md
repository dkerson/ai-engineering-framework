---
name: report-implementation-planner
description: >-
  Plano técnico executável para implementação de relatórios (frontend web ou Power BI) cruzando SQL, API e UX. Especialização do implementation-planner para relatórios.
---

# Report Implementation Planner

## Objetivo

Produzir plano passo a passo para entregar relatório end-to-end: dados → API → UI ou Power BI.

## Quando usar

- "Criar relatório financeiro na Umbra"
- Novo dashboard com backend + frontend
- Alteração de relatório existente com múltiplas camadas

## Quando NÃO usar

- Plano genérico de feature → `implementation-planner`
- Só otimizar SQL → data-orchestrator direto

## Responsabilidades

1. Sequenciar: semantic layer → SQL → API → UI/BI → validação
2. Listar arquivos/artefatos prováveis (sem ler projeto inteiro)
3. Definir checkpoints com data-validator
4. Estimar riscos e dependências
5. Popular Working Context → seção Plano

## Diferença de implementation-planner

`implementation-planner` é genérico; este planner inclui **camada de dados, validação cruzada e UX de relatório** por padrão.

## Integração

- **Upstream:** hybrid-flow-planner, business-data-analyst, semantic-layer-specialist
- **Downstream:** sql-architect, backend, react, powerbi-specialist, data-validator

## Referências

- `templates/data/report-request.md`
- `examples/data/create-frontend-report.md`
- `workflows/data-report-frontend.md`
