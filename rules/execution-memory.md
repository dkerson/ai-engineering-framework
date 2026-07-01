# Execution Memory

> Finalidade: reutilizar aprendizados de execucoes anteriores antes de planejar ou repetir trabalho.

## Principio central

O framework deve aprender com missoes reais sem se auto-modificar. Antes de executar uma task nao trivial, o Orchestrator consulta memoria curta e acionavel para evitar repetir hipoteses ruins, leituras desnecessarias, validacoes enganosas e escalonamentos caros.

## Fontes canonicas

Consultar somente fontes leves:

- `framework/operating-system/EXECUTION_MEMORY_INDEX.md`
- `framework/operating-system/MISSION_LEDGER.md`
- `framework/operating-system/LEARNING.md`
- `framework/operating-system/ANTI_PATTERNS.md`
- `framework/operating-system/PATTERNS.md`
- `framework/operating-system/EXECUTION_METRICS.md`
- `framework/operating-system/TOKEN_METRICS.md`

Nao ler historico inteiro quando o indice responder. Usar `rg` dirigido por mission type, dominio, skill, erro, tecnologia ou arquivo.

## Gate de recuperacao

Antes do plano executavel, responder internamente:

1. Existe missao similar?
2. Qual modo/modelo funcionou melhor?
3. Qual erro, hipotese ou validacao ja falhou antes?
4. Qual padrao aprovado reduz custo agora?
5. Qual anti-padrao precisa ser evitado?
6. Que evidencia anterior e forte o bastante para guiar o plano?

Se nada relevante for encontrado, registrar `No relevant prior memory` no Working Context e seguir sem busca extra.

## Formato no Working Context

```markdown
### Execution Memory
- Query:
- Sources checked:
- Similar missions:
- Reusable decisions:
- Known failed hypotheses:
- Applicable patterns:
- Anti-patterns to avoid:
- Impact on plan:
- Confidence: [Alta|Media|Baixa]
```

## Memoria de hipoteses

Quando houver retry, bloqueio ou correcao relevante, registrar no indice:

- hipotese testada;
- evidencia;
- resultado;
- causa real, se descoberta;
- acao que evitara repeticao futura.

## Limites

- Nao registrar prompts completos, secrets, codigo longo ou dados privados.
- Nao promover aprendizado de uma unica evidencia para regra geral.
- Nao usar memoria antiga contra evidencia nova mais forte.
- Nao bloquear execucao por falta de memoria.

## Integracao

- `rules/evidence-anchoring.md`: memoria so orienta decisao se tiver evidencia.
- `rules/execution-loop-control.md`: hipoteses descartadas podem virar memoria persistente.
- `rules/post-mission-evaluation.md`: avaliacao final decide o que entra no indice.
- `framework/operating-system/PROMOTION_CRITERIA.md`: promocao ativa a cada 10 missoes reais.
