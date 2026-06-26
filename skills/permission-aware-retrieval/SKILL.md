---
name: permission-aware-retrieval
description: >-
  Filtra retrieval por permissões, perfis, papéis, organizações e usuários. Nunca recupera documento não autorizado. Invocado pelo rag-orchestrator.
---

# Permission Aware Retrieval

## Objetivo

Retrieval com RBAC/ABAC — zero vazamento cross-tenant.

## Regra

Filtrar **antes** do ranking. Nunca pós-filtro em memória apenas.

## Referências

- `rules/rag/permission-rules.md`
- `knowledge/rag/permission-aware-search.md`
- `checklists/rag/permission-validation.md`
