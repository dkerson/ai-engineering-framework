# Capability Registry — Registro Canônico (COS)

> Última atualização: 2026-06-26 · Framework v2.10.0

## Campos

Nome · Descrição · Versão · Categoria · Status · Domínios · Skills · Dependências · Projetos · Health Score · Roadmap · Documentação

## Legenda status

`Idea` · `Analysis` · `Planned` · `Approved` · `In Development` · `Ready` · `Stable` · `Deprecated` · `Removed`

---

## Stable — Domínios existentes

### development-intelligence

| Campo | Valor |
|-------|-------|
| Nome | Development Intelligence |
| Versão | 2.0.0 |
| Categoria | Development |
| Status | Stable |
| Descrição | Backend, API, frontend, mobile, database, devops |
| Health Score | 9.0 |
| Projetos | umbra, irisys, rifsmart (via Orchestrator) |
| Documentação | `docs/ARCHITECTURE.md`, skills Development |

### data-intelligence

| Campo | Valor |
|-------|-------|
| Nome | Data Intelligence |
| Versão | 2.1.0 |
| Categoria | Data, Analytics |
| Status | Stable |
| Descrição | SQL, BI, Power BI, ETL, semantic layer, data validation |
| Health Score | 9.0 |
| Skills | data-orchestrator, sql-architect, powerbi-specialist, ... |
| Documentação | `docs/DATA_INTELLIGENCE.md` |

### product-design-intelligence

| Campo | Valor |
|-------|-------|
| Nome | Product & Design Intelligence |
| Versão | 2.7.0 |
| Categoria | Design, Product |
| Status | Stable |
| Descrição | UX, UI, Design System, aesthetic gate |
| Health Score | 8.8 |
| Documentação | `docs/DESIGN_INTELLIGENCE.md` |

### growth-brand-intelligence

| Campo | Valor |
|-------|-------|
| Nome | Growth & Brand Intelligence |
| Versão | 2.2.0 |
| Categoria | Growth, Marketing |
| Status | Stable |
| Descrição | Brand, copy, SEO, landing, assets, conversion |
| Health Score | 8.8 |
| Documentação | `docs/GROWTH_BRAND_INTELLIGENCE.md` |

### infrastructure-intelligence

| Campo | Valor |
|-------|-------|
| Nome | Infrastructure Intelligence |
| Versão | 2.6.0 |
| Categoria | Infrastructure, DevOps |
| Status | Stable |
| Descrição | Project Registry, discovery, MCP governance |
| Health Score | 8.5 |
| Documentação | `docs/Infrastructure-Intelligence.md` |

### plugin-architecture

| Campo | Valor |
|-------|-------|
| Nome | Plugin Architecture |
| Versão | 2.8.0 |
| Categoria | Integration, Plugins |
| Status | Stable |
| Descrição | Pacotes de integração independentes (GitHub, SQL, cloud) |
| Dependências | infrastructure-intelligence |
| Regra COS | **Todo plugin pertence a uma Capability** |
| Health Score | 8.0 |
| Documentação | `docs/PLUGIN_ARCHITECTURE.md`, `plugins/` |

### framework-operating-system

| Campo | Valor |
|-------|-------|
| Nome | Framework Operating System |
| Versão | 2.5.0 |
| Categoria | Architecture |
| Status | Stable |
| Descrição | Governança, health, roadmap, backlog do framework |
| Health Score | 9.0 |
| Documentação | `docs/Framework-Operating-System.md` |

### strategic-intelligence-layer

| Campo | Valor |
|-------|-------|
| Nome | Strategic Intelligence Layer |
| Versão | 2.4.0 |
| Categoria | Architecture |
| Status | Stable |
| Descrição | Mission Brief a partir de linguagem natural |
| Integração COS | Primeira pergunta: Capability existe? |
| Health Score | 9.0 |
| Documentação | `docs/Strategic-Intelligence-Layer.md` |

### knowledge-hub

| Campo | Valor |
|-------|-------|
| Nome | Knowledge Hub |
| Versão | 2.3.0 |
| Categoria | Knowledge |
| Status | Stable |
| Descrição | Biblioteca interna de boas práticas |
| Skills | knowledge-engine |
| Health Score | 8.5 |
| Documentação | `docs/KNOWLEDGE_HUB.md` |

### mission-intelligence

| Campo | Valor |
|-------|-------|
| Nome | Mission Intelligence |
| Versão | 2.12.0 |
| Categoria | Architecture |
| Status | Stable |
| Descrição | Mission types, recognition, memory, continuous evolution — integrado ao NLME |
| Skills | mission-translator, mission-builder, prompt-builder |
| Health Score | 9.0 |
| Documentação | `docs/Missions.md` · `docs/Natural-Language-Missions.md` |

### natural-language-mission-engine

| Campo | Valor |
|-------|-------|
| Nome | Natural Language Mission Engine |
| Versão | 2.12.0 |
| Categoria | Architecture |
| Status | Stable |
| Descrição | Linguagem natural → Translation Brief → Mission Package → Structured Prompt |
| Skills | mission-translator, mission-builder, prompt-builder |
| Health Score | 9.0 |
| Documentação | `docs/Natural-Language-Missions.md` |

### product-excellence

| Campo | Valor |
|-------|-------|
| Nome | Product Audit / Excellence |
| Versão | 2.3.0 |
| Categoria | Product |
| Status | Stable |
| Descrição | Auditoria de produto, scores, quality gate |
| Health Score | 8.5 |
| Documentação | `docs/PRODUCT_EXCELLENCE.md` |

### product-evolution

| Campo | Valor |
|-------|-------|
| Nome | Product Evolution |
| Versão | 2.3.0 |
| Categoria | Product |
| Status | Stable |
| Descrição | Roadmap pós-auditoria |
| Health Score | 8.0 |
| Documentação | `docs/PRODUCT_EVOLUTION.md` |

### continuous-improvement

| Campo | Valor |
|-------|-------|
| Nome | Continuous Improvement |
| Versão | 2.4.0 |
| Categoria | Automation, Architecture |
| Status | Stable |
| Descrição | Continuous Evolution, backlog sugerido pós-mission |
| Health Score | 8.0 |
| Documentação | `docs/Continuous-Evolution.md` |

### capability-operating-system

| Campo | Valor |
|-------|-------|
| Nome | Capability Operating System |
| Versão | 2.10.0 |
| Categoria | Architecture |
| Status | Stable |
| Descrição | Administra todas as capabilities; registry, roadmap, health |
| Skills | capability-manager, capability-builder, capability-evaluator, capability-discovery, capability-resolver |
| Health Score | 8.5 |
| Documentação | `docs/CAPABILITY_OPERATING_SYSTEM.md` |

---

## Ready — Capabilities entregues (framework-only)

### rag — RAG Intelligence

| Campo | Valor |
|-------|-------|
| Nome | RAG Intelligence |
| Versão | 1.0.0 |
| Categoria | AI, Search, Knowledge |
| Status | Ready |
| Descrição | Assistentes com conhecimento próprio: retrieval, citations, guardrails |
| Dependências | knowledge-hub, plugin-architecture (opcional vector DB) |
| Skills | rag-orchestrator + 19 especialistas (ver `capabilities/rag/`) |
| Projetos | Nenhum (consumo futuro) |
| Health Score | 8.2 |
| Roadmap | Stable após 1º projeto consumidor |
| Documentação | `capabilities/rag/`, `docs/RAG_INTELLIGENCE.md` |

---

## Planned / Idea

| ID | Nome | Categoria | Status | Versão prevista |
|----|------|-----------|--------|-----------------|
| ocr | OCR Intelligence | AI, Vision | Planned | 1.0.0 |
| vision | Vision Intelligence | Vision, AI | Idea | TBD |
| voice | Voice Intelligence | Voice, AI | Idea | TBD |
| memory | Memory Intelligence | AI | Planned | 1.0.0 |
| agents | Agents Intelligence | AI, Automation | Idea | TBD |
| evaluation | Evaluation Intelligence | AI, Testing | Planned | 1.0.0 |

Ver `capabilities/planned/` e `roadmap/CAPABILITY_ROADMAP.md`.

---

## Índice por status

| Status | Count | IDs |
|--------|-------|-----|
| Stable | 14 | development, data, product-design, growth-brand, infrastructure, plugin, fos, sil, knowledge-hub, mission, product-excellence, product-evolution, continuous-improvement, cos |
| Ready | 1 | rag |
| Planned | 3 | ocr, memory, evaluation |
| Idea | 3 | vision, voice, agents |

## Plugin → Capability (obrigatório)

| Plugin | Capability responsável |
|--------|------------------------|
| github-plugin | development-intelligence, infrastructure-intelligence |
| sqlserver-plugin | data-intelligence |
| postgres-plugin | data-intelligence, rag |
| powerbi-plugin | data-intelligence |
| sentry-plugin | infrastructure-intelligence |
| docker-plugin | infrastructure-intelligence |
| azure-plugin | infrastructure-intelligence |
| aws-plugin | infrastructure-intelligence |
