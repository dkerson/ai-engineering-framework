# Token Savings Report

> Finalidade: gerar relatorios sob demanda sobre economia de tokens e eficiencia operacional do framework.

## Comandos naturais

Acionar quando o usuario pedir algo como:

- "gera um report de economia de tokens"
- "relatorio de economia de tokens"
- "avaliar eficiencia do framework"
- "quanto o framework economizou de token"
- "token savings report"
- "relatorio de token economy"

## Principio central

Separar medicao real de estimativa.

Se nao houver logs com tokens reais por chamada/modelo, o relatorio deve declarar:

```text
Economia real em tokens: nao medida.
Economia estimada: baseada em sinais operacionais.
```

Nao inventar numero exato de tokens, dolares ou porcentagem sem fonte.

## Fontes obrigatorias

Ler somente os ledgers necessarios:

1. `framework/operating-system/TOKEN_METRICS.md`
2. `framework/operating-system/MISSION_LEDGER.md`
3. `framework/operating-system/SKILL_USAGE.md`
4. `framework/operating-system/EXECUTION_METRICS.md`

Fontes opcionais, se agregarem evidencia sem leitura ampla:

- `framework/operating-system/IMPLEMENTED.md`
- `framework/operating-system/FRAMEWORK_HEALTH.md`
- `framework/operating-system/reports/`

## Classificacao de evidencia

| Evidencia | Tipo | Confianca |
|-----------|------|-----------|
| Tokens reais por request/modelo | Medicao direta | Alta |
| Execution Metrics com baseline/actual units | Estimativa estruturada | Media |
| Arquivos lidos, skills usadas, modo, validacao | Estimativa operacional | Media |
| Notas de economia/desperdicio em ledger | Evidencia qualitativa | Media |
| Inferencia por regra criada sem uso real ainda | Potencial futuro | Baixa |

## Indicadores

### Economia

- Fast Path usado antes de NLME completo.
- Menor modo seguro escolhido.
- Skills evitadas.
- Arquivos reutilizados via Working Context.
- Context Hygiene/Compacted Snapshot usado.
- Validacao limitada ao risco.
- Model Routing recomendou modelo economico.
- Surface Routing evitou recomendacao errada de modelo.
- Loop Control evitou tentativa repetida.

### Desperdicio

- Full NLME usado para pedido simples.
- Mais de 5 skills em Standard sem justificativa.
- Mais de 12 arquivos lidos antes da primeira hipotese.
- Build completo para mudanca pequena.
- Releitura de arquivos ja analisados.
- Continuacao com plano antigo ou contexto poluido.
- Troca de modelo forte sem gatilho objetivo.

## Score estimado

Quando nao houver token real, gerar apenas um indice qualitativo:

| Score | Interpretacao |
|-------|---------------|
| 80-100 | Economia forte e governada |
| 60-79 | Boa economia com oportunidades |
| 40-59 | Economia moderada; revisar desperdicios |
| 0-39 | Alto risco de desperdicio |

O score e um indice de eficiencia, nao uma contagem de tokens.

Formula sugerida:

```text
base 50
+ 8 por sinal forte de economia recorrente
+ 4 por sinal moderado de economia
- 8 por sinal forte de desperdicio recorrente
- 4 por sinal moderado de desperdicio
limitar entre 0 e 100
```

## Percentual estimado

Quando `EXECUTION_METRICS.md` tiver entradas, calcular:

```text
Weighted Estimated Savings % =
sum(Baseline Units - Actual Units) / sum(Baseline Units) * 100
```

Regras:

- Declarar como percentual estimado, nao token real.
- Exibir tambem `Retries Avoided` e `Errors Avoided` somados.
- Mostrar confianca com base nas entradas.
- Se houver tokens reais no futuro, separar `Measured Token Savings %` de `Estimated Operational Savings %`.

## Saida obrigatoria

Usar `templates/token-savings-report.md`.

O relatorio deve conter:

1. periodo analisado;
2. fontes consultadas;
3. qualidade dos dados;
4. economia real, se medida;
5. economia estimada e percentual estimado;
6. sinais de economia;
7. sinais de desperdicio;
8. missoes mais eficientes;
9. oportunidades de melhoria;
10. retries evitados e erros evitados;
11. recomendacoes para proxima medicao.

## Registro

Se o relatorio gerar aprendizado util, registrar uma linha curta em `TOKEN_METRICS.md` ou `MISSION_LEDGER.md`. Nao registrar prompts completos, secrets, codigo longo ou dados privados.
