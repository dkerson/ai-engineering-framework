---
name: api
description: >-
  Define e implementa contratos REST/GraphQL: endpoints, DTOs, validação, documentação OpenAPI.
---

# API

## Objetivo

Garantir APIs consistentes, versionadas e bem documentadas.

## Quando usar

- Novo endpoint
- Alteração de contrato
- Integração externa via API

## Quando NÃO usar

- Lógica de negócio interna (backend)
- UI components (react)

## Responsabilidades

1. Definir método, path, request/response
2. Validar inputs (400) e auth (401/403)
3. Documentar OpenAPI/Swagger
4. Seguir convenções REST do projeto
5. Usar `rules/api.md`

## Entradas esperadas

- Technical spec
- Functional spec

## Saídas esperadas

- Endpoints implementados
- Contrato documentado

## Checklist

- [ ] Status codes corretos
- [ ] Validação de input
- [ ] Paginação/filtros se listagem
- [ ] Swagger atualizado
- [ ] Breaking changes identificados

## Integração com outras skills

- **Upstream:** tech-lead, functional-spec
- **Downstream:** backend, qa

## Exemplos

**Input:** GET /api/orders?page=1
**Output:** Endpoint paginado com OrderListDto.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `rules/api.md`
- `checklists/api.md`
