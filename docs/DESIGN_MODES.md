# Design Modes

Três modos de operação para interface. O Orchestrator escolhe **um** por tarefa.

## LEGACY MODE

**Quando:** projeto existente, legado, manutenção, bug, pequenas melhorias.

**Preservar:** layout, componentes, identidade, cores, tipografia, espaçamentos.

**Melhorar somente:** acessibilidade, organização, responsividade, consistência, UX pontual.

**Proibido:** redesenhar, trocar componentes, mudar identidade.

Checklist: `checklists/design/legacy.md`

## HYBRID MODE

**Quando:** sistema existente com evolução gradual permitida.

**Permitido:** hierarquia, espaçamento, tipografia, organização, responsividade, mobile, a11y — sem descaracterizar.

Checklist: `checklists/design/hybrid.md`

## GREENFIELD MODE

**Quando:** novo projeto, módulo, produto, app ou área independente.

**Aplicar:** Design DNA + `design-system/` (se sem identidade do projeto).

Checklist: `checklists/design/greenfield.md`

## Detecção automática

| Sinal | Modo provável |
|-------|---------------|
| "corrigir bug", "typo", "legado" | LEGACY |
| "melhorar tela", "modernizar gradualmente" | HYBRID |
| "novo módulo", "do zero", "novo app" | GREENFIELD |

Usuário pode forçar modo explicitamente.

## Regra absoluta

Alterar identidade visual **somente** com pedido explícito — em qualquer modo.

Rules: `rules/design/design-modes.md` · `rules/design/visual-identity.md`
