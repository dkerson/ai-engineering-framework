# AI Engineering Framework — AGENTS.md

> **Nome oficial:** AI Engineering Framework (v2.x)
> **Alias legado:** Personal AI Framework — pasta `Personal-AI/` preservada para compatibilidade.
>
> Ponto de entrada universal para agentes Codex/Cursor. O usuário **nunca** escolhe skills manualmente.

## Bootstrap obrigatório

0. **Natural Language Mission Engine (NLME):** interpretar linguagem natural → Mission Package → Structured Prompt (interno)
0a. **Strategic Intelligence Layer (SIL):** refinar Mission Brief a partir do NLME
1. **Sempre** iniciar lendo `skills/orchestrator/SKILL.md`
2. O **Orchestrator** é o único agente que conversa com o usuário
3. Nenhuma skill inicia execução por conta própria — todo fluxo passa pelo Orchestrator
4. Respeitar `rules/strategic-intelligence-layer.md`, `rules/hierarchical-orchestration.md` e `rules/token-economy.md`
5. Seguir o processo: Entender → Classificar → Escolher modo → Planejar → Investigar → Implementar → Validar → Revisar → Entregar
6. Manter **Working Context** durante a execução (`context/working-context.md`)
7. Terminar com `templates/final-response.md`

SIL nunca implementa, nunca chama skills diretamente e nunca altera arquivos. Ele entrega um Mission Brief ao Orchestrator.

## Instalação em projetos

Ver `docs/INSTALL.md` (Git Submodule recomendado). Caminhos: `.ai/`, `ai-engineering-framework/` ou `Personal-AI/` (legado).

## Arquitetura hierárquica

```
Usuário (linguagem natural)
              ↓
    Natural Language Mission Engine (NLME)
              ↓
    Strategic Intelligence Layer (Mission Brief)
              ↓
    Capability Operating System (COS)
              ↓
    Framework Operating System (governanca do framework — quando aplicavel)
              ↓
    Orchestrator (executor operacional)
              ↓
    [Fast | Standard | Review | Technical Council]
              ↓
    Domínios: Development · Data Intelligence · Infrastructure Intelligence · Growth & Brand Intelligence · Product Excellence · Knowledge Hub · Framework Operating System · Business/Operations · QA/Validation
              ↓
    hybrid-flow-planner / data-orchestrator (quando aplicável)
              ↓
    Skills sob demanda (nunca auto-iniciam)
              ↓
    Working Context → descartado ao finalizar
```

Detalhes: `docs/Natural-Language-Missions.md` · `docs/ARCHITECTURE.md` · `docs/Framework-Operating-System.md` · `docs/Strategic-Intelligence-Layer.md` · `docs/Missions.md` · `docs/Infrastructure-Intelligence.md` · `docs/Project-Registry.md` · `docs/DATA_INTELLIGENCE.md` · `docs/GROWTH_BRAND_INTELLIGENCE.md` · `docs/KNOWLEDGE_HUB.md` · `docs/PRODUCT_EXCELLENCE.md` · `docs/HYBRID_FLOWS.md` · `workflows/modes.md`

## Estrutura do framework

```
├── AGENTS.md          ← bootstrap
├── VERSION            ← semver
├── CHANGELOG.md
├── README.md
├── docs/              ← INSTALL, ARCHITECTURE, VERSIONING
├── skills/            ← orchestrator + especializadas
├── rules/
├── templates/
├── templates/mission/ ← Mission Brief, Report, Continuous Evolution
├── checklists/
├── workflows/
├── knowledge/         ← boas práticas resumidas por área
├── design-system/       ← tokens UI (Product & Design Intelligence v2.7+)
├── framework/operating-system/ ← governanca viva do framework
├── infrastructure/    ← registry de projetos e infraestrutura
├── plugins/           ← Plugin Architecture & Integration Packs (v2.8+)
├── capabilities/      ← Capability Operating System (COS) v2.10+ · RAG v2.9+
├── context/           ← overlay do projeto consumidor (ver context/README.md)
│   └── semantic-layer/  ← camada semântica Otus/Irisys (templates)
├── templates/data/    ← templates de dados/BI
├── templates/design/  ← Design DNA, interface spec, aesthetic review
├── templates/marketing/ ← templates Growth & Brand
├── checklists/data/
├── checklists/design/
├── checklists/marketing/
├── rules/data/
├── rules/design/
├── rules/marketing/
├── examples/data/
└── examples/marketing-growth-brand.md
```

## Hierarquia de precedência

1. Instruções explícitas do usuário
2. `AGENTS.md` do **projeto consumidor**
3. Este arquivo (`AGENTS.md` do framework)
4. Orchestrator (modo e pipeline)
5. Skills invocadas pelo Orchestrator
6. `rules/` e `context/` do projeto consumidor

## Modos de operação

| Modo | Uso | Pipeline resumido |
|------|-----|-------------------|
| **Fast** | Perguntas, docs, consultas, alteração mínima | Orchestrator sozinho |
| **Standard** | Bug/melhoria/feature pequena | Context → Técnica → QA |
| **Review** | Estrutural, auth, DB, API, integração, performance | Context → Especialistas → Critic → Validator |
| **Technical Council** | Arquitetura, produção, segurança, incidente | Conselho → Decision Maker → Planner → Validator |

## Tipos de demanda

`natural-language-mission` · `framework-operating-system` · `strategic-mission` · `infrastructure-mission` · `plugin-mission` · `capability-mission` · `mcp-mission` · `bug` · `incident` · `feature` · `refactor` · `review` · `documentation` · `functional-spec-doc` · `process-doc` · `performance` · `database` · `api` · `integration` · `devops` · `testing` · `architecture` · `product` · `ux` · `mobile` · `security` · `data` · `hybrid` · `marketing` · `growth` · `brand` · `audit` · `benchmark` · `product-excellence` · `commercial` · `finance` · `deployment` · `support`

Mapeamento: `workflows/_index.md`

## Skills — núcleo e governança

| Skill | Papel |
|-------|-------|
| **Orchestrator** | Único contato; modos; Working Context |
| Context Builder | Contexto mínimo do projeto |
| **Critic** | Criticar solução — nunca implementa |
| **Validator** | Prontidão da entrega |
| **Risk Reviewer** | Classificação de risco |
| **Decision Maker** | Consolida conselho — nunca fala com usuário |
| **Implementation Planner** | Plano técnico executável |
| **Skill Builder** | Gerar novas skills no padrão |

### Natural Language Mission Engine (v2.12+)

| Skill / Conceito | Papel |
|------------------|-------|
| **mission-translator** | Traduz frase humana → Translation Brief |
| **Goal Recognition** | Objetivo real vs texto literal |
| **Mission Recognition** | Tipo de missão e domínios (ver `docs/Mission-Recognition.md`) |
| **Natural Commands** | Verbos naturais → missões (`docs/Natural-Commands.md`) |
| **mission-builder** | Mission Package, roadmap, confidence |
| **prompt-builder** | Structured Prompt interno (usuário nunca vê) |
| **Mission Confidence** | Score antes de executar (`docs/Mission-Confidence.md`) |
| **Autonomous Planning** | Seleção automática de skills/workflows/plugins |

NLME nunca implementa, nunca altera código, nunca expõe prompt estruturado. Ver `docs/Natural-Language-Missions.md` · `workflows/natural-language-mission.md`.

### Strategic Intelligence Layer (v2.4+)

| Conceito | Papel |
|----------|-------|
| Strategic Intelligence Layer | Refina Mission Brief a partir do NLME |
| Mission Recognition | Identifica objetivo, contexto, risco, impacto, dominios e mission type |
| Mission Planner | Define ordem estrategica, quick wins, riscos e necessidade de Council |
| Mission Memory | Preserva objetivo, decisoes, hipoteses, roadmap, validacoes e quick wins |
| Continuous Evolution | Sugere backlog futuro ao fim da mission |

O SIL nao implementa, nao chama skills e nao altera arquivos. Ele entrega ao Master Orchestrator uma Mission pronta para execucao.

### Framework Operating System (v2.5+)

| Conceito | Papel |
|----------|-------|
| Framework Operating System | Administra a evolucao do proprio framework |
| Framework Reviewer | Revisa saude, redundancia, cobertura e complexidade |
| Framework Optimizer | Recomenda otimizacoes sem alterar arquivos |
| Pattern Extractor | Sugere padroes apos evidencia recorrente |
| Anti Pattern Detector | Registra duplicacao, token waste e conflitos |
| Recommendation Engine | Sugere novas skills, workflows, templates, rules, checklists, docs, missions, dominios ou patterns |

O FOS registra, mede, audita e recomenda. Nunca implementa automaticamente; toda mudanca depende de aprovacao do usuario.

### Infrastructure Intelligence (v2.6+)

| Skill | Papel |
|-------|-------|
| infrastructure-discovery | Descobre sinais de infraestrutura sem alterar codigo |
| project-scanner | Responde perguntas usando registries |
| project-resolver | Resolve projeto, ambiente, banco, Git, servico e MCP |
| integration-resolver | Planeja integracoes, MCPs, servicos e skills |

Registries: `infrastructure/registry/` e `infrastructure/projects/`. Credenciais reais nunca sao armazenadas.

### Plugin Architecture (v2.8+)

| Skill | Papel |
|-------|-------|
| plugin-manager | Cadastra, atualiza, lista, desativa e valida plugins |
| plugin-resolver | Seleciona plugin na missão; verifica permissões e riscos |
| plugin-builder | Cria novos plugins no padrão; registra no Registry e FOS |

Registro: `plugins/PLUGIN_REGISTRY.md`. Integrações externas devem ser plugins independentes — ver `docs/PLUGIN_ARCHITECTURE.md`.

### Capability Operating System (v2.10+)

| Skill | Papel |
|-------|-------|
| capability-manager | COS: criar, atualizar, versionar, registrar, planejar — nunca auto-implementar |
| capability-builder | Criar novas capabilities no padrão COS |
| capability-evaluator | Skill? Workflow? Plugin? Rule? Nova Capability? |
| capability-discovery | Identificar oportunidades; registrar only |
| capability-resolver | Selecionar capability na missão |

Registro: `capabilities/registry/`. **Capability-first:** tecnologia nova → Capability → projeto. Ver `docs/CAPABILITY_OPERATING_SYSTEM.md`.

### MCP Governance (v2.11+)

| Skill | Papel |
|-------|-------|
| mcp-discovery-specialist | Discovery MCP por projeto; sugere plugins; classifica risco |
| plugin-manager | Promoção draft/under-review/active com checklist MCP |

Ver `docs/MCP_GOVERNANCE.md` · `infrastructure/registry/MCP_SERVER_CATALOG.md`.

### Data Intelligence (v2.1+)

| Skill | Papel |
|-------|-------|
| **data-orchestrator** | Sub-orquestrador de domínio de dados |
| data-analyst | Análise e interpretação de dados |
| business-data-analyst | Negócio → métricas e relatórios |
| sql-architect | Design/review SQL, views, procedures |
| query-optimizer | Performance de queries |
| dba-reviewer | Segurança de alterações em banco |
| data-validator | Consistência banco/API/tela/BI |
| powerbi-specialist · dax-specialist | Power BI e DAX |
| dashboard-designer · report-ux-reviewer | Dashboards e UX de relatório |
| etl-specialist | Pipelines ETL |
| semantic-layer-specialist | Camada semântica |
| data-quality-reviewer | Qualidade de dados |

### Task / Requirement / Hybrid (v2.1+)

| Skill | Papel |
|-------|-------|
| task-analyst | Análise de task/ticket |
| requirement-reviewer | Completude de requisitos |
| acceptance-criteria-reviewer | Critérios de aceite testáveis |
| business-rule-mapper | Regras de negócio → artefatos |
| impact-analysis | Impacto de mudanças em dados |
| hybrid-flow-planner | Plano para fluxos multi-domínio |
| cross-domain-decision-maker | Decisão entre domínios |
| report-implementation-planner | Plano de relatório end-to-end |

Skill legada `data` preservada — roteia para especializadas. Lista completa: `workflows/_index.md` · `docs/DATA_INTELLIGENCE.md`.

### Growth & Brand Intelligence (v2.2+)
| Skill | Papel |
|-------|-------|
| brand-strategist | Tom de voz, posicionamento e personalidade |
| project-style-analyzer | Design System, UI library, tema, identidade e modo visual |
| knowledge-engine | Consulta Knowledge Hub conforme demanda |
| content-strategist | Arquitetura de conteudo e narrativa |
| copywriter | Headlines, beneficios, CTAs, FAQ e mensagens de conversao |
| ux-writer | Microcopy, mensagens internas, onboarding e estados |
| landing-page-specialist | Estrutura de landing pages modernas |
| seo-specialist | SEO, metadados, headings e Open Graph |
| asset-intelligence | Decisao automatica do tipo de asset mais adequado |
| asset-curator · open-source-asset-finder | Curadoria e recomendacao de fontes abertas |
| image-curator · illustration-curator · icon-curator | Curadoria visual por tipo de asset |
| logo-manager · image-optimizer | Logos, favicons, previews sociais e otimizacao |
| brand-reviewer · marketing-reviewer · conversion-optimizer | Revisao de marca, comunicacao e conversao |
| social-proof-specialist | Clientes, cases, depoimentos, numeros e autoridade |
| benchmark-intelligence · product-excellence · product-evolution-planner | Benchmark por principios, auditoria e roadmap evolutivo |

Fluxo automatico para landing page, site, pagina institucional, tela publica, portal, home publica, marketing, onboarding e assets: ver `workflows/marketing.md` e `docs/GROWTH_BRAND_INTELLIGENCE.md`.

Fluxo automatico para "analise esse produto", "faca uma auditoria", "modernize o sistema" e pedidos similares: ver `workflows/product-excellence.md`, `docs/PRODUCT_EXCELLENCE.md` e `docs/PRODUCT_EVOLUTION.md`.

### Product & Design Intelligence (v2.7+)

| Skill | Papel |
|-------|-------|
| **product-designer** | Objetivo de produto e escopo de UI |
| ux-researcher | Jobs-to-be-done, contexto de uso |
| ux-designer | Fluxos, wireframes, estados |
| ui-designer | Layout, componentes, tokens visuais |
| **design-system** | Tokens e padrões DS (`design-system/`) |
| visual-designer | Composição e hierarquia estética |
| mobile-designer · desktop-designer | Layout por plataforma |
| interaction-designer | Microinterações e feedback |
| component-library | Inventário e reuso de componentes |
| benchmark-specialist | Princípios de qualidade (sem cópia) |
| design-reviewer | Checklist de interface |
| **product-aesthetic-director** | Scores 0–10; gate ≥ 8 |
| report-designer | Relatórios web/PDF/Excel/PBI |
| accessibility | WCAG e a11y |
| dashboard-designer · report-ux-reviewer | Dashboards/BI (evoluídas) |

**Design Modes:** LEGACY · HYBRID · GREENFIELD — `docs/DESIGN_MODES.md`. **Nunca** alterar identidade visual sem pedido explícito. Complementa Growth & Brand (`project-style-analyzer`). Detalhes: `docs/DESIGN_INTELLIGENCE.md`.

### Knowledge Hub e Product Excellence (v2.3+)

| Conceito | Papel |
|----------|-------|
| Knowledge Hub | Biblioteca interna em `knowledge/` com boas praticas resumidas |
| Knowledge Engine | Seleciona areas relevantes antes de planejar |
| Benchmark Intelligence | Compara principios com referencias modernas sem copiar |
| Product Excellence | Padrao minimo de qualidade de produto |
| Product Evolution | Roadmap apos auditoria, com impacto/esforco/prioridade |

## Technical Council

Processo (não skill): `workflows/technical-council.md`

## Economia de tokens

- Menor modo seguro
- Working Context — sem releitura
- Council: máx. 150 palavras/skill; usuário vê só decisão consolidada

`rules/token-economy.md` · `rules/hierarchical-orchestration.md`

## Resposta final

Resumo · Diagnóstico · Plano · **Modo** · Skills · Arquivos · Validações · Resultado · Como testar · Riscos · Próximos passos

Templates: `templates/final-response.md` · `templates/data/final-response-data.md` (demandas de dados/BI)

## Expansão

`skills/skill-builder/SKILL.md` → registrar em `workflows/_index.md` e neste arquivo.
