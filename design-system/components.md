# Catálogo de Componentes

> Reutilizar **sempre** componentes do projeto antes de criar novos. Skill: `component-library`.

## Prioridade de reuso

1. Componentes do projeto (`shared/`, `ui/`, lib do framework UI)
2. Design System documentado do cliente
3. Tokens desta pasta (Greenfield)
4. Novo componente — somente se gap real e aprovado no WC

## Mapeamento típico (Angular/React)

| Padrão | Buscar em |
|--------|-----------|
| Button | `*button*` |
| Input/Form | `*form*`, `*input*` |
| Table | `*table*`, `*grid*` |
| Modal/Dialog | `*dialog*`, `*modal*` |
| Card | `*card*` |
| Toast/Snackbar | `*toast*`, `*snackbar*` |

## Registro no Working Context

- `Componentes reutilizados: [...]`
- `Componentes novos propostos: [...]` (justificar)
