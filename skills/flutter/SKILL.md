---
name: flutter
description: >-
  Implementa apps mobile Flutter: widgets, state, navigation, platform channels.
---

# Flutter

## Objetivo

Desenvolver UI mobile Flutter com performance e UX nativa.

## Quando usar

- Telas Flutter
- Widgets, BLoC/Riverpod
- Integração mobile API

## Quando NÃO usar

- Web React (usar react)
- Backend puro

## Responsabilidades

1. Seguir arquitetura do projeto (features/layers)
2. Widgets composáveis
3. State management consistente
4. Testes widget quando crítico
5. Platform-specific via channels se necessário

## Entradas esperadas

- Mobile UX spec
- API contracts

## Saídas esperadas

- Telas/widgets implementados

## Checklist

- [ ] State management correto
- [ ] Performance (const, listView.builder)
- [ ] Offline handling se aplicável
- [ ] Testes widget críticos

## Integração com outras skills

- **Upstream:** mobile-ux, tech-lead
- **Downstream:** qa, code-review

## Exemplos

**Input:** Tela home dashboard
**Output:** DashboardScreen + provider + API service.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `checklists/frontend.md`
