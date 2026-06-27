# Exemplos — Natural Language Missions

> Após NLME v2.12 — o usuário escreve apenas o objetivo.

## Product Evolution

**Entrada:** "Transforme o Umbra em um produto de referência."

**NLME:**
- Mission: Product Evolution
- Domínios: Product, UX, UI, Growth, Brand, QA
- Pipeline: product-excellence → benchmark → evolution planner
- Modo: Review

## Modernization

**Entrada:** "Modernize o Irisys."

**NLME:**
- Mission: Modernization
- Pipeline: architecture review → design review → performance → roadmap
- Modo: Review/Council se >3 módulos

## Growth

**Entrada:** "Quero vender mais."

**NLME:**
- Mission: Growth
- Pipeline: copy → landing → conversão → marketing → benchmark
- Modo: Standard/Review

## Dashboard

**Entrada:** "Esse dashboard está ruim."

**NLME:**
- Mission: Dashboard
- Goal real: melhor analytics UX + performance + clareza KPI
- Pipeline: data → dashboard designer → ux → performance
- Modo: Review

## Knowledge / KB

**Entrada:** "Analise o KB."

**NLME:**
- Mission: Audit + Knowledge
- Projeto: umbra
- Pipeline: product-excellence → knowledge hub → ux
- Confidence: ~85 → executar autonomamente

## Capability / RAG

**Entrada:** "Prepare um Chat IA."

**NLME:**
- Mission: Capability + RAG
- Pipeline: capability-mission → rag-orchestrator → infrastructure
- Plugins: conforme PROJECT_MCP

## Vago → inferido

**Entrada:** "Está feio."

**NLME:**
- Goal real: UX/UI/Design premium
- Mission: UX/UI ou Continuous Improvement
- Pergunta: só se projeto desconhecido

## Referências

- `docs/Natural-Commands.md`
- `docs/Mission-Catalog.md`
- `workflows/natural-language-mission.md`
