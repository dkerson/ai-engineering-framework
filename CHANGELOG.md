# Changelog — AI Engineering Framework

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).
Versionamento segue [Semantic Versioning](https://semver.org/lang/pt-BR/).

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
