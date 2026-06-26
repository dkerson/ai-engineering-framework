---
name: implementation-planner
description: >-
  Transforma decisão técnica em plano executável: etapas, arquivos, validações, testes e ordem de implementação. Invocado pelo Orchestrator após Decision Maker ou planejamento em modos Review/Council.
---

# Implementation Planner

## Objetivo

Converter decisão em plano técnico **acionável** com ordem clara e validações por etapa.

## Quando usar

- Após **Decision Maker** (Technical Council)
- Modo **Review** quando múltiplos arquivos/módulos
- Orchestrator precisa de plano antes de implementar mudanças complexas
- Substituir ou complementar tech-lead em escopos grandes

## Quando NÃO usar

- Modo Fast
- Fix pontual de 1 arquivo (Orchestrator executa direto)
- **Nunca** auto-iniciar

## Saída obrigatória

```markdown
## Plano de Implementação

### Etapas
1. [ação] — arquivos: [...] — validação: [...]
2. ...

### Arquivos afetados
- `path/to/file` — [criar|alterar|remover]

### Validações por etapa
- Etapa 1: [teste/lint/build]
- ...

### Testes
- [casos a criar ou executar]

### Ordem de implementação
[sequência com dependências]
```

Máximo: **300 palavras** (plano pode ser mais longo que opiniões do conselho).

## Responsabilidades

1. Ler decisão do Decision Maker ou escopo do Orchestrator
2. Reutilizar Working Context — não reler arquivos
3. Produzir etapas ordenadas com dependências
4. Indicar validação mínima por etapa
5. Atualizar Working Context com plano

## Entradas esperadas

- Decisão consolidada
- Working Context (escopo, módulos, riscos)

## Saídas esperadas

- Plano numerado no Working Context
- Lista de arquivos candidatos
- Critérios de validação por etapa

## Orquestração hierárquica

- **Invocação:** somente Orchestrator
- **Fala com usuário:** não — plano resumido na resposta final
- **Downstream:** skills técnicas executam etapas na ordem
- Detalhes: `rules/hierarchical-orchestration.md`

## Checklist

- [ ] Etapas ordenadas com dependências
- [ ] Arquivos listados
- [ ] Validações por etapa
- [ ] Plano no Working Context

## Integração

- **Upstream:** decision-maker, orchestrator, tech-lead
- **Downstream:** backend, api, database, react, flutter, qa

## Referências

- `skills/tech-lead/SKILL.md`
- `context/working-context.md`
- `rules/token-economy.md`
