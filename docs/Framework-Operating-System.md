# Framework Operating System

> Sistema operacional do AI Engineering Framework.

## Objetivo

Administrar a evolucao do proprio framework por meio de registros vivos, metricas, saude, roadmap, backlog, decisoes, aprendizado e recomendacoes.

## Responsabilidades

- Registrar
- Aprender
- Medir
- Organizar
- Priorizar
- Versionar
- Documentar
- Auditar
- Recomendar

## Limites

O FOS nunca:

- Executa codigo
- Implementa features
- Modifica o framework automaticamente
- Remove skills
- Altera interfaces publicas sem aprovacao

Toda mudanca depende de aprovacao do usuario.

## Estrutura

`framework/operating-system/`

Documentos vivos principais:

- `FRAMEWORK_STATUS.md`
- `FRAMEWORK_HEALTH.md`
- `ROADMAP.md`
- `BACKLOG.md`
- `IDEAS.md`
- `IMPLEMENTED.md`
- `UNDER_REVIEW.md`
- `REJECTED.md`
- `DECISIONS.md`
- `CHANGELOG.md`
- `LEARNING.md`
- `RETROSPECTIVES.md`
- `PATTERNS.md`
- `ANTI_PATTERNS.md`
- `RECOMMENDATIONS.md`
- `FRAMEWORK_METRICS.md`
- `FRAMEWORK_REPORT.md`
- `MISSION_LEDGER.md`
- `SKILL_USAGE.md`
- `TOKEN_METRICS.md`
- `EXECUTION_METRICS.md`
- `EXECUTION_MEMORY_INDEX.md`
- `PROMOTION_CRITERIA.md`
- `NEXT_STEPS.md`
- `VERSION.md`

## Execution Intelligence

O FOS pode observar execucoes reais para reduzir custo e melhorar eficiencia:

- `MISSION_LEDGER.md` registra metadados curtos de missoes.
- `SKILL_USAGE.md` mede quais skills foram realmente usadas.
- `TOKEN_METRICS.md` registra sinais de desperdicio e economia.
- `EXECUTION_METRICS.md` registra baseline, actual units, savings %, retries e errors avoided.
- `EXECUTION_MEMORY_INDEX.md` concentra aprendizados reutilizaveis para consulta antes de tasks similares.
- `PROMOTION_CRITERIA.md` define quando aprendizado vira recomendacao.
- `rules/context-hygiene.md` define quando o Orchestrator cria Compacted Snapshot para evitar contexto poluido.
- `rules/execution-memory.md` define recuperacao dirigida de aprendizados anteriores.
- `rules/evidence-anchoring.md` exige separar fatos observados, inferencias e hipoteses.
- `rules/post-mission-evaluation.md` fecha o ciclo de avaliacao e atualizacao de memoria.

Limite: observar e recomendar nao autoriza auto-mutacao. Mudancas no framework continuam dependendo de aprovacao do usuario.

## Natural Questions

O framework deve responder usando documentos vivos:

- Como esta nosso Framework?
- Qual nossa evolucao?
- O que implementamos?
- O que ainda falta?
- Quais ideias temos?
- Quais melhorias recomenda?
- Qual nosso Roadmap?
- Qual nossa Saude?
- Quais padroes aprendemos?
- Qual nossa divida tecnica?
- Quais erros nao devemos repetir?
- A promocao de padroes das ultimas 10 missoes esta em dia?
