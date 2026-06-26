---
name: plugin-builder
description: >-
  Cria novos plugins seguindo o padrão do framework: estrutura, documentação, templates, checklists, rules, exemplos e registro no Plugin Registry e FOS. Invocado somente pelo Orchestrator em expansão do framework.
---

# Plugin Builder

## Objetivo

Gerar pacotes de plugin independentes, documentados e registrados — **sem implementar integração real** até aprovação explícita.

## Quando usar

- "Crie um plugin para Oracle/Stripe/Jira..."
- Expansão do framework com nova integração planejada
- Infrastructure Intelligence sugere plugin inexistente

## Quando NÃO usar

- Ativar plugin em projeto (usar `plugin-manager`)
- Resolver plugin em missão (usar `plugin-resolver`)
- Implementar código MCP ou conectores reais (backlog pós-aprovação)

## Responsabilidades

1. Verificar duplicação em `PLUGIN_REGISTRY.md`.
2. Copiar estrutura de `PLUGIN_TEMPLATE.md` para `plugins/{name}/`.
3. Preencher os 11 arquivos obrigatórios do plugin.
4. Declarar permissões, riscos, access mode e MCP em `PLUGIN.md` / `SECURITY.md` / `MCP.md`.
5. Criar `EXAMPLES.md` com pelo menos um cenário.
6. Registrar entrada completa em `PLUGIN_REGISTRY.md` (status `draft`, lifecycle `implemented`).
7. Atualizar FOS: `IMPLEMENTED.md`, `CHANGELOG.md`, `FRAMEWORK_STATUS.md`.
8. Solicitar validação via `plugin-manager`.

## Orquestração hierárquica

- **Invocação:** Orchestrator ou Recommendation Engine via FOS
- **Working Context:** nome proposto, tipo, MCP, risco
- **Economia:** usar template; não duplicar policy global inline

## Artefatos obrigatórios por plugin

| Arquivo | Conteúdo mínimo |
|---------|-----------------|
| README.md | Propósito, status, quick start |
| PLUGIN.md | Manifesto completo |
| SKILLS.md | Skills planejadas |
| RULES.md | Regras específicas + link policy global |
| TEMPLATES.md | Templates placeholder |
| CHECKLISTS.md | Ativação e pré-execução |
| WORKFLOWS.md | Workflows acionados |
| MCP.md | Servers + env vars (sem valores) |
| SECURITY.md | Risco, access, ações destrutivas |
| EXAMPLES.md | ≥1 cenário |
| CHANGELOG.md | v0.1.0 inicial |

## Checklist

- [ ] Nome `{service}-plugin` em kebab-case
- [ ] 11 arquivos presentes
- [ ] Sem secrets
- [ ] Permissões e riscos declarados
- [ ] Registry atualizado
- [ ] FOS atualizado
- [ ] plugin-manager validou duplicação

## Integração com outras skills

- **Upstream:** orchestrator, recommendation-engine (FOS)
- **Downstream:** plugin-manager (validação e ativação)

## Exemplos

**Input:** "Crie um plugin para Oracle."

**Output:** `plugins/oracle-plugin/` completo; Registry; FOS; ver `plugins/examples/create-oracle-plugin.md`.

## Referências

- `plugins/PLUGIN_TEMPLATE.md`
- `plugins/PLUGIN_POLICY.md`
- `plugins/PLUGIN_LIFECYCLE.md`
- `skills/skill-builder/SKILL.md`
