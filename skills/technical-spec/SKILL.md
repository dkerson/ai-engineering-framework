---
name: technical-spec
description: >-
  Produz especificação técnica de implementação. Usar após functional-spec ou para decisões de design.
---

# Technical Spec

## Objetivo

Descrever COMO implementar: componentes, contratos, dados, integrações.

## Quando usar

- Feature complexa
- Documentação técnica
- Antes de implementação multi-camada

## Quando NÃO usar

- Spec funcional pura
- Fix trivial one-liner

## Responsabilidades

1. Definir componentes e responsabilidades
2. Especificar contratos (API, eventos)
3. Modelar dados e migrations
4. Listar dependências e riscos técnicos
5. Usar `templates/technical-spec.md`

## Entradas esperadas

- Functional spec
- Decisões do software-architect

## Saídas esperadas

- Technical spec document
- Diagrama de componentes (opcional)

## Checklist

- [ ] Componentes com SRP
- [ ] Contratos definidos
- [ ] Modelo de dados claro
- [ ] Riscos técnicos listados

## Integração com outras skills

- **Upstream:** functional-spec, software-architect
- **Downstream:** tech-lead, backend, api, database

## Exemplos

**Input:** Login OAuth
**Output:** Spec com endpoints, tokens, middleware, entidades.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `templates/technical-spec.md`
- `rules/architecture.md`
