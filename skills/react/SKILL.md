---
name: react
description: >-
  Implementa frontend React/Next.js: components, hooks, state, routing.
---

# React

## Objetivo

Desenvolver UI React seguindo padrões do projeto.

## Quando usar

- Componentes React/Next
- Hooks, state management
- Integração com API frontend

## Quando NÃO usar

- Flutter mobile (usar flutter)
- Backend API

## Responsabilidades

1. Ler estrutura (`features/`, `core/`)
2. Componentes pequenos e focados
3. Tipagem TypeScript estrita
4. Acessibilidade básica
5. Mensagens UI em pt-BR se projeto BR
6. Evitar hardcode de URL, permissao, status, tenant, menu ou regra de exibicao

## Entradas esperadas

- UX spec
- API contracts

## Saídas esperadas

- Componentes implementados
- Testes se aplicável

## Checklist

- [ ] Tipos corretos
- [ ] Loading/error states
- [ ] Responsivo se aplicável
- [ ] Sem console.log
- [ ] A11y básica
- [ ] Sem hardcode de ambiente, permissao, menu, status ou regra variavel

## Integração com outras skills

- **Upstream:** ux, tech-lead, api
- **Downstream:** qa, code-review

## Exemplos

**Input:** Tela login Google
**Output:** LoginComponent + OAuth redirect handler.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `checklists/frontend.md`
- `checklists/no-hardcode.md`
- `rules/clean-code.md`
- `rules/no-hardcode.md`
