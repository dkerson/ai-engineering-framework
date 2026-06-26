---
name: software-architect
description: >-
  Toma decisões arquiteturais, define padrões e ADRs. Usar em features complexas, refatorações estruturais ou dúvidas de design.
---

# Software Architect

## Objetivo

Garantir soluções escaláveis, coerentes com arquitetura existente.

## Quando usar

- Decisão arquitetural
- Feature multi-módulo
- Refatoração estrutural
- Integração complexa

## Quando NÃO usar

- Alteração localizada
- Tarefa já coberta por padrão existente

## Responsabilidades

1. Analisar arquitetura atual (`context/architecture.md`)
2. Propor opções com trade-offs
3. Recomendar abordagem
4. Gerar ADR se decisão significativa
5. Validar SOLID e boundaries

## Entradas esperadas

- Context builder output
- Functional/technical requirements

## Saídas esperadas

- Decisão arquitetural
- ADR (`templates/adr.md`) se aplicável

## Checklist

- [ ] Opções avaliadas
- [ ] Trade-offs documentados
- [ ] Coerência com arquitetura existente
- [ ] ADR gerado se necessário

## Integração com outras skills

- **Upstream:** functional-spec, context-builder
- **Downstream:** technical-spec, tech-lead

## Exemplos

**Input:** Event-driven vs REST
**Output:** ADR recomendando outbox pattern.


## Orquestração hierárquica

> Regras obrigatórias — ver `rules/hierarchical-orchestration.md`

- **Único contato com usuário:** Orchestrator — esta skill **nunca** auto-inicia
- **Invocação:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar análises; não reler arquivos já catalogados
- **Modo Council:** máx. 150 palavras (diagnóstico · risco · recomendação · validação)
- **Economia:** seguir `rules/token-economy.md`


## Referências

- `templates/adr.md`
- `rules/architecture.md`
- `rules/solid.md`
