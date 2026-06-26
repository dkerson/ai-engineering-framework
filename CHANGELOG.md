# Changelog — AI Engineering Framework

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
