# Post-Mission Evaluation

> Finalidade: transformar cada execucao relevante em aprendizado curto, verificavel e reutilizavel.

## Principio central

Ao final de toda task executavel, o Orchestrator faz uma avaliacao curta antes da resposta final. A avaliacao nao deve virar burocracia: ela so registra sinais uteis para melhorar execucoes futuras.

## Perguntas obrigatorias

1. O objetivo foi cumprido?
2. A validacao foi suficiente para o risco?
3. O modo usado foi o menor modo seguro?
4. Houve leitura, skill, comando ou modelo caro sem justificativa?
5. Houve hipotese descartada ou erro evitado que deve entrar na memoria?
6. Alguma conclusao ficou sem evidencia?
7. Existe aprendizado reutilizavel?

## Saida minima

```markdown
### Post-Mission Evaluation
- Outcome: [Done|Partial|Blocked|Recommendation-only]
- Quality confidence: [Alta|Media|Baixa]
- Validation fit: [Sufficient|Partial|Not run|Not applicable]
- Token efficiency: [Good|Acceptable|Waste signal]
- Reusable learning:
- Memory index update: [yes/no + motivo]
- Promotion candidate: [yes/no]
```

## Quando registrar no FOS

Registrar somente quando houver um destes sinais:

- retry ou hipotese descartada;
- erro evitado;
- economia ou desperdicio de tokens;
- padrao recorrente;
- anti-padrao observado;
- decisao que deve orientar missoes futuras;
- validacao enganosa ou incompleta;
- skill desnecessaria ou ausente.

## Integracao

- Atualizar `EXECUTION_MEMORY_INDEX.md` quando a avaliacao gerar aprendizado reutilizavel.
- Atualizar `EXECUTION_METRICS.md` quando houver baseline/actual units.
- Atualizar `TOKEN_METRICS.md` quando houver waste/savings relevante.
- Atualizar `LEARNING.md` somente quando houver aprendizado real, nao mera execucao normal.
