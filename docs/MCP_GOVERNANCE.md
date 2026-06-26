# MCP Governance

> Framework v2.11.0 — uso governado de MCP por plugin, capability e projeto.

## Princípios

- Credenciais via **variáveis de ambiente** ou Secret Manager — nunca no repo.
- **Plugin** conecta serviço; **Capability** define competência; **Projeto** declara perfil MCP.
- Framework gera **exemplos** (`*.example.json`, `ENV.example`) — usuário copia localmente.

## Artefatos

| Artefato | Local |
|----------|-------|
| Catálogo global | `infrastructure/registry/MCP_SERVER_CATALOG.md` |
| Conector plugin | `plugins/{name}/MCP*.example.*`, `ENV.example` |
| Perfil projeto | `projects/{project}/mcp/` |
| Cursor exemplo | `.cursor/mcp.example.json` |
| Codex exemplo | `.codex/config.example.toml` |
| Audit | `plugins/MCP_READINESS_AUDIT.md` |

## Skills

- `mcp-discovery-specialist` — discovery por projeto
- `plugin-manager` — promoção de status
- `plugin-resolver` — seleção na missão
- `infrastructure-discovery` — sinais de infra

## Workflow

`workflows/mcp-mission.md`

## Referências

- `rules/mcp-security.md`
- `plugins/PLUGIN_STATUS_POLICY.md`
