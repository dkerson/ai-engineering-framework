# Workflow: Feature



> Pipeline para novas funcionalidades. Modo padrão: **Standard**. Escalar para Review/Council se auth, pagamento ou arquitetura.



## Trigger

`feature` — implementar, adicionar, criar funcionalidade



## Modo sugerido



| Condição | Modo |

|----------|------|

| Feature pequena, 1–2 módulos | Standard |

| Auth, DB, integração, performance | Review |

| Pagamento, arquitetura, >3 módulos | Technical Council |



## Pipeline por modo



### Standard

```

Product Owner* → [Skill Técnica] → QA → Entrega

```



### Review

```

Context Builder → Product Owner → UX* → Software Architect* → Implementation Planner → [Impl] → Critic → Validator → Entrega

```



### Technical Council

```

Conselho → Decision Maker → Implementation Planner → [Impl] → Critic → Validator → ChangeLog → Entrega

```



\* Condicional conforme escopo.



## Passos (Review)



| # | Skill | Ação |

|---|-------|------|

| 1 | product-owner | Valor, escopo, critérios de aceite |

| 2 | functional-spec | Spec funcional (se necessário) |

| 3 | software-architect | Decisões técnicas, ADR se necessário |

| 4 | implementation-planner | Plano de implementação |

| 5 | backend/api/database/react/flutter | Implementação |

| 6 | critic | Validar abordagem |

| 7 | validator | Testes, lint, build |

| 8 | changelog | Registro de mudança |



## Checklists

- `checklists/feature.md`

- `checklists/review.md`



## Rules

- `rules/hierarchical-orchestration.md`

- `rules/architecture.md`

- `rules/clean-code.md`


