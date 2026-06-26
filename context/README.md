# Context — Projeto consumidor

> O framework é **agnóstico**. Os arquivos aqui definem o **projeto em execução**, não o framework.

## Arquivos

| Arquivo | Conteúdo |
|---------|----------|
| `architecture.md` | Camadas, módulos, diagramas |
| `tech-stack.md` | Linguagens, frameworks, versões |
| `domain.md` | Entidades, regras de negócio |
| `coding-standards.md` | Convenções do time |
| `business.md` | Glossário, personas |
| `patterns.md` | Padrões recorrentes do projeto |
| `working-context.md` | **Especificação** do Working Context (não editar por tarefa) |
| `design-dna.md` | Design DNA do projeto — modo, tokens, componentes (v2.7+) |
| `semantic-layer/` | Camada semântica — conceitos de negócio → tabelas/APIs/telas (v2.1+) |

## Novo projeto

1. Copie `context/_template/` para `context/`
2. Preencha com dados reais
3. **Não** commite segredos

## Projeto Umbra (exemplo)

Neste monorepo, `context/` está preenchido com dados do **Umbra** (Angular 19 + .NET 8). Outros consumidores (RIFSMART, APIs, etc.) substituem estes arquivos pelos seus.

## Precedência

1. `AGENTS.md` do projeto consumidor
2. `context/` do projeto consumidor
3. `context/_template/` (somente referência)
