# Checklist: Permission Cache

- [ ] Cache key inclui user e tenant/org
- [ ] Cache key inclui role_version ou permission_version
- [ ] TTL curto definido
- [ ] Invalidacao cobre role, tenant, plano, status, sessao e policy
- [ ] Falha de cache resulta em deny
- [ ] Acoes destrutivas revalidam permissao server-side
- [ ] Sem secrets ou tokens completos no cache
- [ ] Teste de stale permission planejado
- [ ] Auditoria cobre alteracao e negacao relevante
