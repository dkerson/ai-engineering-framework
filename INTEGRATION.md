# Integração — Codex / Cursor

> **AI Engineering Framework** (alias legado: Personal AI Framework)

## Método recomendado: Git Submodule

```bash
git submodule add https://github.com/dkerson/ai-engineering-framework.git .ai
```

Detalhes completos: [`docs/INSTALL.md`](docs/INSTALL.md) — instalar, atualizar, versionar, remover.

No `AGENTS.md` do projeto:

```markdown
## AI Engineering Framework

**Bootstrap obrigatório:** ler [.ai/AGENTS.md](.ai/AGENTS.md) e executar `.ai/skills/orchestrator/SKILL.md`.

O Orchestrator é o único agente que conversa com o usuário. Nenhuma skill auto-inicia.
```

Preencha `context/` com dados do **seu** projeto (`context/_template/` como base).

---

## Caminhos de instalação

| Pasta | Status |
|-------|--------|
| `.ai/` | Recomendado (submodule) |
| `ai-engineering-framework/` | Alternativa explícita |
| `Personal-AI/` | Legado — Umbra e projetos v1 |

---

## Opção: Cópia manual

Copie o diretório do framework para a raiz. Funciona, mas dificulta atualização isolada.

---

## Opção: Global (Cursor)

```powershell
Copy-Item -Recurse .ai\skills\* "$env:USERPROFILE\.cursor\skills\"
```

Mantenha o framework no repo para rules, workflows e context.

---

## Opção: Symlink

```powershell
New-Item -ItemType SymbolicLink -Path ".cursor\skills\orchestrator" -Target "..\..\.ai\skills\orchestrator"
```

---

## Codex (OpenAI)

1. Merge `AGENTS.md` do projeto com bootstrap do framework
2. Skills em `.codex/skills/` — symlink ou cópia de `skills/`

---

## Fluxo hierárquico

```
Pedido → AGENTS.md → Orchestrator
    → Classificar → Modo (Fast/Standard/Review/Council)
    → Working Context → Skills sob demanda
    → Validator/Critic (conforme modo)
    → final-response.md → descartar Working Context
```

---

## Verificação

| Pedido | Modo esperado |
|--------|---------------|
| "Como funciona X?" | Fast |
| "Corrija typo em Y" | Standard |
| "Adicione migration Z" | Review |
| "Integre pagamento" | Technical Council |

---

## Manutenção

- Nova skill: `skills/skill-builder/SKILL.md`
- Versão: `VERSION` + `CHANGELOG.md` + `docs/VERSIONING.md`
