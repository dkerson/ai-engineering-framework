# Permission Cache

> Regras para cachear permissoes em memoria, sessao, claims, edge, Redis ou camada local.

## Regra central

Cache de permissao e otimizacao, nao autoridade final. Quando houver duvida, falhar fechado.

## Chave de cache

A chave deve incluir, quando aplicavel:

- `user_id`
- `tenant_id` ou `org_id`
- `role_version` ou `permission_version`
- `session_id` ou `token_id`
- `environment`
- `resource_scope` quando a permissao nao for global

## Invalidacao obrigatoria

Invalidar quando mudar:

- role, grupo, cargo, plano, feature flag ou tenant;
- status do usuario ou sessao;
- ownership de recurso;
- policy ou matriz de permissoes;
- vinculo usuario-org;
- revogacao administrativa;
- suspeita de comprometimento.

## TTL e consistencia

- TTL curto para permissoes sensiveis.
- Sem TTL infinito.
- Revalidar antes de delete, approve, payout, export, permission update, deploy ou acao admin.
- Usar versao de permissao para evitar stale access.
- Preferir cache local por usuario/tenant a cache global.

## Fail-closed

Falhas de cache, lookup, parse, rede ou fonte autoritativa devem resultar em `deny` para acoes protegidas.

## O que nao cachear

- Secrets.
- Tokens completos quando hash/identificador basta.
- PII desnecessaria.
- Decisoes de permissao sem tenant.
- Permissoes administrativas sem versao/expiracao.
