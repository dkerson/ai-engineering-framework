---
name: backend
description: >-
  Implementa lógica server-side: services, controllers, domain, infra. Usar em tarefas backend .NET, Node, Python, etc.
---

# Backend

## Objetivo

Implementar alterações server-side seguindo camadas e convenções do projeto.

## Quando usar

- Lógica de negócio server-side
- Controllers, services, workers
- Integrações backend

## Quando NÃO usar

- Frontend puro (usar react)
- SQL puro sem camada (usar database)

## Responsabilidades

1. Ler convenções (`AGENTS.md`, `context/coding-standards.md`)
2. Implementar menor diff possível
3. Respeitar camadas (Api → App → Domain → Infra)
4. Tratar erros e validações
5. Não alterar appsettings/secrets sem preservar valores
6. Evitar hardcode funcional; valores variáveis devem seguir `rules/no-hardcode.md`

## Entradas esperadas

- Plano do tech-lead
- Technical spec

## Saídas esperadas

- Código implementado
- Testes se aplicável

## Checklist

- [ ] Camadas respeitadas
- [ ] Validação de entrada
- [ ] Erros tratados
- [ ] Sem secrets expostos
- [ ] Sem hardcode de ambiente, domínio, tenant, permissão ou regra variável
- [ ] Diff mínimo

## Integração com outras skills

- **Upstream:** tech-lead, api, database
- **Downstream:** qa, code-review

## Exemplos

**Input:** Endpoint criar pedido
**Output:** Controller + Service + DTO + teste unitário.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `rules/clean-code.md`
- `rules/no-hardcode.md`
- `checklists/backend.md`
- `checklists/no-hardcode.md`
