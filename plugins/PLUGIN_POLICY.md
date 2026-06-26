# Plugin Policy — Política Global

> Toda integração externa deve seguir esta política. Violações bloqueiam ativação ou execução.

## Regras obrigatórias

### 1. Plugin nunca pode armazenar secrets

- Proibido commitar tokens, senhas, connection strings reais ou chaves privadas.
- Usar placeholders (`${VAR}`, `<SECRET>`, `env:VAR_NAME`) na documentação.
- Credenciais reais ficam em Secret Manager, CI ou ambiente local do usuário.

### 2. Plugin deve usar variáveis de ambiente

- Toda credencial referenciada via nome de variável documentado em `MCP.md`.
- Exemplo: `GITHUB_TOKEN`, `POSTGRES_DATABASE_URL`, `SENTRY_AUTH_TOKEN`.
- Nunca incluir valores reais em arquivos do framework.

### 3. Plugin deve declarar permissões

- Documentar escopo em `PLUGIN.md` e `SECURITY.md`.
- Classificar: `read-only`, `read-write`, `admin`.
- Listar recursos afetados (repos, tabelas, issues, deploys, etc.).

### 4. Plugin deve declarar riscos

- Nível: `low`, `medium`, `high`, `critical`.
- Descrever impacto de falha ou uso indevido.
- Registrar no Plugin Registry.

### 5. Plugin deve declarar acesso read/write

- Campo explícito `access_mode` em `PLUGIN.md`.
- Plugins `read-write` ou `admin` exigem validação extra no Plugin Resolver.

### 6. Aprovação antes de ações destrutivas

Ações que **sempre** exigem aprovação explícita do usuário:

- push · merge · deploy · migration · delete
- update em banco · alteração em task · alteração em produção
- exclusão de recurso · alteração de permissão

O Plugin Resolver aciona `security-review` e `risk-reviewer` antes de encaminhar ao Orchestrator.

### 7. Plugin deve ser documentado

- Todos os arquivos obrigatórios presentes (ver `PLUGIN_TEMPLATE.md`).
- `README.md` com propósito, status e quick start.
- `EXAMPLES.md` com pelo menos um cenário de uso.

### 8. Plugin deve ser independente do core

- Não alterar skills, rules ou workflows do núcleo sem necessidade.
- Não duplicar responsabilidade de outro plugin ou skill core.
- Integrar via Plugin Registry e contratos documentados.

### 9. Plugin não pode duplicar responsabilidade

- Antes de criar plugin, consultar `PLUGIN_REGISTRY.md`.
- Plugin Manager valida overlap; conflitos vão para FOS `under-review/`.
- Preferir estender plugin existente a criar duplicata.

### 10. Plugin deve seguir economia de tokens

- Carregar somente arquivos do plugin necessários à missão.
- Referenciar docs longas por link; não inline no Working Context.
- Seguir `rules/token-economy.md`.

### 11. Plugin deve pertencer a uma Capability (COS)

- Todo plugin declara `capability_id` responsável no Plugin Registry.
- Plugin **nunca** existe sem capability pai.
- Ver `capabilities/registry/CAPABILITY_REGISTRY.md` (seção Plugin → Capability).

## Enforcement

| Camada | Ação |
|--------|------|
| Plugin Builder | Valida estrutura e política na criação |
| Plugin Manager | Valida no cadastro/atualização |
| Plugin Resolver | Verifica permissões e risco antes da execução |
| Orchestrator | Bloqueia execução sem aprovação em ações destrutivas |
| FOS | Audita violações e registra decisões |

## Referências

- `rules/plugin-policy.md`
- `rules/infrastructure-secrets.md`
- `checklists/plugin-health.md`
- `plugins/PLUGIN_LIFECYCLE.md`
