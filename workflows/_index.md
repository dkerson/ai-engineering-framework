# Índice de Workflows



> Finalidade: mapeamento central tipo-de-demanda → modo sugerido → pipeline de skills.



## Processo universal



Todo workflow segue: `workflows/_process.md`



## Modos de operação



Antes de executar qualquer workflow, o Orchestrator escolhe o modo: `workflows/modes.md`



| Modo | Quando usar |

|------|-------------|

| Fast | Perguntas, docs simples, alteração mínima |

| Standard | Bug/melhoria/feature pequena |

| Review | Estrutural, DB, auth, integração, performance |

| Technical Council | Risco alto, >3 módulos, arquitetura, incidente |



## Skills de governança (por modo)



| Skill | Fast | Standard | Review | Council |

|-------|------|----------|--------|---------|

| context-builder | — | * | ✓ | ✓ |

| critic | — | — | ✓ | ✓ |

| validator | — | — | ✓ | ✓ |

| risk-reviewer | — | * | * | ✓ |

| decision-maker | — | — | — | ✓ |

| implementation-planner | — | * | * | ✓ |

| qa | — | ✓ | ✓ | ✓ |



\* Quando necessário



## Workflows por tipo



| Arquivo | Tipo | Modo sugerido | Pipeline resumido |

|---------|------|---------------|-------------------|

| [bug.md](bug.md) | Bug | Standard | Context → Bug Hunter → Tech Lead → [técnica] → QA |

| [incident.md](incident.md) | Incidente | **Council** | Conselho → Bug Hunter → Fix → Validator → Release |

| [feature.md](feature.md) | Feature | Standard/Review | PO → Spec → UX → Architect → Impl → QA |

| [refactor.md](refactor.md) | Refatoração | Review/Council | Context → Architect → Planner → Impl → Critic → Validator |

| [review.md](review.md) | Code Review | Fast/Standard | Code Review → Security Review* |

| [documentation.md](documentation.md) | Documentação | **Fast** | Orchestrator ou Context → Tech Spec |

| [functional-spec-doc.md](functional-spec-doc.md) | EF Otus7 | Standard | Context* → EF Doc Generator |

| [process-doc.md](process-doc.md) | Processo / guia | Standard | Context* → Process Doc Generator |

| [performance.md](performance.md) | Performance | Review/Council | Performance → Database → Backend → Critic → Validator |

| [database.md](database.md) | Database | Review/Council | Context → Database → Backend → Critic → Validator |

| [api.md](api.md) | API | Standard/Review | API → Backend → QA → Validator* |

| [integration.md](integration.md) | Integração | Review/**Council** | Conselho → API → Backend → Validator |

| [devops.md](devops.md) | DevOps | Standard/Review | DevOps → QA → Validator |

| [testing.md](testing.md) | Testes | Standard | QA → Playwright* |

| [architecture.md](architecture.md) | Arquitetura | **Council** | Conselho → Architect → Planner → Review |

| [product.md](product.md) | Produto | Fast/Standard | Product Owner → Functional Spec |

| [ux.md](ux.md) | UX | Standard | UX → Func Spec |

| [mobile.md](mobile.md) | Mobile | Standard/Review | Mobile UX → Flutter* → QA |

| [security.md](security.md) | Segurança | Review/**Council** | Security Review → Critic → Validator |

| [data.md](data.md) | Dados | Standard/Review | Data Orchestrator → [skills dados] → Data Validator |

| [hybrid-flows.md](hybrid-flows.md) | Híbrido | Standard/Review | Hybrid Flow Planner → domínios → Validator |

| [data-sql.md](data-sql.md) | SQL | Standard | SQL Architect → Query Optimizer → Data Validator |

| [data-powerbi.md](data-powerbi.md) | Power BI | Standard/Review | PBI → DAX → Query Optimizer → Data Validator |

| [data-report-frontend.md](data-report-frontend.md) | Relatório web | Standard/Review | Semantic → SQL → Backend → React → UX → QA |

| [data-divergence.md](data-divergence.md) | Divergência | Standard/Review | Rule Mapper → SQL → Validator → Bug Hunter |

| [data-procedure.md](data-procedure.md) | Procedure | Review | SQL → DBA Reviewer → Impact → Validator |

| [commercial.md](commercial.md) | Comercial | Fast/Standard | Commercial → Func Spec |

| [finance.md](finance.md) | Financeiro | Review/**Council** | Finance → Func Spec → Risk Reviewer |

| [deployment.md](deployment.md) | Implantação | Review | Deployment → Validator → Release Notes |

| [support.md](support.md) | Suporte | Standard | Support → Bug Hunter* |



\* Condicional — Orchestrator decide conforme risco.



## Processos especiais



| Arquivo | Descrição |

|---------|-----------|

| [modes.md](modes.md) | 4 modos de operação |

| [technical-council.md](technical-council.md) | Processo do Conselho Técnico |

| [_process.md](_process.md) | Fases universais |



## Skills técnicas substituíveis



No passo `[técnica]` ou `Impl`, escolher conforme stack:



- Frontend React/Next → `react`

- Mobile Flutter → `flutter`

- Server/API → `backend` + `api`

- Banco → `database` · SQL analítico/BI → `data-orchestrator` + `sql-architect`

- Dados/BI → ver `docs/DATA_INTELLIGENCE.md`



Detectar stack via `context/tech-stack.md` ou AGENTS.md do projeto.



## Adicionar workflow



1. Criar `workflows/<tipo>.md` seguindo formato de `bug.md`

2. Indicar modo sugerido e critérios de escalonamento

3. Registrar nesta tabela

4. Atualizar classificação em `skills/orchestrator/SKILL.md`

