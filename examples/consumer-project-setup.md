# Exemplo: Instalar framework em novo projeto (RIFSMART)

> Referência para consumidores além do Umbra.

## Cenário

Novo monorepo NestJS + React sem framework de agentes.

## Passos

```bash
cd rifsmart
git submodule add https://github.com/dkerson/ai-engineering-framework.git .ai
cp .ai/context/_template/*.md .ai/context/
```

## AGENTS.md do RIFSMART

```markdown
## AI Engineering Framework
Bootstrap: [.ai/AGENTS.md](.ai/AGENTS.md) → `.ai/skills/orchestrator/SKILL.md`
```

## context/tech-stack.md (trecho)

```markdown
| Framework | NestJS 10 |
| Frontend | React 19 |
| Banco | PostgreSQL + Prisma |
```

## Teste

Pedido: `"Como está organizado o módulo de pedidos?"`

- Modo esperado: **Fast** ou **Standard** (se precisar Context Builder)
- Orchestrator único contato
- Sem skills desnecessárias

## Atualizar framework sem tocar no RIFSMART

```bash
cd .ai && git checkout v2.1.0 && cd ..
git add .ai && git commit -m "chore: framework v2.1.0"
```

Código do RIFSMART permanece intacto.
