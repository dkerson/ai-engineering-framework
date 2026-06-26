---
name: support
description: >-
  Triagem de suporte: classificar ticket, reproduzir, escalar.
---

# Support

## Objetivo

Resolver ou encaminhar tickets de suporte eficientemente.

## Quando usar

- Ticket de suporte
- Reclamação de usuário
- Triagem inicial

## Quando NÃO usar

- Desenvolvimento de feature
- Code review

## Responsabilidades

1. Classificar severidade e impacto
2. Reproduzir se possível
3. Workaround temporário se urgente
4. Escalar para bug-hunter se técnico
5. Comunicar status ao usuário

## Entradas esperadas

- Ticket/descrição
- Logs/screenshots

## Saídas esperadas

- Resolução ou escalonamento
- Comunicação ao usuário

## Checklist

- [ ] Severidade classificada
- [ ] Reproduzido ou N/A
- [ ] Workaround se aplicável
- [ ] Escalonado se necessário

## Integração com outras skills

- **Upstream:** orchestrator
- **Downstream:** bug-hunter, deployment

## Exemplos

**Input:** "Não consigo login"
**Output:** Escalado P2 — OAuth callback 404, bug-hunter.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `workflows/support.md`
