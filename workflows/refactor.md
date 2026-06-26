# Workflow: Refatoração

> Reorganização de código. Modo padrão: **Review**. Council se grande escopo ou >3 módulos.

## Trigger
`refactor` — refatore, limpe, reorganize

## Modo sugerido

| Condição | Modo |
|----------|------|
| 1–2 módulos | Review |
| Grande escopo, >3 módulos | **Technical Council** |

## Pipeline (Review)

```
Context Builder → Software Architect → Implementation Planner → [Impl] → Critic → Validator → Entrega
```

## Pipeline (Council)

```
Conselho → Decision Maker → Implementation Planner → [Impl] → Critic → Validator → Code Review → Entrega
```

## Skills
`context-builder`, `software-architect`, `implementation-planner`, `critic`, `validator`, `code-review`

## Checklist
- `checklists/review.md`

## Rules
- `rules/hierarchical-orchestration.md`
- `rules/clean-code.md`
