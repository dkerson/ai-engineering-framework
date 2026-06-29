# AI Engineering Framework

**v2.14** — Biblioteca reutilizável de agentes com **Natural Language Mission Engine (NLME)**, **Framework Operating System**, **Strategic Intelligence Layer**, **Security Intelligence**, **Context Hygiene**, **Orquestração Inteligente Hierárquica** e domínios especializados para Codex, Cursor e ferramentas baseadas em AGENTS.md.

> **Compatibilidade:** este diretório pode chamar-se `Personal-AI/` (legado Umbra), `.ai/` ou `ai-engineering-framework/` — o conteúdo é o mesmo.

## O que é

Framework modular e **agnóstico de projeto**. O usuário conversa em linguagem natural; o NLME traduz em missões; o SIL refine estrategicamente; o Orchestrator executa.

```
Usuário (linguagem natural)
              ↓
    Natural Language Mission Engine
              ↓
    Strategic Intelligence Layer
              ↓
    Capability Operating System
              ↓
    Orchestrator
              ↓
    Fast | Standard | Review | Technical Council
              ↓
    Domínios + Hybrid Flow / Data Orchestrator / Security Intelligence
              ↓
    Skills sob demanda + Working Context + Context Hygiene
              ↓
    Resposta consolidada
```

## Princípios

| Princípio | Implementação |
|-----------|---------------|
| Modular | Skills, rules, workflows independentes |
| Reutilizável | Git Submodule em múltiplos projetos |
| Baixo consumo de tokens | Modo mínimo + Working Context + Context Hygiene |
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
| [`docs/Framework-Operating-System.md`](docs/Framework-Operating-System.md) | Governanca, saude, roadmap e recomendacoes do framework |
| [`rules/context-hygiene.md`](rules/context-hygiene.md) | Protocolo de compactacao de contexto poluido |
| [`docs/Infrastructure-Intelligence.md`](docs/Infrastructure-Intelligence.md) | Projetos, repositorios, bancos, servicos, APIs, MCPs e ambientes |
| [`docs/Project-Registry.md`](docs/Project-Registry.md) | Project Registry por projeto |
| [`docs/Infrastructure-Registry.md`](docs/Infrastructure-Registry.md) | Registry global de infraestrutura |
| [`docs/Natural-Language-Missions.md`](docs/Natural-Language-Missions.md) | NLME — linguagem natural → missões autônomas |
| [`docs/Strategic-Intelligence-Layer.md`](docs/Strategic-Intelligence-Layer.md) | SIL, Mission Brief (após NLME) |
| [`docs/Missions.md`](docs/Missions.md) | Mission Types, Mission Score e Mission Memory |
| [`docs/Mission-Recognition.md`](docs/Mission-Recognition.md) | Reconhecimento de intencao humana |
| [`docs/Mission-Modes.md`](docs/Mission-Modes.md) | Modos estrategicos de mission |
| [`docs/Continuous-Evolution.md`](docs/Continuous-Evolution.md) | Backlog sugerido apos missions |
| [`docs/DATA_INTELLIGENCE.md`](docs/DATA_INTELLIGENCE.md) | Domínio de dados/BI/SQL/Power BI |
| [`docs/SECURITY_INTELLIGENCE.md`](docs/SECURITY_INTELLIGENCE.md) | SI, autorizacao, permissoes, cache de acesso e threat modeling |
| [`docs/GROWTH_BRAND_INTELLIGENCE.md`](docs/GROWTH_BRAND_INTELLIGENCE.md) | Domínio de branding/copy/marketing/SEO/assets |
| [`docs/GROWTH_INTELLIGENCE.md`](docs/GROWTH_INTELLIGENCE.md) | Crescimento, conversao e evolucao |
| [`docs/BRAND_INTELLIGENCE.md`](docs/BRAND_INTELLIGENCE.md) | Brand DNA, voz, identidade e consistencia |
| [`docs/KNOWLEDGE_HUB.md`](docs/KNOWLEDGE_HUB.md) | Biblioteca interna de boas praticas |
| [`docs/KNOWLEDGE_ENGINE.md`](docs/KNOWLEDGE_ENGINE.md) | Consulta automatica do Knowledge Hub |
| [`docs/BENCHMARK_INTELLIGENCE.md`](docs/BENCHMARK_INTELLIGENCE.md) | Benchmark por principios, sem copia |
| [`docs/PRODUCT_EXCELLENCE.md`](docs/PRODUCT_EXCELLENCE.md) | Padrao minimo de excelencia de produto |
| [`docs/PRODUCT_EVOLUTION.md`](docs/PRODUCT_EVOLUTION.md) | Roadmap apos auditorias |
| [`docs/HYBRID_FLOWS.md`](docs/HYBRID_FLOWS.md) | Fluxos dev + dados + BI |
| [`docs/USING_IN_PROJECTS.md`](docs/USING_IN_PROJECTS.md) | Umbra, Irisys e consumidores |
| [`docs/UPDATE_FRAMEWORK.md`](docs/UPDATE_FRAMEWORK.md) | Atualizar submodule |
| [`docs/INSTALL.md`](docs/INSTALL.md) | Submodule: instalar, atualizar, remover |
| [`docs/VERSIONING.md`](docs/VERSIONING.md) | Semver e tags |
| [`CHANGELOG.md`](CHANGELOG.md) | Histórico de versões |
| [`INTEGRATION.md`](INTEGRATION.md) | Codex, Cursor, alternativas |
| [`context/README.md`](context/README.md) | Contexto por projeto consumidor |

## Stacks suportadas

Node · NestJS · React · Next.js · Flutter · Python · Go · .NET · REST · SQL Server · Power BI · Microserviços · Security/SI · Landing Pages · Sites · SEO · Branding

Defina a stack em `context/tech-stack.md` — templates em `context/_template/`.

## Estrutura

```
├── VERSION / CHANGELOG.md
├── docs/
├── skills/         # orchestrator + governança + técnicas
├── rules/
├── workflows/
├── knowledge/
├── framework/operating-system/
├── infrastructure/
├── templates/
├── templates/mission/
├── checklists/
├── context/        # overlay do projeto + semantic-layer/
├── templates/data/ # pedidos SQL, relatórios, validação
├── templates/marketing/
├── checklists/data/
├── checklists/marketing/
├── rules/data/
├── rules/marketing/
├── examples/data/
└── examples/marketing-growth-brand.md
```

## Criar nova skill

`skills/skill-builder/SKILL.md` — gera SKILL.md, exemplo, checklist, integração com orchestrator.

## Versão

Ver [`VERSION`](VERSION) — atual: **2.14.0**

## Licença

Uso Otus7 / Douglas — ver repositório para termos.
