---
name: impact-analysis
description: >-
  Analisa impacto de alterações em banco, procedures, APIs e relatórios dependentes. Complementa risk-reviewer com foco em dependências de dados e BI.
---

# Impact Analysis

## Objetivo

Mapear o que quebra ou muda quando um artefato de dados (procedure, view, coluna, medida) é alterado.

## Quando usar

- Alteração em stored procedure ou view
- Mudança de indicador financeiro
- Novo índice ou coluna usada em relatórios
- Antes de deploy em produção

## Quando NÃO usar

- Risco geral de feature → `risk-reviewer`
- Design de SQL sem commit de mudança → `sql-architect`

## Responsabilidades

1. Listar consumidores: relatórios Power BI, APIs, telas Umbra/Irisys, jobs
2. Classificar impacto: alto/médio/baixo
3. Exigir plano de comunicação e rollback
4. Coordenar com `dba-reviewer` e `data-validator`
5. Documentar no Working Context

## Diferença de risk-reviewer

`risk-reviewer` classifica risco holístico; **impact-analysis** mapeia dependências técnicas de artefatos de dados.

## Integração

- **Upstream:** sql-architect, requirement-reviewer, dba-reviewer
- **Downstream:** deployment, data-validator, qa

## Referências

- `rules/data/safe-database-changes.md`
- `checklists/data/production-safety.md`
