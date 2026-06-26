# Workflow: Documentação técnica

> Documentação de código/arquitetura. Modo padrão: **Fast** para perguntas; **Standard** para gerar docs.

## Trigger

`documentation` — documente código, README, arquitetura técnica

**Não usar para:**
- EF kickoff → `functional-spec-doc` → `ef-doc-generator`
- Guia passo a passo → `process-doc` → `process-doc-generator`

## Modo sugerido

| Condição | Modo |
|----------|------|
| Pergunta/explicação | **Fast** |
| Gerar documentação | Standard |

## Pipeline (Fast)

```
Orchestrator → Entrega
```

## Pipeline (Standard)

```
Context Builder → Technical Spec → Validator* → Entrega
```

## Passos (Standard)

| # | Skill | Ação |
|---|-------|------|
| 1 | context-builder | Mapear código e domínio existente |
| 2 | technical-spec | Spec técnica (`templates/technical-spec.md`) |
| 3 | validator | Revisar precisão (checklist documentação) |

## Checklists
- `checklists/review.md`

## Rules
- `rules/hierarchical-orchestration.md`
- `rules/documentation.md`
