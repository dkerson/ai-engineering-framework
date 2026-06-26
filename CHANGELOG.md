# Changelog — AI Engineering Framework

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
