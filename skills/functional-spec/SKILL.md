---
name: functional-spec
description: >-
  Define requisitos funcionais em texto (escopo, fluxos, regras). Para gerar
  arquivos EF HTML+MD Otus7 gravados no repo, o orchestrator usa
  ef-doc-generator automaticamente.
---

# Functional Spec

## Objetivo

Descrever **O QUE** o sistema faz — requisitos, fluxos, regras de negócio.

## Quando usar

- Refinamento de requisitos antes de implementação
- Input para `ef-doc-generator` ou `technical-spec`
- Feature pipeline (workflow `feature.md`)

## Quando NÃO usar

- **Gerar arquivos EF HTML+MD** → orchestrator roteia para `ef-doc-generator`
- Guia passo a passo → `process-doc-generator`
- Spec técnica → `technical-spec`

## Responsabilidades

1. Descrever fluxos principais e alternativos
2. Definir regras de negócio (RN01…)
3. Critérios de aceite testáveis
4. Delegar geração de artefatos Otus7 ao `ef-doc-generator`

## Saídas

- Requisitos em texto/markdown **ou**
- Arquivos em `docs/specs/` quando via `ef-doc-generator`


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- Gerador de arquivos: `skills/ef-doc-generator/SKILL.md`
- Template HTML: `docs/templates/functional-spec.html`
- `templates/functional-spec.md`
