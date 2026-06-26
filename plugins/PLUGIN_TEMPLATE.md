# Plugin Template — Criar Novo Plugin

> Use com `skills/plugin-builder/SKILL.md`. Copie esta estrutura; não implemente integração real até aprovação.

## Nomenclatura

- Pasta: `{service}-plugin` (kebab-case)
- Exemplos: `github-plugin`, `oracle-plugin`, `stripe-plugin`

## Estrutura obrigatória

```text
plugins/{plugin-name}/
├── README.md          ← visão geral e quick start
├── PLUGIN.md          ← manifesto: status, versão, tipo, permissões, riscos
├── SKILLS.md          ← skills que o plugin expõe ou consome
├── RULES.md           ← regras específicas do plugin
├── TEMPLATES.md       ← templates gerados pelo plugin
├── CHECKLISTS.md      ← checklists de validação
├── WORKFLOWS.md       ← workflows acionados pelo plugin
├── MCP.md             ← MCPs suportados e env vars (sem valores reais)
├── SECURITY.md        ← política de segurança e ações destrutivas
├── EXAMPLES.md        ← cenários de uso
└── CHANGELOG.md       ← histórico de versões
```

## PLUGIN.md — manifesto

```markdown
# {Nome Legível} Plugin

| Campo | Valor |
|-------|-------|
| ID | {plugin-name} |
| Versão | 0.1.0 |
| Status | draft |
| Lifecycle | proposed |
| Tipo | {vcs|database|bi|...} |
| Access | read-only | read-write | admin |
| Risco | low | medium | high | critical |
| Owner | {equipe ou framework} |

## Propósito

[Uma frase: o que este plugin integra]

## Dependências

- [outros plugins ou MCPs]

## Permissões declaradas

- [escopo:recurso:ação]

## Projetos associados

- [projeto ou "nenhum ainda"]
```

## MCP.md — padrão

```markdown
# MCP

## Supported MCP Servers

- {server-name}

## Required Environment Variables

- {VAR_NAME}

## Optional Environment Variables

- {VAR_NAME}

> Nunca incluir valores reais.
```

## SECURITY.md — padrão

```markdown
# Security

## Access Mode

read-only | read-write | admin

## Risk Level

low | medium | high | critical

## Destructive Actions (require approval)

- [lista]

## Prohibited

- Armazenar secrets no repositório
- Executar {ação} sem aprovação explícita
```

## Registro pós-criação

1. Adicionar entrada em `plugins/PLUGIN_REGISTRY.md`
2. Atualizar FOS (`IMPLEMENTED.md`, `CHANGELOG.md`, `FRAMEWORK_STATUS.md`)
3. Se associado a projeto: criar/atualizar `PROJECT_PLUGINS.md`
4. Registrar em `workflows/_index.md` se novo tipo de missão
5. Plugin Manager valida duplicação e documentação

## Referências

- `plugins/PLUGIN_POLICY.md`
- `plugins/PLUGIN_LIFECYCLE.md`
- `plugins/examples/create-oracle-plugin.md`
