# AI Engineering Framework — AGENTS.md

> **Nome oficial:** AI Engineering Framework (v2.x)
> **Alias legado:** Personal AI Framework — pasta `Personal-AI/` preservada para compatibilidade.
>
> Ponto de entrada universal para agentes Codex/Cursor. O usuário **nunca** escolhe skills manualmente.

## Bootstrap obrigatório

1. **Sempre** iniciar lendo `skills/orchestrator/SKILL.md`
2. O **Orchestrator** é o único agente que conversa com o usuário
3. Nenhuma skill inicia execução por conta própria — todo fluxo passa pelo Orchestrator
4. Respeitar `rules/hierarchical-orchestration.md` e `rules/token-economy.md`
5. Seguir o processo: Entender → Classificar → Escolher modo → Planejar → Investigar → Implementar → Validar → Revisar → Entregar
6. Manter **Working Context** durante a execução (`context/working-context.md`)
7. Terminar com `templates/final-response.md`

## Instalação em projetos

Ver `docs/INSTALL.md` (Git Submodule recomendado). Caminhos: `.ai/`, `ai-engineering-framework/` ou `Personal-AI/` (legado).

## Arquitetura hierárquica

```
Usuário ↔ Orchestrator (único contato)
              ↓
    [Fast | Standard | Review | Technical Council]
              ↓
    Skills sob demanda (nunca auto-iniciam)
              ↓
    Working Context → descartado ao finalizar
```

Detalhes: `docs/ARCHITECTURE.md` · `workflows/modes.md`

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
├── checklists/
├── workflows/
├── context/           ← overlay do projeto consumidor (ver context/README.md)
└── examples/
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

`bug` · `incident` · `feature` · `refactor` · `review` · `documentation` · `functional-spec-doc` · `process-doc` · `performance` · `database` · `api` · `integration` · `devops` · `testing` · `architecture` · `product` · `ux` · `mobile` · `security` · `data` · `commercial` · `finance` · `deployment` · `support`

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

Lista completa de skills técnicas e meta: tabelas em versões anteriores permanecem válidas — ver `workflows/_index.md`.

## Technical Council

Processo (não skill): `workflows/technical-council.md`

## Economia de tokens

- Menor modo seguro
- Working Context — sem releitura
- Council: máx. 150 palavras/skill; usuário vê só decisão consolidada

`rules/token-economy.md` · `rules/hierarchical-orchestration.md`

## Resposta final

Resumo · Diagnóstico · Plano · **Modo** · Skills · Arquivos · Validações · Resultado · Como testar · Riscos · Próximos passos

Template: `templates/final-response.md`

## Expansão

`skills/skill-builder/SKILL.md` → registrar em `workflows/_index.md` e neste arquivo.
