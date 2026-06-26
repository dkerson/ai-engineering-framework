# Plugin Architecture — AI Engineering Framework

> Caminho canônico: `.ai/plugins/` (ou `Personal-AI/plugins/` em instalações legadas).

## Objetivo

Estender o AI Engineering Framework **sem inflar o núcleo**. Integrações com serviços, bancos, ferramentas, MCPs e providers vivem em **pacotes independentes**, versionados, documentados e controlados pelo Master Orchestrator.

## Princípios

| Princípio | Regra |
|-----------|-------|
| Core limpo | Skills e rules do núcleo não duplicam lógica de integração |
| Independência | Cada plugin é autocontido e pode evoluir separadamente |
| Segurança | Sem secrets; variáveis de ambiente; aprovação para ações destrutivas |
| Governança | Plugin Registry + Framework Operating System registram todo ciclo de vida |
| Economia | Carregar somente o plugin necessário para a missão |

## Estrutura

```text
plugins/
├── README.md                 ← este arquivo
├── PLUGIN_POLICY.md          ← política global
├── PLUGIN_REGISTRY.md        ← registro central
├── PLUGIN_TEMPLATE.md        ← template para novos plugins
├── PLUGIN_LIFECYCLE.md       ← ciclo de vida
├── examples/                 ← exemplos de uso
└── {plugin-name}/
    ├── README.md
    ├── PLUGIN.md
    ├── SKILLS.md
    ├── RULES.md
    ├── TEMPLATES.md
    ├── CHECKLISTS.md
    ├── WORKFLOWS.md
    ├── MCP.md
    ├── SECURITY.md
    ├── EXAMPLES.md
    └── CHANGELOG.md
```

## Componentes do framework

| Componente | Papel |
|------------|-------|
| **Plugin Manager** | Cadastrar, atualizar, listar, desativar, validar plugins |
| **Plugin Resolver** | Identificar plugin necessário na missão; verificar permissões e riscos |
| **Plugin Builder** | Criar novos plugins no padrão; registrar no Registry e FOS |
| **Master Orchestrator** | Orquestra plugins via Plugin Resolver |
| **Project Registry** | Associa plugins ativos/desativados por projeto |
| **Infrastructure Intelligence** | Consulta plugins antes de sugerir conexões |
| **Framework Operating System** | Registra mudanças de status e saúde |

## Status de plugin

`planned` · `draft` · `active` · `deprecated` · `disabled` · `removed`

## Comandos naturais suportados

- Cadastre um plugin para Power BI.
- Ative o plugin do GitHub para o projeto Umbra.
- Quais plugins o Irisys usa?
- Desative o plugin do Sentry.
- Crie um plugin para Oracle.
- Liste plugins ativos.
- Quais plugins têm permissão de escrita?
- Quais plugins têm risco alto?

## Referências

- `docs/MCP_GOVERNANCE.md`
- `plugins/MCP_READINESS_AUDIT.md`
- `plugins/PLUGIN_STATUS_POLICY.md`
- `infrastructure/registry/MCP_SERVER_CATALOG.md`
