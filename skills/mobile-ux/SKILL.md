---
name: mobile-ux
description: >-
  Experiência mobile: gestos, navegação, platform guidelines.
---

# Mobile UX

## Objetivo

Definir UX mobile seguindo iOS/Android guidelines.

## Quando usar

- App mobile
- Telas Flutter/RN
- Gestos e navegação

## Quando NÃO usar

- Web desktop (ux)
- Backend

## Responsabilidades

1. Seguir Material/Cupertino guidelines
2. Thumb zone, bottom nav
3. Offline states
4. Push/deep links se aplicável
5. Platform-specific patterns

## Entradas esperadas

- Functional spec
- Mobile requirements

## Saídas esperadas

- Mobile UX spec
- Navigation map

## Checklist

- [ ] Platform guidelines
- [ ] Gesture navigation
- [ ] Offline handling
- [ ] Safe areas

## Integração com outras skills

- **Upstream:** functional-spec
- **Downstream:** flutter

## Exemplos

**Input:** App banking
**Output:** Tab nav + biometric login flow.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `checklists/frontend.md`
