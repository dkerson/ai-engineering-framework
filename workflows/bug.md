# Workflow: Bug



> Pipeline para correção de bugs. Modo padrão: **Standard**. Escalar para Review se DB/auth; Council se produção.



## Trigger

`bug` — erros, falhas, comportamento incorreto



## Modo sugerido



| Condição | Modo |

|----------|------|

| 1 arquivo, sem risco | Standard |

| DB, auth, integração | Review |

| Produção, >3 módulos | Technical Council |



## Pipeline por modo



### Standard

```

Context Builder* → Bug Hunter → [Skill Técnica] → QA → Entrega

```



### Review

```

Context Builder → Bug Hunter → Tech Lead → [Skill Técnica] → Critic → Validator → Entrega

```



### Technical Council

```

Conselho → Decision Maker → Implementation Planner → Bug Hunter → [Fix] → Validator → Entrega

```



\* Context Builder somente se contexto insuficiente.



## Passos (Standard)



| # | Skill | Ação |

|---|-------|------|

| 1 | context-builder | Stack, área afetada (se necessário) |

| 2 | bug-hunter | Reproduzir, isolar causa, localizar arquivo/linha |

| 3 | backend/api/database/react/flutter | Implementar correção mínima |

| 4 | qa | Validar fix + regressão mínima |



## Checklists

- `checklists/bug.md`

- `checklists/review.md` (modo Review+)



## Rules

- `rules/hierarchical-orchestration.md`

- `rules/token-economy.md`

- `rules/clean-code.md`



## Template de saída

- `templates/final-response.md`


