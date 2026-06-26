---
name: database
description: >-
  Schema, migrations, queries, índices, performance SQL. Usar em alterações de banco de dados.
---

# Database

## Objetivo

Gerenciar persistência de forma segura e performática.

## Quando usar

- Migration nova
- Query lenta
- Modelagem de entidades
- Índices

## Quando NÃO usar

- ORM config trivial sem schema change
- Lógica de aplicação pura

## Responsabilidades

1. Analisar schema atual
2. Criar migration reversível
3. Otimizar queries (evitar N+1)
4. Validar índices
5. Usar `templates/migration.md`

## Entradas esperadas

- Technical spec
- Entity model

## Saídas esperadas

- Migration scripts
- Queries otimizadas

## Checklist

- [ ] Migration up/down testada
- [ ] Índices adequados
- [ ] Sem data loss
- [ ] Naming consistente
- [ ] Rollback plan

## Integração com outras skills

- **Upstream:** tech-lead, software-architect
- **Downstream:** backend, qa

## Exemplos

**Input:** Campo status em orders
**Output:** Migration AddStatusToOrders + índice.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `rules/database.md`
- `checklists/database.md`
- `templates/migration.md`
