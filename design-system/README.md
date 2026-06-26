# Design System — AI Engineering Framework

> Biblioteca lógica de tokens e padrões. **Não substitui** o Design System do projeto consumidor.

## Uso

1. Orchestrator identifica **Design Mode** (`docs/DESIGN_MODES.md`)
2. Carrega **Design DNA** do projeto (`context/design-dna.md` ou `templates/design/design-dna.md`)
3. Se projeto tem DS próprio → usar integralmente (`rules/design/visual-identity.md`)
4. Se não tem → aplicar tokens desta pasta como baseline moderno (`design-dna-default.md`)

## Índice

| Área | Arquivo |
|------|---------|
| Design DNA padrão | [design-dna-default.md](design-dna-default.md) |
| Cores | [colors.md](colors.md) |
| Tipografia | [typography.md](typography.md) |
| Espaçamento | [spacing.md](spacing.md) |
| Grid | [grid.md](grid.md) |
| Ícones | [icons.md](icons.md) |
| Botões | [buttons.md](buttons.md) |
| Inputs | [inputs.md](inputs.md) |
| Cards | [cards.md](cards.md) |
| Badges / Chips | [badges.md](badges.md) · [chips.md](chips.md) |
| Dialogs / Drawers | [dialogs.md](dialogs.md) · [drawers.md](drawers.md) |
| Tabelas / Forms | [tables.md](tables.md) · [forms.md](forms.md) |
| Navegação | [navigation.md](navigation.md) |
| Feedback | [feedback.md](feedback.md) |
| Loading / Skeletons | [loading.md](loading.md) · [skeletons.md](skeletons.md) |
| Empty / Error | [empty-states.md](empty-states.md) · [error-states.md](error-states.md) |
| Light / Dark | [light-mode.md](light-mode.md) · [dark-mode.md](dark-mode.md) |
| Componentes (catálogo) | [components.md](components.md) |

## Regra absoluta

**Nunca copiar** layouts, marcas ou identidade de Linear, Stripe, Notion, Vercel, GitHub, Material 3, Apple HIG ou Fluent 2 — apenas princípios de qualidade.
