# Changelog — AI Engineering Framework

## [2.18.0] - 2026-06-30

### Adicionado

- **Model Routing & Approval Gate:** `rules/model-routing.md`
- Recomendacao de modelo antes da execucao: Composer 2.5 Standard, Auto ou modelo forte conforme custo/risco
- Gate obrigatorio de plano + modelo recomendado + aprovacao do usuario antes de executar tasks

### Alterado

- Orchestrator passa a aplicar Model Routing antes de criar o plano executavel
- Token Budget e Token Economy passam a exigir recomendacao de modelo e pausa quando houver gatilho de escalonamento
- Working Context e resposta final registram modelo recomendado, motivo, aprovacao e troca solicitada
- Processo universal passa a incluir plano + modelo + aprovacao antes de investigar, editar, executar comandos ou validar

### Preservado

- O framework nao altera automaticamente o seletor de modelo do Cursor
- Fast Path pode responder sem gate quando for pergunta/resposta sem leitura ampla, comando, edicao ou validacao

## [2.17.0] - 2026-06-29

### Adicionado

- **MCP Portability & Local Secrets:** `docs/MCP_PORTABILITY.md`
- Rule: `rules/mcp-portability.md`
- Templates agregados com `context7`, `github`, `clickup`, `mssql` e `mssql-fiscal`

### Alterado

- ClickUp passa a preferir MCP remoto oficial `https://mcp.clickup.com/mcp`
- GitHub passa a preferir MCP remoto `https://api.githubcopilot.com/mcp/`
- MSSQL deixa de depender de path `C:\Users\Danie\...` e usa `npx -y @mcp-collection/mssql-mcp`
- Variaveis MSSQL principal e fiscal ficam separadas

### Preservado

- Nenhum secret real e versionado
- Writes em ClickUp, SQL, GitHub e Docker seguem exigindo pedido explicito/aprovacao

## [2.16.0] - 2026-06-29

### Adicionado

- **Configuration & Hardcode Governance:** `docs/CONFIGURATION_HARDCODE_GOVERNANCE.md`
- Rule: `rules/no-hardcode.md`
- Checklist: `checklists/no-hardcode.md`
- Skill: `hardcode-scanner`
- Workflow: `workflows/hardcode-audit.md`

### Alterado

- Orchestrator detecta hardcode, valor fixo, seeds, modulos, menus, permissoes, status e parametros configuraveis
- Backend, API, React, QA e Code Review passam a validar hardcode funcional
- Working Context registra achados, falso positivo, categoria e destino recomendado
- Feature e Review ganham guardrail anti-hardcode

### Preservado

- Secrets continuam cobertos por Security/Infrastructure Secrets
- Constantes tecnicas e enums de contrato seguem permitidos quando justificados
- Correcoes em projetos consumidores dependem de escopo/aprovacao da missao

## [2.15.0] - 2026-06-29

### Adicionado

- **Execution Reliability:** `docs/EXECUTION_RELIABILITY.md`
- Rules: `execution-loop-control.md`, `frontend-runtime-validation.md`, `regression-boundary.md`
- Checklist: `checklists/frontend-regression.md`
- Working Context: `Attempt Ledger`, `Regression Boundary` e `Frontend Runtime`

### Alterado

- Orchestrator passa a bloquear repeticao de hipotese apos falhas repetidas
- Bug Hunter registra tentativas e hipoteses descartadas
- QA valida Boundary Map, rotas/testes canario e runtime frontend quando aplicavel
- Workflows de bug e product-design passam a exigir guardrails contra loops, cache/porta errada e regressao colateral

### Preservado

- Menor modo seguro continua obrigatorio
- Context Hygiene continua responsavel por contexto poluido
- Execution Reliability nao substitui QA/Validator; define guardrails antes e durante validacao

## [2.14.0] - 2026-06-29

### Adicionado

- **Security Intelligence Domain:** `docs/SECURITY_INTELLIGENCE.md`
- Skills: `security-architect`, `authorization-specialist`, `permission-cache-reviewer`, `threat-modeler`, `si-governance`
- Workflow: `workflows/security-intelligence.md`
- Rules: `security-access-control.md`, `permission-cache.md`, `threat-modeling.md`
- Checklists: `security-architecture.md`, `authorization.md`, `permission-cache.md`, `threat-model.md`

### Alterado

- `security-review` passa a ser revisor geral e delega profundidade para especialistas de Security Intelligence
- Orchestrator detecta SI, permissionamento, nivel de acesso, cache de permissao, threat model, ataques e multi-tenant
- COS registra `security-intelligence` como capability Stable

### Preservado

- Security Intelligence nao implementa automaticamente; o Orchestrator escolhe o menor pipeline seguro
- Regras existentes de security, plugin e RAG permission-aware continuam validas

## [2.13.0] - 2026-06-29

### Adicionado

- **Context Hygiene Protocol:** `rules/context-hygiene.md`
- `Context Health` e `Compacted Snapshot` no Working Context
- Checkpoints do Orchestrator para compactar contexto poluido durante a execucao
- Integracao com Token Economy, processo universal e hierarquia de orquestracao

### Alterado

- Orchestrator passa a avaliar poluicao de contexto em transicoes de fase, antes de validacoes amplas e quando houver outputs longos ou planos substituidos
- Token Economy passa a tratar compactacao de contexto como economia operacional
- FOS atualizado para registrar Context Hygiene como evolucao de Execution Intelligence

### Preservado

- O protocolo nao apaga historico tecnicamente; ele define o contexto operacional ativo
- Skills continuam sem auto-iniciar e nao compactam contexto por conta propria

## [2.12.1] - 2026-06-28

### Adicionado

- **Execution Intelligence baseline:** `MISSION_LEDGER.md`, `SKILL_USAGE.md`, `TOKEN_METRICS.md`, `PROMOTION_CRITERIA.md`
- **Token Budget Policy:** `rules/token-budget-policy.md`
- Fast Path antes do NLME completo para pedidos simples e baixo risco
- End-of-mission token waste review no Orchestrator

### Alterado

- Orchestrator registra sinais uteis de usage/learning/token notes sem auto-mutacao
- FOS governance explicita: observar e recomendar, nunca alterar sem aprovacao
- Framework status/health atualizados com inventario real de skills/workflows/rules/checklists

### Preservado

- NLME/SIL/COS continuam disponiveis para missoes ambiguas, estrategicas ou de maior risco
- Framework nao implementa mudancas em si mesmo sem aprovacao do usuario

## [2.12.0] - 2026-06-26

### Adicionado — Natural Language Mission Engine (NLME)

- **Nova camada:** NLME acima do SIL — linguagem natural → missões autônomas
- **Skills:** mission-translator, mission-builder, prompt-builder
- **Mecanismos:** Goal Recognition, Mission Confidence, Autonomous Planning, Natural Commands
- **Workflow:** `natural-language-mission.md`
- **Docs:** Natural-Language-Missions, Mission-Translator, Goal-Recognition, Prompt-Builder, Mission-Catalog, Natural-Commands, Autonomous-Planning, Mission-Confidence
- **Rules:** natural-language-mission-engine, goal-recognition, mission-confidence
- **Templates:** mission/mission-brief, structured-prompt, nlme-first-response
- **Checklist:** nlme-mission · **Examples:** natural-language-missions
- **Capability COS:** natural-language-mission-engine (Stable)

### Alterado

- SIL recebe Mission Package do NLME (refina, não substitui)
- Orchestrator: pipeline NLME antes de classificação legada
- Mission Recognition estendido com exemplos vNext
- Strategic Mission workflow integrado ao NLME
- AGENTS.md, README, token-economy, Strategic-Intelligence-Layer

### Preservado

- Todas as skills, workflows e interfaces públicas existentes
- Classificação legada Orchestrator via `legacy_demand_type`
- COS, FOS, domínios e plugins intactos

## [2.11.0] - 2026-06-26

### Adicionado

- **MCP Readiness & Connector Implementation**
- `MCP_SERVER_CATALOG.md`, `MCP_READINESS_AUDIT.md`, `PLUGIN_STATUS_POLICY.md`
- Conectores por plugin prioritário: PERMISSIONS, USAGE, HEALTH, ENV.example, Cursor/Codex examples
- **Project MCP Profiles:** `projects/{umbra,irisys,rifsmart}/mcp/`
- `.cursor/mcp.example.json`, `.codex/config.example.toml`
- **Skill:** mcp-discovery-specialist
- **Workflow:** mcp-mission.md · **Rule:** mcp-security.md
- **docs/MCP_GOVERNANCE.md**

### Alterado

- sentry-plugin → **active** (read-only)
- sqlserver, github, docker → **under-review**
- postgres, powerbi, clickup: conectores draft
- PLUGIN_HEALTH, mcps registry, PROJECT_MCP umbra

### Preservado

- Sem credenciais reais; sem conexão a serviços

## [2.10.0] - 2026-06-26

### Adicionado

- **Capability Operating System (COS)** — núcleo de administração de capabilities
- Estrutura COS: `registry/`, `roadmap/`, `implemented/`, `planned/`, `templates/`, `documentation/`
- **CAPABILITY_STATUS**, **CAPABILITY_HEALTH**, **CAPABILITY_REPORT**, **CAPABILITY_ROADMAP**
- **CAPABILITY_CATEGORIES** (22 categorias)
- Lifecycle estendido: Idea → Analysis → Planned → Approved → ...
- **Skills:** capability-builder, capability-evaluator, capability-discovery
- **capability-manager** evoluído (nunca auto-implementar)
- **PROJECT_CAPABILITIES.md** (umbra, irisys, rifsmart)
- **Capability Intelligence** no SIL
- Regra: **plugin exige capability pai**
- Knowledge: `knowledge/capabilities/`
- 14 domain capabilities registradas como Stable

### Alterado

- Registry canônico em `capabilities/registry/`
- Framework Capability Mission reforçada (framework-only)
- Hierarquia: Capabilities → SIL → Orchestrator → Domains → Skills → Projetos

### Preservado

- RAG Intelligence Ready v1.0.0
- Nenhuma skill removida; zero implementação em produtos

## [2.9.0] - 2026-06-26

### Adicionado

- **Capability Architecture** — tecnologias nascem como capabilities reutilizáveis
- **RAG Intelligence** (Ready v1.0.0) — assistentes baseados em conhecimento próprio
- Estrutura `capabilities/` com registry, lifecycle, template
- **22 skills:** capability-manager, capability-resolver, rag-orchestrator + 19 especialistas RAG
- **9 rules** `rules/rag/`, **8 checklists** `checklists/rag/`, **templates** `templates/rag/`
- **10 workflows** `workflows/rag/` + `capability-mission.md`
- **11 knowledge articles** `knowledge/rag/`
- Capabilities Planned: ocr, vision, voice, memory, agents, evaluation
- **Documentação:** `docs/CAPABILITY_ARCHITECTURE.md`, `docs/RAG_INTELLIGENCE.md`
- **CAPABILITY_HEALTH.md**

### Alterado

- Orchestrator integra Capability Resolver (passo 2g)
- Knowledge Hub estendido com domínio RAG

### Preservado

- Nenhuma skill removida; knowledge-engine distinto de knowledge-architect
- **Framework-only** — zero implementação em Umbra, Irisys, SmartRifa

## [2.8.0] - 2026-06-26

### Adicionado

- **Plugin Architecture & Integration Packs** — extensibilidade por pacotes independentes
- Estrutura `plugins/` com policy, registry, template, lifecycle e examples
- **11 plugins iniciais (draft):** github, postgres, sqlserver, powerbi, clickup, sentry, docker, supabase, firebase, azure, aws
- **Skills:** plugin-manager, plugin-resolver, plugin-builder
- **Documentação:** `docs/PLUGIN_ARCHITECTURE.md`
- **Workflow:** `workflows/plugin-mission.md`
- **Rule:** `rules/plugin-policy.md`
- **Checklist:** `checklists/plugin-health.md`
- **Plugin Health:** `framework/operating-system/health/PLUGIN_HEALTH.md`
- **Project Registry:** `PROJECT_PLUGINS.md` por projeto (umbra, irisys, rifsmart)

### Alterado

- Orchestrator integra Plugin Resolver em missões com integração externa
- Infrastructure Intelligence consulta plugins antes de sugerir conexões
- Integration Resolver delega mapeamento serviço → plugin ao Plugin Resolver
- Project Registry documenta associação de plugins por projeto

### Preservado

- Núcleo do framework intacto — nenhuma skill existente removida
- Plugins em draft — integração MCP real permanece backlog

## [2.7.0] - 2026-06-26

### Adicionado

- **Product & Design Intelligence Domain** — qualidade de interface implementável (UX, UI, Design System)
- **Design Modes:** LEGACY · HYBRID · GREENFIELD (`docs/DESIGN_MODES.md`)
- **Design DNA** — `templates/design/design-dna.md`, `design-system/design-dna-default.md`
- **design-system/** — tokens: cores, tipografia, spacing, componentes, dark/light
- **15 skills:** product-designer, ux-researcher, ux-designer, ui-designer, design-system, visual-designer, mobile-designer, desktop-designer, interaction-designer, component-library, benchmark-specialist, design-reviewer, product-aesthetic-director, report-designer, accessibility
- **Artefatos:** `rules/design/`, `checklists/design/`, `templates/design/`, `examples/design/`
- **Documentação:** `DESIGN_INTELLIGENCE.md`, `DESIGN_GUIDE.md`, `DESIGN_SYSTEM.md`, `DESIGN_MODES.md`, `PRODUCT_DESIGN.md`
- **Workflow:** `workflows/product-design.md`
- Gate estético: notas 0–10; entrega bloqueada se dimensão < 8
- **context/design-dna.md** — exemplo Umbra (overlay consumidor)

### Alterado

- Orchestrator integra Product & Design sem remover SIL, FOS, Infrastructure nem Growth & Brand
- **dashboard-designer** evoluída (BI, KPIs, resumo executivo)

### Preservado

- Skills legadas `ux`, `mobile-ux`, `report-ux-reviewer`
- Domínios v2.1–v2.6 intactos

## [2.6.0] - 2026-06-26

### Adicionado

- **Infrastructure Intelligence** - novo dominio para projetos, repositorios, bancos, servicos, APIs, filas, storage, cloud, MCPs, ambientes, dependencias e conexoes.
- Estrutura `infrastructure/` com `projects/`, `registry/`, `catalog/`, `services/`, `repositories/`, `databases/`, `mcp/`, `providers/`, `cloud/`, `monitoring/`, `queues/`, `storage/`, `apis/`, `integrations/`, `environments/`.
- Project Registry para `irisys`, `umbra` e `rifsmart`.
- Infrastructure Registry global para projects, repositories, databases, services, providers, cloud, queues, storage, APIs, MCPs, integrations e connections.
- Skills: `infrastructure-discovery`, `project-scanner`, `project-resolver`, `integration-resolver`.
- Rules/checklists/templates de infraestrutura e secrets.
- Knowledge Hub de infraestrutura: infrastructure, git, cloud, mcp, docker, kubernetes, apis, queues, storage, providers e monitoring.

### Segurança

- Credenciais reais nunca devem ser armazenadas.
- Usar placeholders, environment variables, `.env.example` ou Secret Managers.

### Alterado

- Orchestrator, AGENTS, README, Architecture e workflow index reconhecem Infrastructure Missions.
- FOS passa a registrar evolucao de infraestrutura em status, roadmap, implemented, learning, report e metrics.

## [2.5.0] - 2026-06-26

### Adicionado

- **Framework Operating System (FOS)** - sistema operacional de governanca do proprio framework.
- Estrutura `framework/operating-system/` com roadmap, backlog, ideas, implemented, under-review, rejected, decisions, learning, metrics, patterns, anti-patterns, retrospectives, releases, versions, knowledge, history, reports, health e governance.
- Documentos vivos: `FRAMEWORK_STATUS.md`, `FRAMEWORK_HEALTH.md`, `ROADMAP.md`, `BACKLOG.md`, `IDEAS.md`, `IMPLEMENTED.md`, `UNDER_REVIEW.md`, `REJECTED.md`, `DECISIONS.md`, `CHANGELOG.md`, `LEARNING.md`, `RETROSPECTIVES.md`, `PATTERNS.md`, `ANTI_PATTERNS.md`, `RECOMMENDATIONS.md`, `FRAMEWORK_METRICS.md`, `FRAMEWORK_REPORT.md`, `NEXT_STEPS.md`, `VERSION.md`.
- Skills de governanca: `framework-reviewer`, `framework-optimizer`, `pattern-extractor`, `anti-pattern-detector`, `recommendation-engine`.
- Workflow `framework-operating-system.md`.
- Rules, checklists e templates para governanca, health, dashboard, decisions e recommendations.

### Alterado

- AGENTS, README, Architecture, Orchestrator e workflow index passam a reconhecer perguntas naturais sobre saude, roadmap, evolucao e recomendacoes do framework.
- Framework version atualizado para 2.5.0.

### Governanca

- FOS registra, mede, audita e recomenda.
- FOS nunca implementa automaticamente.
- Toda mudanca no framework depende de aprovacao do usuario.

## [2.4.0] - 2026-06-26

### Adicionado

- **Strategic Intelligence Layer (SIL)** - nova camada acima do Master Orchestrator para transformar linguagem natural em Missoes Estrategicas.
- **Mission System:** Mission Types, Mission Recognition, Mission Planner, Mission Modes, Mission Memory e Mission Score.
- **Continuous Evolution** - backlog sugerido ao fim de cada mission com oportunidades, melhorias, dividas tecnicas, features e evolucoes de UX/produto.
- **Documentacao SIL:** `docs/Strategic-Intelligence-Layer.md`, `docs/Missions.md`, `docs/Mission-Recognition.md`, `docs/Mission-Modes.md`, `docs/Continuous-Evolution.md`.
- **Artefatos de mission:** `templates/mission/`, `checklists/mission-recognition.md`, `checklists/continuous-evolution.md`, `rules/strategic-intelligence-layer.md`.
- **Workflow:** `workflows/strategic-mission.md`.
- **Exemplo:** `examples/strategic-mission.md`.

### Alterado

- **AGENTS.md, README, ARCHITECTURE, Orchestrator e workflows** atualizados para posicionar o SIL acima do Master Orchestrator.
- **Working Context** expandido com Mission Memory.
- **Final response template** expandido com Mission Report e Continuous Evolution quando aplicavel.

### Preservado (compatibilidade)

- O Master Orchestrator continua sendo o unico executor operacional.
- O SIL nao implementa codigo, nao chama skills diretamente e nao altera arquivos.
- Todas as skills, modos e dominios v2.3 permanecem preservados.

## [2.3.0] - 2026-06-26

### Adicionado

- **Product Excellence** - padrao minimo para UX, UI, mobile, desktop, performance, conversao, clareza, produtividade, escalabilidade e consistencia.
- **Knowledge Hub** em `knowledge/` com boas praticas resumidas por area.
- **Knowledge Engine** - skill e documentacao para consultar automaticamente o Knowledge Hub conforme a demanda.
- **Benchmark Intelligence** - comparacao por principios com referencias modernas sem copiar layouts ou identidade.
- **Project Style Analyzer** - analise de Design System, UI library, CSS framework, identidade, tema, tipografia, paleta e modo visual.
- **Product Evolution** - quick wins, melhorias de curto/medio prazo, iniciativas estrategicas, roadmap, impacto, esforco e priorizacao.
- **18 skills novas:** project-style-analyzer, knowledge-engine, benchmark-intelligence, product-excellence, product-evolution-planner, brand-identity-manager, brand-voice-manager, brand-consistency-manager, headline-specialist, cta-specialist, microcopy-specialist, faq-specialist, storytelling-specialist, trust-builder, growth-strategist, asset-curator, open-source-asset-finder, visual-consistency-reviewer.

### Alterado

- **Growth & Brand Intelligence** expandido para Growth Intelligence, Brand Intelligence, Knowledge Hub, Benchmark Intelligence e Product Excellence.
- **Workflow marketing** evoluido para fluxo inteligente: Project Style Analyzer -> Knowledge Engine -> Brand/Copy/UX/Assets/SEO -> Frontend -> Reviewers -> Product Excellence -> QA.
- **Product Audit** expandido com Design System, Product Market Fit e Escalabilidade, e regra de melhoria automatica para categorias abaixo de 8.
- **Orchestrator, AGENTS, README, docs, rules e working-context** atualizados para operar como plataforma completa de engenharia de produto.

### Preservado (compatibilidade)

- Todas as skills e artefatos v2.2.
- Dominio Growth & Brand Intelligence mantido; novas capacidades foram adicionadas incrementalmente.

## [2.2.0] - 2026-06-26

### Adicionado

- **Growth & Brand Intelligence** - novo dominio logico para branding, copywriting, marketing, SEO, conversao e assets.
- **16 skills novas:** brand-strategist, content-strategist, copywriter, ux-writer, landing-page-specialist, seo-specialist, asset-intelligence, image-curator, illustration-curator, icon-curator, logo-manager, image-optimizer, brand-reviewer, marketing-reviewer, conversion-optimizer, social-proof-specialist.
- **Workflow de marketing:** `workflows/marketing.md` para landing pages, sites, paginas publicas, copy, SEO, assets e Product Audit.
- **Artefatos de marketing:** `templates/marketing/`, `checklists/marketing/`, `rules/marketing/` e `examples/marketing-growth-brand.md`.
- **Documentacao:** `docs/GROWTH_BRAND_INTELLIGENCE.md`.
- **Product Audit Growth & Brand:** categorias Copy, Brand, Marketing, Conversao, Landing Page, SEO, Assets, Comunicacao, Identidade Visual e Tom de Voz com nota 0-10.

### Alterado

- **Orchestrator** - deteccao de dominio Growth & Brand Intelligence e fluxo automatico para landing pages, sites, paginas publicas, marketing, onboarding e assets.
- **AGENTS.md, README, docs e workflows** - registros atualizados para o novo dominio sem remover skills existentes.

### Preservado (compatibilidade)

- Todas as skills, workflows e interfaces publicas v2.1.
- Bootstrap `AGENTS.md` -> `skills/orchestrator/SKILL.md`.
- Politica de skills sob demanda e economia de tokens.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).
Versionamento segue [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [2.1.0] — 2026-06-25

### Adicionado

- **Data Intelligence Domain** — `data-orchestrator` como sub-orquestrador de dados
- **22 skills novas:** data-analyst, business-data-analyst, sql-architect, query-optimizer, dba-reviewer, data-validator, powerbi-specialist, dax-specialist, dashboard-designer, report-ux-reviewer, etl-specialist, semantic-layer-specialist, data-quality-reviewer, task-analyst, requirement-reviewer, acceptance-criteria-reviewer, business-rule-mapper, impact-analysis, hybrid-flow-planner, cross-domain-decision-maker, report-implementation-planner
- **Fluxos híbridos** — dev + dados + BI (`docs/HYBRID_FLOWS.md`, `workflows/hybrid-flows.md`)
- **Camada semântica** — `context/semantic-layer/` (templates CTe, MDFe, financeiro, ...)
- **Artefatos de dados:** `templates/data/` (12), `checklists/data/` (12), `rules/data/` (9), `examples/data/` (7)
- **Workflows de dados:** data-sql, data-powerbi, data-report-frontend, data-divergence, data-procedure
- **Documentação:** `docs/DATA_INTELLIGENCE.md`, `docs/HYBRID_FLOWS.md`, `docs/USING_IN_PROJECTS.md`, `docs/UPDATE_FRAMEWORK.md`
- **Resposta para dados:** `templates/data/final-response-data.md`
- Tipo de demanda `hybrid` no Orchestrator

### Alterado

- **Orchestrator** — detecção de domínios, Hybrid Flow, invocação de data-orchestrator
- **Working Context** — seção Data Intelligence (tabelas, procedures, divergências, ...)
- **Skill `data`** — evoluída como compatibilidade; roteamento para especializadas
- **Workflow `data.md`** — pipeline via data-orchestrator
- **AGENTS.md** e **README.md** — domínios e skills de dados

### Preservado (compatibilidade)

- Todas as skills v2.0 (39+) — nenhuma removida ou renomeada
- Bootstrap `AGENTS.md` → `orchestrator/SKILL.md`
- Pasta `Personal-AI/` e estrutura de diretórios
- Modos Fast / Standard / Review / Technical Council

### Decisões de não-duplicação

| Pedido | Decisão |
|--------|---------|
| data-analyst | Nova skill; `data` evoluída como legado/roteamento |
| etl-specialist | Nova skill; escopo ETL extraído de `data` |
| impact-analysis | Nova skill; complementa `risk-reviewer` (dependências de dados) |
| cross-domain-decision-maker | Nova skill; complementa `decision-maker` (trade-offs híbridos) |
| report-implementation-planner | Nova skill; especializa `implementation-planner` para relatórios |
| acceptance-criteria-reviewer | Nova skill; complementa `product-owner` (critérios testáveis com dados) |
| task-analyst | Nova skill; complementa `support` (análise estruturada de task) |

## [2.0.0] — 2026-06-25

### Adicionado

- **AI Engineering Framework** — nome oficial do produto (compatível com pasta `Personal-AI/`)
- Modos hierárquicos: Fast, Standard, Review, Technical Council
- Skills de governança: `critic`, `validator`, `risk-reviewer`, `decision-maker`, `implementation-planner`
- Working Context (`context/working-context.md`)
- Regra transversal `rules/hierarchical-orchestration.md`
- Processo Technical Council (`workflows/technical-council.md`, `workflows/modes.md`)
- Documentação de instalação via Git Submodule (`docs/INSTALL.md`)
- Documentação de arquitetura (`docs/ARCHITECTURE.md`)
- Documentação de versionamento (`docs/VERSIONING.md`)
- Templates de contexto por projeto (`context/_template/`)
- `VERSION` e este `CHANGELOG.md`
- Exemplo `examples/hierarchical-orchestration.md`

### Alterado

- Orchestrator reescrito como único contato com o usuário
- `rules/token-economy.md` — política global reforçada
- `workflows/_process.md` — fases Classificar e Escolher modo
- Todos os workflows mapeados para modos sugeridos
- Todas as skills — seção Orquestração hierárquica
- `templates/final-response.md` — campo Modo utilizado
- `skill-builder` — artefatos obrigatórios expandidos

### Preservado (compatibilidade)

- Estrutura de diretórios `Personal-AI/` (consumidores existentes)
- Paths `skills/`, `rules/`, `workflows/`, `templates/`, `checklists/`
- Bootstrap via `AGENTS.md` + `skills/orchestrator/SKILL.md`
- Skills técnicas e workflows existentes (evoluídos, não removidos)
- Contexto Umbra em `context/` (exemplo de consumidor)

## [1.0.0] — anterior

- Personal AI Framework inicial: orchestrator, 30+ skills, workflows, rules, templates
