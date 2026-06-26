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
│  Orchestrator ──► Modo (Fast|Standard|Review|Council)   │
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
| Bootstrap | `AGENTS.md` | Entrada universal; aponta para Orchestrator |
| Orquestração | `skills/orchestrator/` | Modo, pipeline, Working Context, entrega |
| Governança | `critic`, `validator`, `risk-reviewer`, `decision-maker`, `implementation-planner` | Qualidade e decisão |
| Execução | Skills técnicas (`backend`, `api`, `react`, …) | Implementação especializada |
| Fluxos | `workflows/` | Pipelines por tipo de demanda + modos |
| Regras | `rules/` | Políticas transversais |
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
| REST / microserviços | `api`, `integration` |

Defina a stack real em `context/tech-stack.md` do projeto consumidor.

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
| Pasta `Personal-AI/` preservada | Compatibilidade Umbra e consumidores v1 |
| Submodule como instalação primária | Atualização isolada do framework |
| Council como processo, não skill | Composição dinâmica por demanda |
| Context como overlay | Framework independente de domínio |
