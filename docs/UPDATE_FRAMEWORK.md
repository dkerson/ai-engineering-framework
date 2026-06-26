# Atualizar o Framework

> Projetos consumidores (ex.: Umbra) com submodule `Personal-AI/`.

## Atualização rápida

```bash
cd Personal-AI
git fetch origin
git checkout v2.1.0   # ou tag desejada
cd ..
git add Personal-AI
```

Ou:

```bash
git submodule update --remote Personal-AI
```

## Verificar versão

```bash
cat Personal-AI/VERSION
```

## v2.1.0 — Data Intelligence + Fluxos Híbridos

### Novidades

- Domínio **Data Intelligence** com `data-orchestrator`
- 22 skills novas (dados, task/requirement, hybrid)
- `context/semantic-layer/` — templates Otus/Irisys
- `templates/data/`, `checklists/data/`, `rules/data/`, `examples/data/`
- Fluxos híbridos: `docs/HYBRID_FLOWS.md`
- Working Context expandido para dados

### Compatibilidade

- Skill `data` **preservada** (roteamento para especializadas)
- Todas as 39+ skills anteriores **intactas**
- Bootstrap inalterado: `AGENTS.md` → `orchestrator/SKILL.md`

### Após atualizar no Umbra

1. Revisar `CHANGELOG.md`
2. Preencher `Personal-AI/context/semantic-layer/` ou overlay no projeto
3. Opcional: linkar `docs/DATA_INTELLIGENCE.md` no `AGENTS.md` do monorepo

## Versionamento

Semver — ver `docs/VERSIONING.md`.

| Mudança | Versão |
|---------|--------|
| Skills/workflows novos (compatíveis) | MINOR (2.1.0) |
| Quebra de bootstrap ou remoção de skill | MAJOR |

## Contribuir de volta

Repositório: [dkerson/ai-engineering-framework](https://github.com/dkerson/ai-engineering-framework)
