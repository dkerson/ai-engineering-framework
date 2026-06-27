# Mission Confidence

> Score de confiança antes de iniciar execução NLME.

## Mission Confidence Score (0–100)

Calculado por `mission-builder` antes de SIL e execução.

## Fatores

| Fator | Peso | Alto score quando |
|-------|------|-------------------|
| Clareza do objetivo | 25% | Goal Recognition unívoco |
| Projeto identificado | 20% | Registry match |
| Mission Type | 20% | Catálogo com match claro |
| Escopo inferível | 15% | Análise vs implícito e coerente |
| Risco conhecido | 10% | Baixo/médio previsível |
| Histórico (Mission Memory) | 10% | Missão similar já executada |

## Thresholds

| Score | Comportamento |
|-------|---------------|
| **≥ 75** | Executar autonomamente; apresentar plano e iniciar |
| **60–74** | Executar; mencionar 1 suposição na resposta inicial |
| **40–59** | Apresentar plano; **1 pergunta** se gap crítico |
| **< 40** | Apresentar plano; **até 3 perguntas** mínimas |

## Nunca

- Bloquear execução por score 60+ em missões de análise/audit
- Iniciar interrogatório longo
- Pedir confirmação de skills ou workflows

## Exemplo

"Analise o KB" + projeto Umbra implícito:

- Objetivo claro (audit) → 22/25
- Projeto umbra → 18/20
- Audit Mission → 18/20
- Escopo análise → 13/15
- Risco baixo → 9/10
- Sem histórico → 5/10
- **Total ≈ 85** → executar autonomamente

## Referências

- `skills/mission-builder/SKILL.md`
- `rules/mission-confidence.md`
- `templates/mission/nlme-first-response.md`
