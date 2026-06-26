# Exemplo: MCP Mission

**Pedido:** "Quais MCPs a Umbra precisa?"

**Pipeline:** mcp-discovery-specialist → projects/umbra/mcp/

**Resposta:** user-mssql, github, docker (under-review).

---

**Pedido:** "Gere mcp.example.json para Cursor."

**Output:** `Personal-AI/.cursor/mcp.example.json` (copiar localmente).

---

**Pedido:** "Promova sqlserver-plugin para active."

**Pipeline:** plugin-manager → PLUGIN_STATUS_POLICY checklist → **bloqueado** até validação humana MCP local.
