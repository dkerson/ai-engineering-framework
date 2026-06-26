# Arquitetura — AI Engineering Framework

> Framework agnóstico de projeto. Compatível com Codex, Cursor e ferramentas baseadas em AGENTS.md.

## Visão geral

```
┌─────────────────────────────────────────────────────────┐
│                    Projeto consumidor                    │
│  AGENTS.md (projeto)  +  context/ (stack, domínio)      │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│              AI Engineering Framework                    │
│                                                          │
│  FOS ──► SIL ──► Mission ──► Orchestrator ──► Modo       │
│       │                                                  │
│       ├── Working Context (temporário)                   │
│       ├── Workflows (pipelines por tipo)                 │
│       ├── Skills (sob demanda, nunca auto-iniciam)     │
│       ├── Rules (token economy, orquestração)            │
│       └── Templates + Checklists                         │
└─────────────────────────────────────────────────────────┘
```

## Camadas

| Camada | Pasta | Responsabilidade |
|--------|-------|------------------|
| Bootstrap | `AGENTS.md` | Entrada universal; aponta para SIL + Orchestrator |
| Framework Operating System | `framework/operating-system/` | Governa evolucao, saude, roadmap, backlog, metricas e recomendacoes |
| Strategic Intelligence | `docs/Strategic-Intelligence-Layer.md` | Interpreta linguagem natural e cria Mission Briefs |
| Infrastructure Intelligence | `infrastructure/` | Registra projetos, repositorios, bancos, servicos, APIs, MCPs e ambientes |
| Orquestração | `skills/orchestrator/` | Modo, pipeline, Working Context, entrega |
| Governança | `critic`, `validator`, `risk-reviewer`, `decision-maker`, `implementation-planner` | Qualidade e decisão |
| Execução | Skills técnicas (`backend`, `api`, `react`, …) | Implementação especializada |
| Fluxos | `workflows/` | Pipelines por tipo de demanda + modos |
| Regras | `rules/` | Políticas transversais |
| Knowledge Hub | `knowledge/` | Boas praticas resumidas por area, consultadas pelo Knowledge Engine |
| Artefatos | `templates/`, `checklists/` | Saídas padronizadas |
| Contexto | `context/` | Stack e domínio **do projeto consumidor** |

## Modos de execução

Detalhe em `workflows/modes.md`.

| Modo | Skills típicas | Tokens |
|------|----------------|--------|
| Fast | 0 | Mínimo |
| Standard | 2–3 | Baixo |
| Review | 4–6 | Médio |
| Technical Council | 6+ (conselho) | Alto, mas controlado (150 pal/skill) |

## Technical Council

Processo — **não é skill**. Documentado em `workflows/technical-council.md`.

## Strategic Intelligence Layer

O SIL fica acima do Master Orchestrator. Ele nao implementa codigo, nao chama skills e nao altera arquivos. Sua saida e um Mission Brief com objetivo, mission type, mission mode, score, dominios, riscos, quick wins e plano estrategico.

Detalhes: `docs/Strategic-Intelligence-Layer.md`, `docs/Missions.md`, `docs/Mission-Recognition.md`, `docs/Mission-Modes.md`, `docs/Continuous-Evolution.md`.

## Framework Operating System

O FOS governa o proprio framework. Ele registra, aprende, mede, organiza, prioriza, versiona, documenta, audita e recomenda. Ele nunca implementa automaticamente e toda mudanca depende de aprovacao do usuario.

Detalhes: `docs/Framework-Operating-System.md` e `framework/operating-system/`.

## Infrastructure Intelligence

Infrastructure Intelligence registra e consulta infraestrutura dos projetos. Ele conhece Project Registry, Infrastructure Registry, MCP Registry, Connection Registry, dashboards e health reports. Credenciais reais nunca sao armazenadas.

Detalhes: `docs/Infrastructure-Intelligence.md`, `docs/Project-Registry.md`, `docs/Infrastructure-Registry.md`.

## Working Context

Memória de sessão em `context/working-context.md`. Evita releitura entre skills.

## Responsabilidades — sem sobreposição

| Componente | Papel | Não faz |
|------------|-------|---------|
| **Orchestrator** | Decide, comunica, consolida | Implementar código |
| **Context Builder** | Mapeia stack e área afetada | Implementar |
| **Tech Lead** | Plano e divisão (legado, Standard) | Validar entrega final |
| **Implementation Planner** | Plano detalhado (Review/Council) | Decidir conflitos |
| **Decision Maker** | Resolve conflitos do conselho | Falar com usuário |
| **QA** | Estratégia e casos de teste | Checklist final de entrega |
| **Validator** | Lint, build, typecheck, prontidão | Escrever testes novos |
| **Critic** | Questiona solução | Implementar |
| **Risk Reviewer** | Classifica risco | Implementar |

### Tech Lead vs Implementation Planner

- **Tech Lead** — mantido para compatibilidade; usado em pipelines Standard e workflows legados.
- **Implementation Planner** — usado em Review e Technical Council quando o plano exige etapas, arquivos e validações explícitas.
- Orchestrator escolhe um ou ambos conforme complexidade — não duplicar planos.

### QA vs Validator

- **QA** — durante implementação (casos, regressão).
- **Validator** — gate final antes da entrega (prontidão objetiva).

## Compatibilidade de stacks

O framework é agnóstico. Skills técnicas cobrem:

| Stack | Skills |
|-------|--------|
| Node / NestJS | `backend`, `api` |
| React / Next.js | `react` |
| Flutter | `flutter`, `mobile-ux` |
| .NET | `backend`, `api`, `database` |
| Python / Go | `backend`, `api` |
| SQL Server / Power BI | `data-orchestrator`, `sql-architect`, `powerbi-specialist` |

Defina a stack real em `context/tech-stack.md` do projeto consumidor.

## Domínios lógicos (v2.1+)

Além dos modos de execução, o Orchestrator classifica **domínios** envolvidos:

| Domínio | Sub-orquestrador | Skills |
|---------|------------------|--------|
| Development | — | backend, api, react, database |
| Data Intelligence | `data-orchestrator` | sql-architect, powerbi-specialist, data-validator, ... |
| Infrastructure Intelligence | — | project-resolver, infrastructure-discovery, project-scanner, integration-resolver |
| Growth & Brand Intelligence | — | project-style-analyzer, knowledge-engine, brand-strategist, copywriter, ux-writer, asset-intelligence, seo-specialist, benchmark-intelligence, product-excellence |
| Business/Operations | — | task-analyst, business-rule-mapper, support |
| QA/Validation | — | qa, data-validator, bug-hunter, validator |

Fluxos que cruzam domínios usam `hybrid-flow-planner`. Detalhe: `docs/HYBRID_FLOWS.md` · `docs/DATA_INTELLIGENCE.md` · `docs/GROWTH_BRAND_INTELLIGENCE.md`.

### Growth & Brand Intelligence

- Cobre landing pages, sites, paginas institucionais, telas publicas, onboarding, copy, SEO, branding e assets.
- Trabalha integrado a product-owner, ux, react, flutter, design system e QA.
- Asset Intelligence decide o tipo de recurso visual antes de buscar imagens ou sugerir fontes externas.
- Product Audit inclui notas 0-10 para Copy, Brand, Marketing, Conversao, Landing Page, SEO, Assets, Comunicacao, Identidade Visual e Tom de Voz.
- Project Style Analyzer define Legacy Mode, Hybrid Mode, Greenfield Mode ou Automatic Mode.
- Knowledge Engine consulta `knowledge/` antes de planejar quando a demanda exige boas praticas especificas.
- Product Excellence avalia o padrao minimo de produto e aciona Product Evolution quando notas ficam abaixo de 8.

### data-orchestrator vs Orchestrator

- **Orchestrator** — único contato com usuário; decide modo e domínios.
- **data-orchestrator** — sub-plano de dados; nunca substitui o principal.

## Extensibilidade

Nova skill via `skills/skill-builder/SKILL.md`:

1. `skills/<nome>/SKILL.md`
2. Registro em `AGENTS.md` e `workflows/_index.md`
3. Exemplo em `examples/`
4. Checklist em `checklists/` (se aplicável)
5. Seção Orquestração hierárquica obrigatória

## Decisões arquiteturais (ADRs implícitos)

| Decisão | Motivo |
|---------|--------|
| Orchestrator monopólio | Decisão centralizada, menos tokens |
| SIL acima do Orchestrator | Linguagem natural vira Mission antes da execucao operacional |
| FOS como sistema operacional | O framework passa a manter saude, historico, roadmap e recomendacoes sem auto-modificacao |
| Pasta `Personal-AI/` preservada | Compatibilidade Umbra e consumidores v1 |
| Submodule como instalação primária | Atualização isolada do framework |
| Council como processo, não skill | Composição dinâmica por demanda |
| Context como overlay | Framework independente de domínio |
