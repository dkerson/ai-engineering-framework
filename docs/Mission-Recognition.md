# Mission Recognition

> Regras para converter frases humanas em Mission Types. **NLME v2.12+** — primeira etapa após Natural Commands.

## Pipeline NLME

```text
Natural Commands → Mission Recognition → Goal Recognition → Mission Catalog
```

Ver: `docs/Natural-Language-Missions.md` · `skills/mission-translator/SKILL.md`

## Reconhecimento automatico

| Frase do usuario | Mission reconhecida | Dominios provaveis |
|------------------|--------------------|--------------------|
| "Transforme esse produto em referencia" | Product Evolution Mission | Product, UX, UI, Growth, Brand, QA |
| "Quero vender mais" | Growth Mission | Marketing, Copy, Landing Page, Conversao, Product Review |
| "Esse sistema esta lento" | Performance Mission | Development, Data, Architecture, QA |
| "Esse sistema parece antigo" | Modernization Mission | Product, UX, UI, Brand, Frontend |
| "Quero que fique bonito" | UX/UI Mission | UX, UI, Design Review, Assets |
| "Esse dashboard esta ruim" | Dashboard Mission | Data, Analytics, UX, Dashboard, QA |
| "Quero diminuir suporte" | Product Improvement Mission | UX, Onboarding, Help, Microcopy |
| "Quero preparar para escalar" | Scalability Mission | Architecture, Backend, Data, DevOps |
| "Quero lancar esse SaaS" | Launch Mission | Product, Growth, Brand, QA, DevOps |
| "Analise o KB" | Audit + Knowledge Mission | Product Excellence, Knowledge Hub, UX, Development |
| "Prepare um Chat IA" | Capability + RAG Mission | Capability, RAG, Infrastructure |
| "Otimize os relatórios" | Performance + Data Mission | Data Intelligence, Performance, Dashboard |
| "Faça parecer SaaS Premium" | Brand + Product Evolution Mission | Brand, UI, UX, Product Excellence |

## O que identificar

- Objetivo principal
- Objetivos secundarios
- Contexto
- Urgencia
- Impacto
- Complexidade
- Risco
- Dominios envolvidos
- Tipo de mission

## Decisoes autonomas

Quando o usuario pede um objetivo alto nivel, o SIL pode incluir automaticamente:

- Product Audit
- Competitive Benchmark
- Design Review
- Brand Review
- Copy Review
- Dashboard Review
- UX Review
- Roadmap
- Quick Wins
- Implementacao

O usuario nao precisa pedir esses itens explicitamente.
