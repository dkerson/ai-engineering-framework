# Versionamento — AI Engineering Framework

## Repositório independente

| Item | Valor |
|------|-------|
| Nome do repositório | `ai-engineering-framework` |
| Versão atual | Ver arquivo `VERSION` na raiz |
| Changelog | `CHANGELOG.md` |

## Semantic Versioning

| Incremento | Quando |
|------------|--------|
| **MAJOR** | Breaking change em AGENTS.md, paths, orchestrator ou skills de governança |
| **MINOR** | Nova skill, workflow, modo ou feature compatível |
| **PATCH** | Correções de texto, exemplos, typos em skills |

## Tags Git

```bash
# No repositório do framework
git tag -a v2.0.0 -m "AI Engineering Framework 2.0 — orquestração hierárquica"
git push origin v2.0.0
```

Consumidores fixam versão no submodule:

```bash
cd .ai && git checkout v2.0.0
```

## Atualizar só o framework

O projeto consumidor commita apenas o hash do submodule — seu código não muda.

```bash
cd .ai
git pull origin main          # ou checkout de tag específica
cd ..
git add .ai
git commit -m "chore: bump ai-engineering-framework"
```

## Política de compatibilidade

- Paths `skills/`, `rules/`, `workflows/` estáveis entre minors
- `Personal-AI/` permanece alias documentado — não remover sem major
- Novas skills não quebram consumidores existentes
- Remoção de skill → apenas em major + entrada no CHANGELOG

## Roadmap sugerido (próximas versões)

| Versão | Foco |
|--------|------|
| 2.1.0 | Templates de contexto por stack (NestJS, Flutter) |
| 2.2.0 | Skill `nestjs` dedicada; checklist unificado validator/qa |
| 3.0.0 | Renomear pasta default para `.ai/` em exemplos (com migração doc) |
