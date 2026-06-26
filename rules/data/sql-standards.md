# Padrões SQL

## Nomenclatura

- Aliases curtos mas legíveis (cte, viagem, cli)
- CTEs para etapas lógicas nomeadas

## Estrutura

- Filtros de período sempre explícitos
- Evitar SELECT * em produção
- Comentar regra de negócio não óbvia

## SQL Server (Otus/Irisys)

- Preferir SARGable predicates
- SET NOCOUNT ON em procedures
- Transações explícitas em alterações multi-step

## Segurança

- Ver `safe-database-changes.md`
