# Design Modes — LEGACY · HYBRID · GREENFIELD

> O Orchestrator identifica o modo **antes** de qualquer geração de interface.

## Detecção (perguntas internas)

- O projeto possui Design System?
- Existe identidade visual?
- Existe biblioteca de componentes?
- Existe padrão visual / guideline / tema?
- É sistema legado ou manutenção?

## LEGACY MODE

**Quando:** projeto existente, legado, manutenção, bug, pequenas melhorias.

| Preservar | Melhorar apenas |
|-----------|-----------------|
| Layout, componentes, cores, tipografia, espaçamentos, identidade | A11y, organização, responsividade, consistência, UX pontual |

**Proibido:** redesenhar, trocar componentes, mudar identidade visual.

## HYBRID MODE

**Quando:** sistema existente com evolução gradual permitida.

**Permitido:** hierarquia, espaçamento, tipografia, organização, responsividade, mobile, a11y — **sem descaracterizar**.

## GREENFIELD MODE

**Quando:** novo projeto, módulo, produto, app ou área independente.

**Aplicar:** Design DNA + `design-system/` completo (se projeto sem identidade).

## Regra absoluta

Alterar identidade visual de sistema existente **somente** com solicitação explícita do usuário.

Detalhes: `docs/DESIGN_MODES.md`
