---
name: mission-builder
description: >-
  Monta Mission completa a partir do Translation Brief: objetivo, plano, roadmap, domínios, skills, capabilities, plugins, dependências e validações. Invocado pelo Orchestrator via NLME. Nunca implementa código.
---

# Mission Builder

## Objetivo

Transformar **Translation Brief** + **Goal Recognition** em **Mission Package** pronta para Prompt Builder e SIL.

## Quando usar

- Após mission-translator em todo fluxo NLME
- Missões estratégicas, multi-domínio ou autônomas

## Quando NÃO usar

- Fast mode com demanda técnica explícita já classificada (Orchestrator pode pular NLME completo)
- **Nunca** auto-iniciar

## Responsabilidades

1. Consolidar **objetivo principal** e **secundários** (Goal Recognition)
2. Selecionar **Mission Type** → `docs/Mission-Catalog.md`
3. Definir **Mission Mode** estratégico → `docs/Mission-Modes.md`
4. Montar **plano de alto nível** (máx. 10 passos)
5. Selecionar **workflow(s)** → `workflows/_index.md`
6. Listar **skills**, **capabilities**, **plugins** mínimos (Autonomous Planning)
7. Definir **dependências** e **validações** esperadas
8. Esboçar **roadmap** (quick wins · curto · médio · estratégico)
9. Calcular **Mission Confidence Score** → `docs/Mission-Confidence.md`
10. Registrar intenção em **Mission Memory** (FOS) ao encerrar missão

## Orquestração hierárquica

- **Upstream:** mission-translator, goal-recognition
- **Downstream:** prompt-builder → SIL → capability-resolver → orchestrator
- **COS:** consultar `capabilities/registry/CAPABILITY_REGISTRY.md`
- **Infra:** project-resolver quando projeto conhecido

## Saídas esperadas

**Mission Package** (Working Context):

```yaml
mission_type: Product Evolution Mission
mission_mode: Analysis | Planning | Implementation | ...
objective_primary: ""
objectives_secondary: []
project: ""
domains: []
capabilities: []
plugins: []
workflows: []
skills_pipeline: []
operational_mode: Fast | Standard | Review | Council
plan_steps: []
roadmap:
  quick_wins: []
  short_term: []
  medium_term: []
  strategic: []
dependencies: []
validations: []
mission_confidence: 0-100
questions_for_user: []  # máx. 3, só se confidence < threshold
```

## Checklist

- [ ] Mission Type do catálogo oficial
- [ ] Pipeline mínimo — sem skills desnecessárias
- [ ] Confidence calculado; perguntas só se crítico
- [ ] Mission Memory campos preparados para FOS

## Referências

- `docs/Autonomous-Planning.md`
- `docs/Mission-Catalog.md`
- `docs/Missions.md`
- `rules/natural-language-mission-engine.md`
