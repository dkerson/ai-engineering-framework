---
name: capability-evaluator
description: >-
  Avalia se uma necessidade deveria ser nova Skill, Workflow, Plugin, Rule ou nova Capability. Sempre justifica. Invocado pelo Orchestrator ou SIL via Mission Brief.
---

# Capability Evaluator

## Objetivo

Decidir o **nível correto** de extensão do framework.

## Perguntas (sempre justificar)

| Opção | Quando |
|-------|--------|
| **Nova Skill** | Responsabilidade única dentro de capability existente |
| **Novo Workflow** | Sequência nova de skills em capability existente |
| **Novo Plugin** | Integração externa; **deve** ter capability responsável |
| **Nova Rule** | Política transversal ou específica de capability |
| **Nova Capability** | Competência completa nova (RAG, OCR, Voice, ...) |

## Algoritmo

```
1. capability-resolver → capability existente cobre?
2. SE sim → skill/workflow/rule dentro dela
3. SE parcial → estender capability (builder)
4. SE não → propor nova Capability (discovery registra Idea)
5. Documentar justificativa no Working Context
```

## Nunca

- Implementar automaticamente
- Criar plugin sem capability pai

## Referências

- `capabilities/registry/CAPABILITY_REGISTRY.md`
- `plugins/PLUGIN_POLICY.md`
