# Instalação — AI Engineering Framework

> Repositório sugerido: `ai-engineering-framework` (Git independente).
> Consumidores instalam via **Git Submodule** sem copiar arquivos manualmente.

## Caminhos suportados

| Caminho no projeto consumidor | Uso |
|-------------------------------|-----|
| `.ai/` | Curto, oculto, recomendado para monorepos |
| `ai-engineering-framework/` | Explícito, bom para documentação |
| `Personal-AI/` | **Legado** — mantido no Umbra e projetos já integrados |

O conteúdo é idêntico; apenas o nome da pasta muda. Ajuste os paths nos exemplos abaixo.

---

## Instalar (submodule)

```bash
# Opção A — pasta .ai/ (recomendado)
git submodule add https://github.com/dkerson/ai-engineering-framework.git .ai

# Opção B — pasta explícita
git submodule add https://github.com/dkerson/ai-engineering-framework.git ai-engineering-framework
```

No `AGENTS.md` do projeto consumidor:

```markdown
## AI Engineering Framework

**Bootstrap obrigatório:** ler [.ai/AGENTS.md](.ai/AGENTS.md) e executar `.ai/skills/orchestrator/SKILL.md` antes de qualquer tarefa.

O Orchestrator é o único agente que conversa com o usuário.
```

Preencha o contexto do **seu** projeto (não use o exemplo Umbra):

```bash
cp .ai/context/_template/*.md .ai/context/
# Edite architecture.md, tech-stack.md, domain.md, etc.
```

---

## Clonar projeto que já usa submodule

```bash
git clone --recurse-submodules https://github.com/sua-org/seu-projeto.git
```

Ou após clone normal:

```bash
git submodule update --init --recursive
```

---

## Atualizar framework (sem alterar o consumidor)

```bash
cd .ai
git fetch origin
git checkout v2.0.0   # ou tag desejada — ver docs/VERSIONING.md
cd ..
git add .ai
git commit -m "chore: atualiza AI Engineering Framework para v2.0.0"
```

O código do projeto consumidor **não** muda — apenas o ponteiro do submodule.

---

## Trocar versão

```bash
cd .ai
git fetch --tags
git checkout v1.0.0    # downgrade
# ou
git checkout main      # última versão (cuidado em produção)
cd ..
git add .ai && git commit -m "chore: framework v1.0.0"
```

Consulte `CHANGELOG.md` do framework antes de trocar versão major.

---

## Remover

```bash
git submodule deinit -f .ai
git rm -f .ai
rm -rf .git/modules/.ai
```

Remova a seção do framework no `AGENTS.md` do consumidor.

---

## Alternativas (sem submodule)

| Método | Quando usar |
|--------|-------------|
| Cópia manual | Prototipagem rápida, fork pesado |
| Symlink Cursor | Skills globais em `~/.cursor/skills/` |
| Global Cursor | Ver `INTEGRATION.md` |

Submodule é o método recomendado para múltiplos projetos (Umbra, RIFSMART, APIs, etc.).

---

## Verificação pós-instalação

1. `AGENTS.md` do projeto referencia o framework
2. `context/tech-stack.md` preenchido com a stack real
3. Teste: `"O que faz este projeto?"` → modo **Fast**
4. Resposta segue `templates/final-response.md`
