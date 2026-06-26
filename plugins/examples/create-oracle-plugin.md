# Exemplo: Criar plugin Oracle

> Demonstra o fluxo completo sem implementar integração real.

## Pedido do usuário

"Crie um plugin para Oracle."

## Pipeline

```text
Orchestrator (Standard)
  → Plugin Builder
  → Plugin Manager (validação)
  → FOS Update
```

## Passos do Plugin Builder

1. Verificar `PLUGIN_REGISTRY.md` — não existe `oracle-plugin`.
2. Copiar estrutura de `PLUGIN_TEMPLATE.md` para `plugins/oracle-plugin/`.
3. Preencher manifesto:

| Campo | Valor |
|-------|-------|
| ID | oracle-plugin |
| Tipo | database |
| Access | read-write |
| Risco | high |
| MCP | oracle |

4. Documentar env vars em `MCP.md`: `ORACLE_CONNECTION_STRING`, `ORACLE_USER`, `ORACLE_PASSWORD` (sem valores).
5. Listar ações destrutivas em `SECURITY.md`: DDL, DML em produção, drop.
6. Registrar em `PLUGIN_REGISTRY.md` com status `draft`, lifecycle `implemented`.
7. Atualizar FOS.

## Validação Plugin Manager

- [ ] Estrutura completa (11 arquivos)
- [ ] Sem secrets
- [ ] Sem duplicação com postgres-plugin ou sqlserver-plugin (tipo similar, serviço distinto — OK)
- [ ] Permissões e riscos declarados
- [ ] EXAMPLES.md presente

## Resultado esperado

Plugin `oracle-plugin` disponível para ativação em projetos; integração MCP real permanece backlog.
