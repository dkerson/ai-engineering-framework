# Plugin Lifecycle — Ciclo de Vida

> Toda mudança de status deve ser registrada no Framework Operating System.

## Estados do ciclo de vida (desenvolvimento)

```text
proposed
    ↓
reviewed
    ↓
approved
    ↓
implemented
    ↓
active
    ↓
deprecated
    ↓
removed
```

| Estado | Descrição | Quem registra |
|--------|-----------|---------------|
| **proposed** | Ideia ou necessidade identificada | Plugin Builder / Recommendation Engine |
| **reviewed** | Estrutura e política revisadas | Plugin Manager + Framework Reviewer |
| **approved** | Usuário aprovou criação ou ativação | FOS `DECISIONS.md` |
| **implemented** | Arquivos criados; integração documentada | Plugin Builder |
| **active** | Disponível para resolução em missões | Plugin Manager |
| **deprecated** | Substituído ou obsoleto; ainda legível | Plugin Manager |
| **removed** | Removido do registry; histórico preservado no FOS | Plugin Manager |

## Estados operacionais (registry)

Complementares ao ciclo de vida; usados em `PLUGIN_REGISTRY.md`:

| Status | Descrição |
|--------|-----------|
| `planned` | Planejado; estrutura mínima ou ausente |
| `draft` | Estrutura criada; integração não implementada |
| `active` | Operacional no projeto ou globalmente |
| `deprecated` | Não recomendado para novos usos |
| `disabled` | Desativado em projeto específico |
| `removed` | Retirado; entrada histórica no FOS |

## Transições que exigem FOS

Toda transição entre estados operacionais ou de ciclo de vida atualiza:

- `framework/operating-system/FRAMEWORK_STATUS.md`
- `framework/operating-system/CHANGELOG.md`
- `framework/operating-system/IMPLEMENTED.md` (quando implementado)
- `framework/operating-system/DECISIONS.md` (quando aprovado)
- `framework/operating-system/ROADMAP.md` (quando aplicável)
- `framework/operating-system/BACKLOG.md` (quando aplicável)
- `framework/operating-system/FRAMEWORK_HEALTH.md`
- `plugins/PLUGIN_REGISTRY.md`

## Fluxo resumido

```text
Usuário ou SIL identifica necessidade
    → Plugin Builder propõe (proposed)
    → Plugin Manager revisa (reviewed)
    → Usuário aprova (approved) → FOS
    → Plugin Builder implementa estrutura (implemented)
    → Plugin Manager ativa (active) → Registry + Project Registry
    → Uso em missões via Plugin Resolver
    → Deprecação ou remoção com histórico preservado
```

## Referências

- `plugins/PLUGIN_POLICY.md`
- `skills/plugin-manager/SKILL.md`
- `skills/plugin-builder/SKILL.md`
- `docs/Framework-Operating-System.md`
