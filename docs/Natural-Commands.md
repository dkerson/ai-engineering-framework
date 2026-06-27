# Natural Commands

> Catálogo de verbos e frases naturais → tipo de missão NLME.

## Verbos imperativos

| Comando natural | Mission Type | Workflow |
|-----------------|--------------|----------|
| Analise / Audite | Audit Mission | `product-excellence.md` |
| Revise / Review | Review Mission | `review.md` |
| Transforme | Product Evolution Mission | `product-excellence.md` |
| Modernize | Modernization Mission | `product-excellence.md` |
| Melhore / Evolua | Continuous Improvement Mission | `product-excellence.md` |
| Otimize | Performance Mission | `performance.md` |
| Lance / Publique | Launch Mission | `marketing.md` |
| Venda mais / Cresça | Growth Mission | `marketing.md` |
| Prepare | Preparation Mission → Infra/Capability/Launch | contexto |
| Conecte / Integre | Infrastructure Mission | `infrastructure-mission.md` |
| Implemente / Crie / Desenvolva | Development Mission | `feature.md` |
| Configure | Infrastructure Mission | `infrastructure-mission.md` |
| Projete / Arquitete | Architecture Mission | `architecture.md` |
| Escale / Escalone | Scalability Mission | `architecture.md` |
| Corrija / Conserte | Bug Mission | `bug.md` |
| Documente | Knowledge Mission | `documentation.md` |
| Automatize | Automation Mission | `devops.md` |

## Frases implícitas (sem verbo claro)

| Frase | Comando inferido | Mission |
|-------|------------------|---------|
| "Está feio" | Melhore | UX/UI Mission |
| "Está lento" | Otimize | Performance Mission |
| "Está ruim" (dashboard) | Analise | Dashboard Mission |
| "Parece amador" | Transforme | Brand + Modernization |
| "Quero impressionar" | Analise + Transforme | Product Evolution |
| "Prepare um Chat IA" | Prepare | Capability + RAG Mission |

## Modificadores de urgência

| Modificador | Efeito |
|-------------|--------|
| "urgente", "produção", "caiu" | urgency: critical → Council/incident |
| "rápido", "só um olhar" | modo Fast ou Analysis only |
| "completo", "profundo" | Review + Product Excellence full |

## Projeto implícito

| Menção | Projeto |
|--------|---------|
| Umbra, portal, KB interno | umbra |
| Irisys, TMS, logística | irisys |
| SmartRifa, RifSmart | rifsmart |
| Framework, skills, FOS | framework |

## Uso

Mission Translator consulta este catálogo **antes** de Mission Recognition. Múltiplos verbos → missão composta ou prioridade pelo Goal Recognition.

## Referências

- `docs/Mission-Catalog.md`
- `skills/mission-translator/SKILL.md`
