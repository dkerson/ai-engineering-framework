# Checklist: Plugin Health

> Usado por Plugin Manager e Framework Reviewer.

## Registry

- [ ] `PLUGIN_REGISTRY.md` atualizado
- [ ] Todos os plugins com status coerente
- [ ] Versões semver documentadas

## Por plugin

- [ ] 11 arquivos obrigatórios presentes
- [ ] `PLUGIN.md` com permissões e risco
- [ ] `MCP.md` sem valores reais de secrets
- [ ] `SECURITY.md` com ações destrutivas listadas
- [ ] `EXAMPLES.md` com ≥1 cenário
- [ ] Owner definido
- [ ] Sem duplicação de responsabilidade

## Operacional

- [ ] Plugins ativos têm MCP definido (ou explicitamente N/A)
- [ ] Plugins high/critical têm risk-reviewer no fluxo
- [ ] PROJECT_PLUGINS.md sincronizado por projeto
- [ ] Mudanças de status registradas no FOS

## Relatório

Gerar ou atualizar `framework/operating-system/health/PLUGIN_HEALTH.md`.
