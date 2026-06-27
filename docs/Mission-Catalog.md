# Mission Catalog

> Catálogo oficial de tipos de missão NLME — extensão de `docs/Missions.md`.

## Missões de desenvolvimento

| Mission Type | Trigger natural | Workflow principal | Modo operacional |
|--------------|-----------------|-------------------|------------------|
| Development Mission | "Implemente", "Crie", "Desenvolva" | `feature.md` | Standard/Review |
| Bug Mission | "Corrija", "Erro", "Quebrou" | `bug.md` | Standard |
| Review Mission | "Revise", "Review" | `review.md` | Fast/Standard |

## Missões de produto e design

| Mission Type | Trigger natural | Workflow principal |
|--------------|-----------------|-------------------|
| Product Evolution Mission | "Transforme", "Referência" | `product-excellence.md` |
| Modernization Mission | "Modernize", "Antigo" | `product-excellence.md` + `refactor.md` |
| UX Mission | "Experiência", "Confuso", "Fricção" | `ux.md` / `product-design.md` |
| UI Mission | "Feio", "Visual", "Layout" | `product-design.md` |
| Dashboard Mission | "Dashboard ruim", "Relatório" | `data.md` + `product-excellence.md` |
| Continuous Improvement Mission | "Melhore", "Evolua" | `product-excellence.md` |

## Missões de growth e lançamento

| Mission Type | Trigger natural | Workflow principal |
|--------------|-----------------|-------------------|
| Growth Mission | "Venda mais", "Converter" | `marketing.md` |
| Launch Mission | "Lance", "Go-live" | `marketing.md` + `devops.md` |
| Brand Mission | "Premium", "SaaS", "Marca" | `marketing.md` |

## Missões técnicas

| Mission Type | Trigger natural | Workflow principal |
|--------------|-----------------|-------------------|
| Architecture Mission | "Projete", "Arquitetura" | `architecture.md` |
| Performance Mission | "Otimize", "Lento" | `performance.md` |
| Security Mission | "Segurança", "Vulnerável" | `security.md` |
| Scalability Mission | "Escale", "Escale" | `architecture.md` + `devops.md` |
| Data Mission | "SQL", "BI", "Indicadores" | `data.md` |
| Infrastructure Mission | "Conecte", "Configure", "Prepare" | `infrastructure-mission.md` |

## Missões de framework e conhecimento

| Mission Type | Trigger natural | Workflow principal |
|--------------|-----------------|-------------------|
| Framework Mission | Saúde do framework, FOS | `framework-operating-system.md` |
| Capability Mission | "Chat IA", "RAG", "Assistente" | `capability-mission.md` |
| Knowledge Mission | "Biblioteca", "KB", "Documentação" | `documentation.md` + `product-excellence.md` |
| RAG Mission | "Busca semântica", "FAQ IA" | `capability-mission.md` |
| MCP Mission | "MCP", "Conectores" | `mcp-mission.md` |
| Plugin Mission | "Plugin", "Integração" | `plugin-mission.md` |
| Automation Mission | "Automatize", "Pipeline" | `devops.md` |
| Innovation Mission | "Diferencial", "Inove" | `strategic-mission.md` |
| Audit Mission | "Analise", "Auditoria" | `product-excellence.md` |

## Mapeamento composto (exemplos vNext)

| Frase | Missão | Pipeline automático |
|-------|--------|---------------------|
| "Transforme o Umbra em referência" | Product Evolution | Audit → UX → UI → Benchmark → Roadmap → Impl |
| "Modernize o Irisys" | Modernization | Architecture → Design → Performance → Roadmap |
| "Quero vender mais" | Growth | Copy → Landing → Conversão → Marketing → Benchmark |
| "Esse dashboard está ruim" | Dashboard | Dashboard Review → Data → UX → Performance → Impl |
| "Analise o KB" | Audit + Knowledge | Product Excellence → Knowledge Hub → UX → Roadmap |

## Referências

- `docs/Missions.md` (legado — preservado)
- `docs/Mission-Recognition.md`
- `workflows/_index.md`
