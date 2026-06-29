# Checklist: Authorization

- [ ] Subject, tenant, resource e action identificados
- [ ] RBAC/ABAC/misto definido
- [ ] Backend aplica autorizacao antes da acao
- [ ] UI nao e fonte de autorizacao
- [ ] Queries filtram tenant/org antes de negocio
- [ ] Admin scopes separados de scopes comuns
- [ ] Acoes destrutivas revalidam permissao
- [ ] Mudancas de permissao geram auditoria
- [ ] Casos deny testados
