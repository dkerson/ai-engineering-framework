# Execution Metrics

> Finalidade: registrar metricas leves ao final de cada execucao para medir economia estimada de tokens, retries evitados e erros evitados em reports futuros.

## Principio central

Medir sem inflar custo.

O framework deve registrar metricas curtas e aproximadas, baseadas em evidencias observadas durante a execucao. Nunca inventar tokens reais quando a superficie nao expuser telemetria confiavel.

## Arquivo de destino

Registrar em:

`framework/operating-system/EXECUTION_METRICS.md`

## Quando registrar

Registrar ao final de toda task executavel que tenha pelo menos um destes sinais:

- leitura de arquivos;
- edicao;
- comando executado;
- validacao;
- uso de skill;
- roteamento de modelo;
- tentativa/retry;
- report de token economy.

Pode pular em pergunta/resposta puramente conversacional.

## Campos obrigatorios

| Campo | Descricao |
|-------|-----------|
| Date | Data da execucao |
| Mission | Nome curto da missao |
| Surface | Cursor, Codex ou Desconhecida |
| Mode | Fast, Standard, Review ou Technical Council |
| Recommended Model | Modelo recomendado |
| Baseline Route | Caminho que provavelmente seria usado sem o framework |
| Actual Route | Caminho usado |
| Baseline Units | Estimativa de custo operacional sem framework |
| Actual Units | Estimativa de custo operacional com framework |
| Estimated Savings % | Percentual estimado |
| Retries Avoided | Tentativas provavelmente evitadas |
| Errors Avoided | Erros/riscos provavelmente evitados |
| Confidence | Alta, Media ou Baixa |
| Evidence | Evidencia curta |

## Unidades operacionais

Usar unidades operacionais quando tokens reais nao existem.

### Pesos sugeridos

| Item | Unidade |
|------|---------|
| Arquivo lido | 1 |
| Skill usada | 3 |
| Comando/validacao | 2 |
| Tentativa de correcao/retry | 5 |
| Escalada de modo | 8 |
| Full NLME/SIL/COS | 8 |
| Technical Council | 15 |
| Modelo forte sem gatilho | 8 |

## Calculo

```text
Estimated Savings % = ((Baseline Units - Actual Units) / Baseline Units) * 100
```

Regras:

- Se Baseline Units <= 0, nao calcular percentual.
- Limitar percentual entre 0 e 95.
- Arredondar para inteiro.
- Declarar como `estimado`, nunca como token real.

## Como estimar baseline

Use o menor baseline plausivel que o framework evitou:

| Evidencia | Baseline |
|-----------|----------|
| Fast Path aplicado | Full NLME/SIL/COS + leitura de contexto ampla |
| Model Routing economico | Modelo forte ou Auto sem gatilho |
| Surface Routing | Recomendacao errada de modelo/superficie |
| Context Hygiene | Continuar usando contexto poluido |
| Execution Loop Control | Mais 1-2 retries sem mudar hipotese |
| Regression Boundary | Validacao ampla ou regressao colateral |
| No Hardcode | Rework futuro por valor fixo indevido |

## Retries e erros evitados

### Retries Avoided

Contar quando houver:

- loop breaker aplicado;
- hipotese descartada antes de repetir;
- plano refeito antes de novo patch;
- validacao evitada por falta de mudanca relevante.

### Errors Avoided

Contar riscos evitados, como:

- modelo/superficie errado;
- hardcode funcional;
- regressao fora de escopo;
- validacao em porta/cache errado;
- leitura excessiva sem hipotese;
- uso de skill desnecessaria;
- continuar com contexto poluido.

## Confianca

| Confianca | Criterio |
|-----------|----------|
| Alta | Ha tokens reais ou dados objetivos completos |
| Media | Ha contagens de arquivos/skills/comandos e evidencias claras |
| Baixa | E inferencia qualitativa ou regra recem-criada |

## Proibido

- Converter unidades operacionais em tokens reais.
- Converter economia estimada em dolares sem preco e token real.
- Registrar prompts completos, secrets, codigo longo ou dados privados.
- Atualizar metricas com entradas duplicadas para a mesma execucao.
