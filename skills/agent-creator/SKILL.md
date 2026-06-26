---
name: agent-creator
description: >-
  Cria configurações de agentes: instruções, tools, handoffs.
---

# Agent Creator

## Objetivo

Projetar agentes especializados para automações.

## Quando usar

- Novo agente Codex/Cursor
- Automação multi-step
- Agent handoffs

## Quando NÃO usar

- Skill simples (skill-builder)
- Código de aplicação

## Responsabilidades

1. Definir persona e escopo
2. Listar tools/skills disponíveis
3. Definir handoff rules
4. Testar com casos reais
5. Documentar limites

## Entradas esperadas

- Objetivo do agente
- prompt-engineer output

## Saídas esperadas

- Agent config
- Documentação de uso

## Checklist

- [ ] Escopo delimitado
- [ ] Tools corretas
- [ ] Handoffs definidos
- [ ] Testado com 2+ casos

## Integração com outras skills

- **Upstream:** prompt-engineer
- **Downstream:** skill-builder

## Exemplos

**Input:** Agente de triagem de bugs
**Output:** Agent que classifica e roteia para bug-hunter.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `skills/orchestrator/SKILL.md`
