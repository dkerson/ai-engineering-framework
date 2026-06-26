# Plugin Policy — Rule

> Espelho executável de `plugins/PLUGIN_POLICY.md`. Skills de plugin devem referenciar este arquivo.

## Regras

1. Plugin **nunca** armazena secrets — apenas placeholders e nomes de env vars.
2. Plugin **deve** usar variáveis de ambiente documentadas em `MCP.md`.
3. Plugin **deve** declarar permissões em `PLUGIN.md` e `SECURITY.md`.
4. Plugin **deve** declarar risco (`low` | `medium` | `high` | `critical`).
5. Plugin **deve** declarar `access_mode` (`read-only` | `read-write` | `admin`).
6. Ações destrutivas exigem **aprovação explícita** do usuário antes da execução.
7. Plugin **deve** estar documentado (11 arquivos obrigatórios).
8. Plugin **deve** ser independente do core — sem alterar interfaces públicas sem necessidade.
9. Plugin **não pode** duplicar responsabilidade de outro plugin — validar via Plugin Manager.
10. Plugin **deve** seguir economia de tokens — carregar só arquivos necessários.

## Ações destrutivas

push · merge · deploy · migration · delete · update em banco · alteração em task · alteração em produção · exclusão de recurso · alteração de permissão

## Enforcement

| Skill | Quando |
|-------|--------|
| plugin-builder | Na criação |
| plugin-manager | No cadastro/atualização |
| plugin-resolver | Antes da execução |
| security-review | Ações destrutivas ou risco alto |
| risk-reviewer | Risco high/critical |

## Referências

- `plugins/PLUGIN_POLICY.md`
- `rules/infrastructure-secrets.md`
- `rules/token-economy.md`
