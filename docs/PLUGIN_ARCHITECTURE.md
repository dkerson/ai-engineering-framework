# Plugin Architecture

> v2.8.0 — extensibilidade por pacotes independentes sem inflar o núcleo.

## Visão geral

O AI Engineering Framework separa **núcleo** (Orchestrator, SIL, FOS, domínios) de **integrações** (plugins). Cada plugin é um pacote versionado em `plugins/{name}/` com documentação, MCP, segurança e registro central.

```text
Usuário
    ↓
SIL (Mission)
    ↓
Master Orchestrator
    ↓
Plugin Resolver ──→ Plugin Registry
    ↓                      ↑
Plugin ativo          Plugin Manager
    ↓                      ↑
MCP + Domínio         Plugin Builder
    ↓
Project Registry (PROJECT_PLUGINS.md)
    ↓
Infrastructure Intelligence (descoberta → plugin)
    ↓
FOS (auditoria de mudanças)
```

## Componentes

| Componente | Skill/Artefato | Responsabilidade |
|------------|----------------|------------------|
| Plugin Registry | `plugins/PLUGIN_REGISTRY.md` | Fonte canônica de metadados |
| Plugin Policy | `plugins/PLUGIN_POLICY.md` | 10 regras globais |
| Plugin Lifecycle | `plugins/PLUGIN_LIFECYCLE.md` | Estados e transições FOS |
| Plugin Manager | `skills/plugin-manager/` | CRUD operacional |
| Plugin Resolver | `skills/plugin-resolver/` | Seleção na missão |
| Plugin Builder | `skills/plugin-builder/` | Criação de novos pacotes |
| Plugin Health | `framework/operating-system/health/PLUGIN_HEALTH.md` | Relatório de saúde |

## Como o Orchestrator decide usar plugins

1. **Classificar** demanda (`integration`, `infrastructure-mission`, `database`, `devops`, etc.).
2. **Detectar sinais** de serviço externo (GitHub, PostgreSQL, Sentry, Azure...).
3. **Invocar Plugin Resolver** antes de MCP ou skills de integração.
4. Plugin Resolver consulta Registry + `PROJECT_PLUGINS.md`.
5. Se `draft`: documentação e planejamento OK; execução MCP bloqueada.
6. Se `active` + permissões OK: encaminhar ao domínio (Data, Dev, Infra).
7. Se ação destrutiva: pausar para aprovação explícita.
8. Infrastructure Intelligence usa o mesmo fluxo na descoberta (ex.: PostgreSQL → `postgres-plugin`).

## Integração Project Registry

Cada projeto pode ter `PROJECT_PLUGINS.md`:

```markdown
# Project Plugins — Irisys

## Active Plugins
- github-plugin
- sqlserver-plugin

## Disabled Plugins
- sentry-plugin
```

Ver `docs/Project-Registry.md`.

## Integração Infrastructure Intelligence

Antes de sugerir conexão:

1. Detectar tecnologia (PostgreSQL, Docker, Azure...).
2. Consultar `PLUGIN_REGISTRY.md`.
3. Se existir: registrar uso no projeto; Plugin Resolver na missão.
4. Se não existir: sugerir `plugin-builder`; registrar em FOS backlog.

## Segurança

- Plugins nunca armazenam secrets.
- Ações destrutivas exigem aprovação (ver `PLUGIN_POLICY.md`).
- Plugin Resolver aciona `security-review` + `risk-reviewer` quando necessário.

## Referências

- `plugins/README.md`
- `workflows/plugin-mission.md`
- `rules/plugin-policy.md`
- `checklists/plugin-health.md`
