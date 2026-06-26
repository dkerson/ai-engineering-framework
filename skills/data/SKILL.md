---
name: data
description: >-
  Analytics, ETL, pipelines, relatórios, data modeling.
---

# Data

## Objetivo

Soluções de dados: pipelines, queries analíticas, dashboards.

## Quando usar

- Pipeline ETL
- Relatório/analytics
- Data modeling

## Quando NÃO usar

- CRUD app simples (backend)
- UI sem dados

## Responsabilidades

1. Definir fontes e destinos
2. Modelar dados analíticos
3. Pipeline idempotente
4. Validar qualidade dos dados
5. Documentar schema analítico

## Entradas esperadas

- Requisitos de reporting
- Sources disponíveis

## Saídas esperadas

- Pipeline/queries
- Documentação de dados

## Checklist

- [ ] Schema definido
- [ ] Pipeline idempotente
- [ ] Data quality checks
- [ ] Performance acceptable

## Integração com outras skills

- **Upstream:** product-owner
- **Downstream:** backend, qa

## Exemplos

**Input:** Dashboard vendas
**Output:** ETL daily + star schema + API aggregation.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `context/domain.md`
