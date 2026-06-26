# Capability Architecture

> v2.9.0 — evoluído para **Capability Operating System (COS)** em v2.10.0.

Ver **`docs/CAPABILITY_OPERATING_SYSTEM.md`** para governança completa.

## Conceito

**Capability** = pacote reutilizável de skills, rules, templates, workflows e knowledge para uma tecnologia (RAG, OCR, Voice, etc.).

## Regra de ouro

> Nenhuma tecnologia nova é implementada diretamente em Umbra, Irisys, SmartRifa ou outro projeto. Primeiro vira Capability do framework.

## Hierarquia

```text
FOS → Capability Registry → Capability Resolver → Sub-orchestrador (ex. rag-orchestrator) → Skills
```

## Capability vs Plugin

| | Capability | Plugin |
|---|------------|--------|
| Escopo | Tecnologia/padrão (RAG, OCR) | Integração externa (GitHub, SQL Server) |
| Exemplo | RAG Intelligence | github-plugin |
| Uso conjunto | RAG + postgres-plugin para pgvector | — |

## Referências

- `capabilities/README.md`
- `capabilities/CAPABILITY_REGISTRY.md`
- `docs/RAG_INTELLIGENCE.md`
