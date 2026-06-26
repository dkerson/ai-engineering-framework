---
name: etl-specialist
description: >-
  Pipelines ETL/ELT, cargas incrementais, integração de fontes e data quality em movimento. Evolução do escopo ETL da skill legada data.
---

# ETL Specialist

## Objetivo

Projetar e revisar pipelines de dados: extração, transformação, carga e idempotência.

## Quando usar

- Pipeline ETL/ELT novo ou alterado
- Carga incremental, CDC, staging
- Integração banco → warehouse → Power BI
- Data quality em pipeline

## Quando NÃO usar

- Query analítica pontual → `sql-architect`
- Dashboard → `powerbi-specialist` / `dashboard-designer`
- CRUD de aplicação → `backend`

## Responsabilidades

1. Definir fontes, destinos e frequência
2. Garantir pipeline idempotente e observável
3. Tratar duplicidade e late-arriving data
4. Aplicar `checklists/data/data-quality.md`
5. Documentar schema de staging e destino

## Nota de compatibilidade

Escopo ETL antes coberto pela skill `data` — workflows legados podem referenciar `data`; preferir `etl-specialist` em pipelines novos.

## Integração

- **Upstream:** data-orchestrator, business-data-analyst
- **Downstream:** sql-architect, data-quality-reviewer, backend

## Referências

- `checklists/data/data-quality.md`
- `rules/data/sql-standards.md`
