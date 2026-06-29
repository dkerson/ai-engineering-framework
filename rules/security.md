# Security

## Guardrail anti-hardcode

- Secrets, tokens e connection strings nunca ficam no codigo.
- IDs de tenant, cliente, usuario, role, permissao ou escopo nao devem ser hardcoded.
- Ver tambem `rules/no-hardcode.md`.

> Finalidade: seguranca em codigo, infra, acesso e operacao.

## Regras

- Validar toda input externa.
- Usar parameterized queries; nunca concatenar SQL.
- Secrets em env/vault; nunca no codigo.
- Aplicar principio do menor privilegio.
- Usar HTTPS; cookies secure/httpOnly quando aplicavel.
- Autorizacao sempre no backend antes da acao protegida.
- Tenant isolation antes de filtro de negocio.
- Cache de permissao deve ter TTL, invalidacao e fail-closed.
- Acoes destrutivas exigem revalidacao de permissao.
- Logs de auditoria nao devem expor secrets ou PII desnecessaria.

## Complementos

- `rules/security-access-control.md`
- `rules/permission-cache.md`
- `rules/threat-modeling.md`
- `rules/mcp-security.md`
- `rules/infrastructure-secrets.md`
