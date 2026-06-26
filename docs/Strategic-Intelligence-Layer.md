# Strategic Intelligence Layer

> Camada acima do Master Orchestrator responsavel por transformar linguagem natural em Missoes Estrategicas.

## Objetivo

Permitir que o usuario converse naturalmente, sem conhecer skills, fluxos, tecnicas ou arquitetura interna.

## Posicao na arquitetura

```text
Usuario
-> Strategic Intelligence Layer
-> Master Orchestrator
-> Technical Council
-> Domains
-> Skills
-> Implementacao
```

## Responsabilidade unica

O SIL transforma intencoes humanas em Missoes Estrategicas.

O SIL nunca:

- Implementa codigo
- Chama skills diretamente
- Altera arquivos
- Executa comandos
- Abre projeto ou le arquivos de produto

O SIL sempre:

- Interpreta objetivo principal e secundarios
- Reconhece contexto, urgencia, impacto, risco e complexidade
- Define mission type e mission mode
- Pontua a mission
- Decide se precisa perguntar algo
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

- Se o objetivo estiver claro, nao perguntar.
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
- Plano de alto nivel

Detalhes: `docs/Missions.md`, `docs/Mission-Recognition.md`, `docs/Mission-Modes.md`.
