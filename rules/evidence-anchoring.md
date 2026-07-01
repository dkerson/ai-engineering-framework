# Evidence Anchoring

> Finalidade: reduzir alucinacao operacional separando fatos observados, inferencias e hipoteses.

## Principio central

Toda conclusao operacional deve estar ancorada em evidencia verificavel ou ser marcada como inferencia/hipotese.

## Tipos de afirmacao

| Tipo | Exige |
|------|-------|
| Observado | Arquivo, linha, comando, diff, log, registro FOS ou output resumido |
| Inferido | Evidencia parcial + raciocinio curto |
| Hipotese | Declarar que falta confirmacao e definir validacao |
| Decisao | Evidencias consideradas + trade-off |
| Recomendacao | Impacto, esforco, risco e fonte |

## Gate anti-alucinacao

Antes de implementar, validar ou responder:

1. O que estou afirmando como fato?
2. Qual evidencia sustenta isso?
3. O que e apenas inferencia?
4. O que precisa de validacao?
5. A resposta separa observado de recomendado?

Se uma conclusao nao tiver evidencia suficiente, escrever como hipotese e indicar a validacao minima.

## Evidencias aceitas

- Caminho de arquivo com linha quando aplicavel.
- Comando executado e resultado resumido.
- Diff local ou commit remoto.
- Registro FOS vivo.
- Resultado de teste, build, lint, browser, network, console ou consulta.
- Declaracao explicita do usuario.

## Proibido

- Declarar sucesso sem validacao coerente com o risco.
- Afirmar causa raiz sem evidencia.
- Promover padrao com uma ocorrencia isolada.
- Confundir recomendacao com fato observado.
- Copiar longos outputs para justificar conclusoes.

## Formato no Working Context

```markdown
### Evidence Anchoring
- Observed facts:
- Inferences:
- Hypotheses:
- Evidence gaps:
- Required validation:
- Confidence:
```
