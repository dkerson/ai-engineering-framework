---
name: playwright
description: >-
  Testes E2E com Playwright: fluxos críticos, selectors, CI integration.
---

# Playwright

## Objetivo

Automatizar testes end-to-end de fluxos críticos.

## Quando usar

- E2E de fluxo crítico
- Regressão UI automatizada
- CI E2E pipeline

## Quando NÃO usar

- Testes unitários (qa)
- Testes de API isolados

## Responsabilidades

1. Identificar fluxos críticos (login, checkout, etc.)
2. Page Object Model
3. Selectors estáveis (data-testid)
4. Rodar apenas spec relacionado
5. Integrar CI se projeto tiver

## Entradas esperadas

- QA test plan
- Fluxos funcionais

## Saídas esperadas

- Specs Playwright
- Resultado de execução

## Checklist

- [ ] Fluxos críticos cobertos
- [ ] Selectors estáveis
- [ ] Sem flaky waits fixos
- [ ] Screenshots on failure

## Integração com outras skills

- **Upstream:** qa, ux
- **Downstream:** devops (CI)

## Exemplos

**Input:** Fluxo login
**Output:** login.spec.ts com OAuth mock.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `rules/testing.md`
