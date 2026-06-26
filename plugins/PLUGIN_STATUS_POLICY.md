# Plugin Status Policy — MCP Readiness

> Promover plugin apenas quando checklist completo. Sem secrets no repositório.

## Status válidos

`planned` · `draft` · `under-review` · `active` · `deprecated` · `disabled` · `removed`

## draft → under-review

Requer:

- [ ] MCP.md completo (servers, env vars, escopo)
- [ ] SECURITY.md
- [ ] PERMISSIONS.md
- [ ] ENV.example
- [ ] MCP_CONFIG_CURSOR.example.json
- [ ] MCP_CONFIG_CODEX.example.toml
- [ ] USAGE.md
- [ ] HEALTH.md
- [ ] Risco classificado
- [ ] capability_id pai no Registry

## under-review → active

Requer **todos** acima **mais**:

- [ ] Uso documentado (USAGE.md + EXAMPLES.md)
- [ ] Revisão humana aprovada
- [ ] Nenhum secret no repositório
- [ ] Produção: read-only por padrão (exceto aprovação explícita para write)
- [ ] Entrada em MCP_SERVER_CATALOG.md

## Nunca promover para active se

- Faltam arquivos de conector
- Risco high/critical sem política de aprovação documentada
- MCP real não validado localmente pelo usuário (framework não testa credenciais)

## Referências

- `plugins/MCP_READINESS_AUDIT.md`
- `rules/mcp-security.md`
- `checklists/mcp-readiness.md`
