# AI Engineering Framework

**v2.1** — Biblioteca reutilizável de agentes com **Orquestração Inteligente Hierárquica** para Codex, Cursor e ferramentas baseadas em AGENTS.md. Suporte a **Data Intelligence** (SQL, Power BI, BI) e **fluxos híbridos** (dev + dados + relatórios Umbra/Irisys).

> **Compatibilidade:** este diretório pode chamar-se `Personal-AI/` (legado Umbra), `.ai/` ou `ai-engineering-framework/` — o conteúdo é o mesmo.

## O que é

Framework modular e **agnóstico de projeto**. O Orchestrator é o único agente que conversa com o usuário, escolhe o modo de execução e invoca especialistas somente quando necessário.

```
Usuário ↔ Orchestrator
              ↓
    Fast | Standard | Review | Technical Council
              ↓
    Domínios + Hybrid Flow / Data Orchestrator
              ↓
    Skills sob demanda + Working Context
              ↓
    Resposta consolidada
```

## Princípios

| Princípio | Implementação |
|-----------|---------------|
| Modular | Skills, rules, workflows independentes |
| Reutilizável | Git Submodule em múltiplos projetos |
| Baixo consumo de tokens | Modo mínimo + Working Context |
| Alta qualidade | Critic, Validator, Technical Council |
| Compatível | Codex, Cursor, AGENTS.md |

## Instalação rápida

```bash
git submodule add https://github.com/dkerson/ai-engineering-framework.git .ai
```

No `AGENTS.md` do seu projeto:

```markdown
## AI Engineering Framework
Bootstrap: [.ai/AGENTS.md](.ai/AGENTS.md) → `.ai/skills/orchestrator/SKILL.md`
```

Guia completo: [`docs/INSTALL.md`](docs/INSTALL.md)

## Modos de operação

| Modo | Quando | Pipeline |
|------|--------|----------|
| **Fast** | Perguntas, docs, alteração mínima | Orchestrator |
| **Standard** | Bugs/features pequenas | Context → Técnica → QA |
| **Review** | Auth, DB, API, integração | Context → Especialistas → Critic → Validator |
| **Technical Council** | Arquitetura, produção, incidente | Conselho → Decision Maker → Planner |

Detalhes: [`workflows/modes.md`](workflows/modes.md)

## Documentação

| Documento | Conteúdo |
|-----------|----------|
| [`AGENTS.md`](AGENTS.md) | Bootstrap para agentes |
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | Arquitetura e responsabilidades |
| [`docs/DATA_INTELLIGENCE.md`](docs/DATA_INTELLIGENCE.md) | Domínio de dados/BI/SQL/Power BI |
| [`docs/HYBRID_FLOWS.md`](docs/HYBRID_FLOWS.md) | Fluxos dev + dados + BI |
| [`docs/USING_IN_PROJECTS.md`](docs/USING_IN_PROJECTS.md) | Umbra, Irisys e consumidores |
| [`docs/UPDATE_FRAMEWORK.md`](docs/UPDATE_FRAMEWORK.md) | Atualizar submodule |
| [`docs/INSTALL.md`](docs/INSTALL.md) | Submodule: instalar, atualizar, remover |
| [`docs/VERSIONING.md`](docs/VERSIONING.md) | Semver e tags |
| [`CHANGELOG.md`](CHANGELOG.md) | Histórico de versões |
| [`INTEGRATION.md`](INTEGRATION.md) | Codex, Cursor, alternativas |
| [`context/README.md`](context/README.md) | Contexto por projeto consumidor |

## Stacks suportadas

Node · NestJS · React · Next.js · Flutter · Python · Go · .NET · REST · SQL Server · Power BI · Microserviços

Defina a stack em `context/tech-stack.md` — templates em `context/_template/`.

## Estrutura

```
├── VERSION / CHANGELOG.md
├── docs/
├── skills/         # orchestrator + governança + técnicas
├── rules/
├── workflows/
├── templates/
├── checklists/
├── context/        # overlay do projeto + semantic-layer/
├── templates/data/ # pedidos SQL, relatórios, validação
├── checklists/data/
├── rules/data/
└── examples/data/
```

## Criar nova skill

`skills/skill-builder/SKILL.md` — gera SKILL.md, exemplo, checklist, integração com orchestrator.

## Versão

Ver [`VERSION`](VERSION) — atual: **2.1.0**

## Licença

Uso Otus7 / Douglas — ver repositório para termos.
