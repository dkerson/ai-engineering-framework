# MCP Security Rules

## Portabilidade obrigatoria

- Templates MCP compartilhados nao podem depender de `C:\Users\{outro_usuario}\...`.
- Usar `npx`, MCP remoto OAuth ou variaveis de ambiente para paths inevitaveis.
- Ver `rules/mcp-portability.md`.

> Obrigatório para plugins, projetos e agentes. Complementa `rules/infrastructure-secrets.md`.

## Proibido

1. **Nunca** armazenar secrets no repositório (tokens, passwords, connection strings reais).
2. **Nunca** commitar `.env` com valores reais.
3. **Nunca** commitar `.cursor/mcp.json` com tokens reais — usar `mcp.example.json` + env.
4. **Nunca** commitar `.codex/config.toml` com tokens reais — usar `config.example.toml` + env.
5. **Nunca** configurar credenciais reais via agente sem pedido explícito do usuário.

## Produção

6. **Produção read-only por padrão** — writes exigem aprovação explícita.
7. **Escrita em banco** (INSERT/UPDATE/DELETE/DDL) exige aprovação explícita.
8. **push / merge / deploy** exige pedido explícito.

## Ferramentas de produtividade

9. **ClickUp / Jira** — não alterar status de task sem pedido explícito.

## Escopo MCP

10. **MCP remoto** — escopo mínimo (least privilege).
11. **MCP local** — revisar comando e permissões antes de ativar.

## Enforcement

| Camada | Ação |
|--------|------|
| plugin-resolver | Verifica PERMISSIONS.md antes de write |
| mcp-discovery-specialist | Classifica risco; não configura secrets |
| Plugin Manager | Bloqueia active sem checklist |
| Orchestrator | Pausa ações destrutivas |

## Referências

- `plugins/PLUGIN_POLICY.md`
- `docs/MCP_GOVERNANCE.md`
