---
name: ux
description: >-
  Experiência de usuário web: fluxos, wireframes textuais, acessibilidade.
---

# UX

## Objetivo

Definir experiência usable e acessível antes/durante implementação.

## Quando usar

- Nova tela/fluxo web
- Melhoria de usabilidade
- Antes de implementação frontend

## Quando NÃO usar

- Mobile app (mobile-ux)
- Backend puro

## Responsabilidades

1. Mapear user journey
2. Definir estados: loading, empty, error
3. Hierarquia visual e CTA
4. A11y: contraste, keyboard, labels
5. Wireframe textual

## Entradas esperadas

- Functional spec
- Product owner requirements

## Saídas esperadas

- Fluxos UX
- Requisitos de interface
- Wireframes textuais

## Checklist

- [ ] Happy path claro
- [ ] Error/empty states
- [ ] A11y considerada
- [ ] Mobile-first se aplicável

## Integração com outras skills

- **Upstream:** functional-spec
- **Downstream:** react

## Exemplos

**Input:** Checkout flow
**Output:** 3 steps, progress indicator, error em pagamento.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `checklists/frontend.md`
