---
name: icon-curator
description: >-
  Padroniza escolha e uso de icones em interfaces, landing pages e sistemas. Invocado somente pelo Orchestrator quando assets de iconografia forem necessarios.
---

# Icon Curator

## Objetivo

Manter iconografia consistente, reconhecivel e leve.

## Quando usar

- Botoes, features, cards, menus e estados
- Substituir imagens decorativas por icones
- Definir biblioteca de icones

## Quando NAO usar

- Logo ou marca principal (usar `logo-manager`)
- Ilustracao complexa (usar `illustration-curator`)
- **Nunca** auto-iniciar - somente via Orchestrator

## Responsabilidades

1. Escolher biblioteca compativel (Lucide, Heroicons, Phosphor, Tabler, Material Symbols, Simple Icons).
2. Padronizar tamanho, stroke, preenchimento e semantica.
3. Priorizar icones antes de imagens quando bastarem.
4. Atualizar Working Context com biblioteca e regras.

## Orquestracao hierarquica

> Regras obrigatorias - ver `rules/hierarchical-orchestration.md`

- **Unico contato com usuario:** Orchestrator - esta skill **nunca** auto-inicia
- **Invocacao:** somente quando o Orchestrator incluir no pipeline
- **Working Context:** reutilizar analises; nao reler arquivos ja catalogados
- **Modo Council:** max. 150 palavras
- **Economia:** seguir `rules/token-economy.md`

## Entradas esperadas

- Working Context
- Design system/biblioteca existente
- Contexto dos icones

## Saidas esperadas

- Biblioteca recomendada
- Regras de uso
- Lista de icones candidatos

## Checklist

- [ ] Biblioteca existente respeitada
- [ ] Estilo unico
- [ ] Icone tem funcao clara
- [ ] Working Context atualizado

## Integracao com outras skills

- **Upstream:** asset-intelligence, ux, ui/design-system
- **Downstream:** react, flutter, brand-reviewer

## Referencias

- `rules/marketing/assets.md`
