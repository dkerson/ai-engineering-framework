# Template Canônico de Skill

> Finalidade: copiar este arquivo ao criar novas skills via Skill Builder.

```markdown
---
name: [kebab-case-name]
description: >-
  [O que faz — terceira pessoa]. Invocado somente pelo Orchestrator quando [triggers].
---

# [Título Legível]

## Objetivo

[Uma frase: responsabilidade única]

## Quando usar

- [Cenário 1 — Orchestrator invoca]
- [Cenário 2]

## Quando NÃO usar

- [Anti-cenário 1]
- **Nunca** auto-iniciar — somente via Orchestrator
- Delegar para skill X

## Responsabilidades

1. [Passo acionável]
2. [Passo acionável]
3. Atualizar Working Context com descobertas (bullets concisos)

## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`

## Entradas esperadas

- Working Context
- [Input específico]

## Saídas esperadas

- [Output 1 — adicionar ao Working Context]
- [Output 2]

## Checklist

- [ ] [Critério verificável]
- [ ] Working Context atualizado
- [ ] Sem comunicação direta com usuário (salvo Orchestrator)

## Integração com outras skills

- **Upstream:** orchestrator
- **Downstream:** [skills invocadas após esta]

## Exemplos

**Input:** [pedido concreto via Orchestrator]
**Output:** [resultado no Working Context]

## Referências

- `rules/hierarchical-orchestration.md`
- `rules/token-economy.md`
- `context/working-context.md`
```

## Regras de authoring

| Regra | Detalhe |
|-------|---------|
| Linhas | SKILL.md < 500 |
| Description | Terceira pessoa + "Invocado pelo Orchestrator" |
| Nome | kebab-case, max 64 chars |
| Orquestração | Seção **Orquestração hierárquica** obrigatória |
| Progressive disclosure | Detalhes em `reference.md` irmão se > 500 linhas |
| DRY | Linkar rules/templates — não duplicar |

## Registro pós-criação

1. `workflows/_index.md` — se skill entra em pipeline
2. `AGENTS.md` — tabela de skills
3. `examples/` — se caso de uso não óbvio
