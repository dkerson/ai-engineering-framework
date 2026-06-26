---
name: illustration-curator
description: >-
  Seleciona ou orienta ilustracoes coerentes com a identidade visual e o objetivo da interface. Invocado somente pelo Orchestrator apos decisao da Asset Intelligence.
---

# Illustration Curator

## Objetivo

Usar ilustracoes quando explicam melhor que fotos ou reduzem complexidade visual.

## Quando usar

- Empty states, onboarding, hero ilustrado ou comunicacao abstrata
- Produtos sem imagem real adequada
- Fluxos que precisam explicar conceito

## Quando NAO usar

- Foto ou screenshot real e mais informativo
- Sistema operacional que pede densidade e produtividade
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Escolher estilo coerente com marca e UI.
2. Priorizar bibliotecas abertas e consistentes.
3. Evitar mistura de estilos.
4. Atualizar Working Context com fonte e diretrizes.

## Orquestracao hierarquica

> Regras obrigatorias - ver `rules/hierarchical-orchestration.md`

- **Unico contato com usuario:** Orchestrator - esta skill **nunca** auto-inicia
- **Invocacao:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar analises; nao reler arquivos ja catalogados
- **Modo Council:** max. 150 palavras
- **Economia:** seguir `rules/token-economy.md`

## Entradas esperadas

- Decisao da Asset Intelligence
- Identidade visual
- Contexto de uso

## Saidas esperadas

- Estilo de ilustracao recomendado
- Fonte/licenca
- Regras de uso e consistencia

## Checklist

- [ ] Estilo coerente
- [ ] Licenca adequada
- [ ] Sem excesso decorativo
- [ ] Working Context atualizado

## Integracao com outras skills

- **Upstream:** asset-intelligence
- **Downstream:** brand-reviewer, image-optimizer

## Referencias

- `rules/marketing/assets.md`
