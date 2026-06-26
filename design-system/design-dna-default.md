# Design DNA — Padrão Greenfield

> Aplicar somente quando o projeto **não** possui identidade visual definida.

## Princípios (inspiração, não cópia)

- Clareza > decoração
- Densidade moderada (SaaS B2B)
- Hierarquia tipográfica forte
- Ações primárias óbvias
- Feedback imediato
- Consistência de componentes

## Tokens base

| Token | Valor sugerido |
|-------|----------------|
| Raio | 6–8px (cards), 4px (inputs), full (pills) |
| Sombra | sutil: `0 1px 2px rgba(0,0,0,.06)` |
| Densidade | 8px grid |
| Fonte UI | system-ui stack ou Inter/Geist se permitido |
| Escala tipo | 12 · 14 · 16 · 20 · 24 · 32 |
| Contraste texto | ≥ 4.5:1 (WCAG AA) |
| Cor primária | neutro escuro + 1 accent (azul/índigo) |
| Superfície | fundo off-white / dark slate |

## Comportamento

- Máx. 1 CTA primário por área
- Tabelas: zebra leve ou hover row
- Formulários: label acima, erro inline
- Navegação: sidebar ou top nav consistente
- Mobile: stack vertical, touch ≥ 44px

## Modos

| Mode | Aplicação deste arquivo |
|------|-------------------------|
| GREENFIELD | Total |
| HYBRID | Parcial — respeitar DS existente |
| LEGACY | **Não aplicar** — preservar identidade |
