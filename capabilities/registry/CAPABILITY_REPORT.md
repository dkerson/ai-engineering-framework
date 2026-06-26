# Capability Report

> Responde perguntas naturais via COS · v2.10.0

## Quais Capabilities temos?

**18 registradas:** 14 Stable (domínios + COS) · 1 Ready (RAG) · 3 Planned · 3 Idea.

Ver `CAPABILITY_STATUS.md` para lista completa.

## Quais estão prontas?

- **Ready for projects:** RAG Intelligence v1.0.0
- **Stable (em uso via Orchestrator):** Development, Data, Product & Design, Growth & Brand, Infrastructure, Plugin, FOS, SIL, Knowledge Hub, Mission, Product Excellence/Evolution, Continuous Improvement, COS

## Quais ainda faltam?

| Prioridade | Capability | Status |
|------------|------------|--------|
| P1 | OCR Intelligence | Planned |
| P1 | Evaluation Intelligence | Planned |
| P2 | Memory Intelligence | Planned |
| P3 | Vision, Voice, Agents | Idea |

Ver `roadmap/CAPABILITY_ROADMAP.md`.

## Quais estão em desenvolvimento?

Nenhuma em **In Development** no momento. RAG concluiu fase Ready.

## Quais projetos utilizam cada Capability?

| Projeto | Capabilities (declaradas) |
|---------|---------------------------|
| umbra | development, data, infrastructure, product-design, plugin (via PROJECT_CAPABILITIES) |
| irisys | development, data, growth-brand (planejado RAG) |
| rifsmart | development (mínimo) |

**Nenhum projeto consome RAG ainda** — framework-only.

Ver `infrastructure/projects/*/PROJECT_CAPABILITIES.md`.

## Quais possuem maior impacto?

1. RAG Intelligence — assistentes, help centers, documentação
2. OCR Intelligence — desbloqueia PDFs escaneados para RAG
3. Data Intelligence — já Stable; base para BI e RAG híbrido

## O Framework suporta RAG?

**Sim.** Capability Ready v1.0.0. Consumo em projeto requer Capability Mission aprovada — não implementação ad hoc.

## O Framework suporta OCR?

**Planejado.** Status Planned; depende de RAG para ingestão.

## Próxima Capability recomendada

**OCR Intelligence** — impacto alto, esforço médio, dependência RAG satisfeita (Ready).

## Referências

- `skills/capability-manager/SKILL.md`
- `examples/capability-operating-system.md`
