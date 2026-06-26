# Workflow: MCP Mission

> Preparar MCPs de forma segura — exemplos only, sem secrets.

## Trigger

Quais MCPs, prepare MCPs, mcp.example.json, config.example.toml, promova plugin, MCP risco alto, plugins draft, RAG pgvector, configure MCP sem secrets.

## Pipeline

```text
MCP Mission
→ project-resolver
→ mcp-discovery-specialist
→ plugin-resolver
→ plugin-manager* (promoção status)
→ MCP_SERVER_CATALOG update
→ MCP_READINESS_AUDIT / PLUGIN_HEALTH update
→ FOS*
```

## Modo

| Cenário | Modo |
|---------|------|
| Consultar MCPs, listar draft | Fast |
| Preparar perfil projeto | Standard |
| Promover plugin active | Standard → Review |

## Regras

- Nunca secrets no repo
- Nunca `.cursor/mcp.json` real commitado
- Promover active só com PLUGIN_STATUS_POLICY checklist
- Produção read-only default

## Skills

mcp-discovery-specialist, plugin-manager, plugin-resolver, project-resolver, security-review, validator

## Referências

- `docs/MCP_GOVERNANCE.md`
- `plugins/MCP_READINESS_AUDIT.md`
