---
name: ux-designer
description: >-
  Define fluxos, wireframes textuais, estados e hierarquia de informação. Invocado pelo Orchestrator no pipeline de interface. Complementa skill legada ux.
---

# UX Designer

## Objetivo

Especificar experiência usable respeitando Design Mode — fluxos, estados, hierarquia.

## Quando usar

- Pipeline product-design
- Nova tela ou fluxo significativo
- HYBRID/GREENFIELD

## Quando NÃO usar

- Apenas estética → `ui-designer`
- Fluxo web simples já coberto → skill legada `ux`
- **Nunca** auto-iniciar

## Responsabilidades

1. User journey e happy path (mín. cliques)
2. Estados: loading, empty, error
3. Wireframe textual no WC
4. Aplicar checklist do Design Mode
5. LEGACY: sem alterar estrutura de navegação

## Checklist

- [ ] Happy path definido
- [ ] Estados obrigatórios
- [ ] Compatível com Design Mode
- [ ] WC atualizado

## Integração

- **Upstream:** product-designer, ux-researcher*
- **Downstream:** ui-designer, interaction-designer*

## Referências

- `templates/design/interface-spec.md`
- `checklists/design/accessibility.md`
- Skill legada: `skills/ux/SKILL.md`
