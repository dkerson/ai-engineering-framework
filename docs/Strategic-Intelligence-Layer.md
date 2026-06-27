# Strategic Intelligence Layer

> Camada estratégica que refina Mission Brief a partir do NLME.

## Objetivo

Permitir que o usuário converse naturalmente, sem conhecer skills, fluxos, técnicas ou arquitetura interna. O **NLME** traduz a conversa; o **SIL** refine estrategicamente.

## Posicao na arquitetura

```text
Usuario (linguagem natural)
        ↓
Natural Language Mission Engine (NLME)
        ↓
Strategic Intelligence Layer (SIL)
        ↓
Capability Operating System (COS)
        ↓
Master Orchestrator
        ↓
Technical Council (quando necessario)
        ↓
Domains → Skills → Projetos
```

## Entrada NLME (v2.12+)

O SIL recebe do NLME:

- Translation Brief (mission-translator)
- Mission Package (mission-builder)
- Structured Prompt (prompt-builder — interno)
- Mission Confidence Score

O SIL **refina** e produz **Mission Brief** final → `templates/mission/mission-brief.md`.

## Capability Intelligence (COS v2.10+)

Antes de dominios e plano, o SIL considera:

1. **Ja existe Capability?** → sugerir `capability_id` no Mission Brief
2. **Se nao** → flag `propose_new_capability` para capability-evaluator
3. **Nunca implementar** — Orchestrator + COS registram Idea com aprovacao

## Responsabilidade unica

O SIL transforma Mission Package em Mission Brief operacional.

O SIL nunca:

- Implementa codigo
- Chama skills diretamente
- Altera arquivos
- Executa comandos
- Abre projeto ou le arquivos de produto

O SIL sempre:

- Interpreta objetivo principal e secundarios (com Goal Recognition)
- Reconhece contexto, urgencia, impacto, risco e complexidade
- Define mission type e mission mode
- Pontua a mission
- Decide se precisa perguntar algo (Mission Confidence)
- Entrega um Mission Brief ao Master Orchestrator

## Strategic Thinking

Antes de classificar a mission, o SIL considera perspectivas de:

- CEO
- CTO
- Head de Produto
- Head de UX
- Head de Engenharia
- Head de Dados
- Head de Marketing

## Question Engine

- Se o objetivo estiver claro (Confidence ≥ 60), nao perguntar.
- Se faltar informacao realmente critica, perguntar o minimo necessario.
- Evitar entrevistas longas.
- Preferir decisao autonoma quando o risco for baixo ou medio.

## Saida para o Master Orchestrator

O SIL deve produzir:

- Mission type
- Mission mode
- Objetivo principal
- Objetivos secundarios
- Dominios envolvidos
- Risco, impacto, complexidade e confianca
- Quick wins provaveis
- Necessidade de Technical Council
- Knowledge Hub sugerido
- **Capability sugerida** (COS) ou flag `propose_new_capability`
- Plano de alto nivel

Detalhes: `docs/Natural-Language-Missions.md` · `docs/Missions.md` · `docs/Mission-Recognition.md` · `docs/Mission-Modes.md`.
