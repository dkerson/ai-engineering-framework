# Alterações Seguras em Banco

Qualquer alteração em banco exige:

- [ ] Análise de impacto (`impact-analysis`)
- [ ] Plano de rollback
- [ ] Validação em ambiente seguro
- [ ] Cuidado com dados financeiros
- [ ] Cuidado com produção
- [ ] Proibir UPDATE/DELETE sem WHERE
- [ ] Evitar migrations destrutivas
- [ ] Validar cardinalidade antes de alterar joins
- [ ] Validar impacto em relatórios existentes

Skills: `dba-reviewer` antes de aplicar em produção.
