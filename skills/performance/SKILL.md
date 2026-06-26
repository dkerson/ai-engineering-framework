---
name: performance
description: >-
  Profiling, benchmarks, otimização de gargalos. Usar quando algo está lento ou consome recursos excessivos.
---

# Performance

## Objetivo

Identificar e resolver gargalos com medição antes/depois.

## Quando usar

- Lentidão reportada
- Timeout, high CPU/memory
- Otimização solicitada

## Quando NÃO usar

- Feature nova sem problema perf
- Premature optimization

## Responsabilidades

1. Medir baseline (tempo, queries, memória)
2. Identificar top bottleneck (80/20)
3. Aplicar fix mínimo
4. Medir novamente
5. Documentar ganho

## Entradas esperadas

- Sintoma de lentidão
- Logs/metrics se disponíveis

## Saídas esperadas

- Métricas before/after
- Fix aplicado ou recomendado

## Checklist

- [ ] Baseline medido
- [ ] Gargalo identificado
- [ ] Fix mínimo aplicado
- [ ] Melhoria quantificada
- [ ] Sem otimização prematura

## Integração com outras skills

- **Upstream:** orchestrator
- **Downstream:** database, backend, devops

## Exemplos

**Input:** API lista 10s
**Output:** N+1 em OrderItems — eager load reduziu para 200ms.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `checklists/performance.md`
- `templates/root-cause-analysis.md`
