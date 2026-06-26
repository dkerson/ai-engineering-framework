# Growth & Brand Intelligence

> Dominio responsavel por branding, copy, marketing, SEO e assets visuais em produtos criados com o AI Engineering Framework.

## Objetivo

Garantir que landing pages, sites, portais, sistemas web, apps mobile e dashboards tenham comunicacao clara, identidade consistente e aparencia profissional.

## Quando usar

- Landing page, site, home publica, portal ou pagina institucional
- Marketing, campanha, copy, SEO, prova social ou conversao
- Onboarding, empty states, mensagens internas e microcopy
- Logo, favicon, app icon, social preview, imagens, ilustracoes ou icones
- Auditoria de comunicacao, marca, assets ou conversao

## Principios

| Principio | Regra |
|-----------|-------|
| Identidade existente primeiro | Respeitar Design DNA, brand kit e assets ja presentes no projeto |
| Conversao com contexto | Copy e CTAs devem refletir produto, publico e oferta real |
| Assets com criterio | Analisar necessidade antes de buscar ou gerar imagens |
| Sistemas sao produtivos | Em ERP, CRM, BI e dashboards, usar visuals apenas quando agregarem clareza |
| Licencas abertas | Priorizar fontes publicas, gratuitas e com licenca adequada |

## Skills

| Skill | Papel |
|-------|-------|
| `project-style-analyzer` | Detecta Design System, UI library, tema, identidade e modo visual |
| `knowledge-engine` | Consulta o Knowledge Hub relevante antes do plano |
| `brand-strategist` | Tom de voz, posicionamento e personalidade |
| `brand-identity-manager` | Identidade visual, logo, cores e tipografia |
| `brand-voice-manager` | Voz e linguagem da marca |
| `brand-consistency-manager` | Consistencia entre Brand/Communication/Marketing/Visual/Product DNA |
| `content-strategist` | Arquitetura de conteudo e narrativa |
| `copywriter` | Headlines, beneficios, CTAs, FAQ e secoes persuasivas |
| `headline-specialist` | Refinamento de headlines e subheadlines |
| `cta-specialist` | Chamadas para acao e microcopy de conversao |
| `faq-specialist` | Objecoes e perguntas frequentes |
| `storytelling-specialist` | Narrativa de produto e marca |
| `ux-writer` | Microcopy, mensagens, tooltips, empty/error/success states |
| `microcopy-specialist` | Textos curtos de interface |
| `landing-page-specialist` | Estrutura de landing page orientada a conversao |
| `seo-specialist` | Metadados, headings, semantica e busca organica |
| `growth-strategist` | Hipoteses de crescimento e priorizacao |
| `trust-builder` | Credibilidade, seguranca, autoridade e confianca |
| `asset-intelligence` | Decide tipo de asset e fontes adequadas |
| `asset-curator` | Curadoria consolidada de assets |
| `open-source-asset-finder` | Recomenda fontes abertas; nunca baixa automaticamente |
| `image-curator` | Seleciona imagens publicas/licenciadas quando necessario |
| `illustration-curator` | Seleciona ilustracoes e estilos compativeis |
| `icon-curator` | Padroniza bibliotecas e uso de icones |
| `logo-manager` | Logo, favicon, PWA/app icons e previews sociais |
| `image-optimizer` | Formato, peso, lazy loading, responsividade e SEO |
| `brand-reviewer` | Consistencia visual e textual |
| `visual-consistency-reviewer` | Consistencia visual entre telas e assets |
| `marketing-reviewer` | Persuasao, credibilidade, autoridade e clareza |
| `conversion-optimizer` | CTA, fluxo, prova social e reducao de friccao |
| `social-proof-specialist` | Clientes, cases, depoimentos, numeros e selos |
| `product-excellence` | Padrao minimo de produto completo |
| `product-evolution-planner` | Roadmap apos auditoria |

## Pipeline automatico

Para pedidos como landing page, site, pagina institucional, tela publica, portal, home publica, marketing ou onboarding, o Orchestrator monta o menor fluxo seguro:

```text
project-style-analyzer -> knowledge-engine -> brand-strategist
-> content-strategist -> copywriter -> ux-writer
-> product/ux/ui/design-system conforme disponivel
-> asset-intelligence -> landing-page-specialist -> seo-specialist
-> frontend/mobile conforme stack
-> visual-consistency-reviewer -> brand-reviewer -> marketing-reviewer
-> conversion-optimizer -> product-excellence -> qa
```

O pipeline pode ser reduzido quando a tarefa for pontual, por exemplo apenas copy, SEO ou assets.

## Politica de assets

1. Verificar assets reutilizaveis do projeto.
2. Verificar biblioteca interna ou design system.
3. Usar SVG quando fizer sentido.
4. Preferir icones antes de imagens quando resolvem o problema.
5. Usar ilustracoes quando comunicarem melhor que fotos.
6. Buscar imagens publicas somente quando necessario.

Fontes sugeridas: Unsplash, Pexels, Pixabay, Storyset, unDraw, Open Doodles, ManyPixels, Lucide, Heroicons, Phosphor, Tabler Icons, Material Symbols, Simple Icons e Google Fonts.

## Product Audit

Auditorias de produto devem incluir notas de 0 a 10 para:

- Copy
- Brand
- Marketing
- Conversao
- Landing Page
- SEO
- Assets
- Comunicacao
- Identidade Visual
- Tom de Voz
- Design System
- Product Market Fit
- Escalabilidade

Use `checklists/marketing/product-audit.md` para consolidar avaliacao e recomendacoes.

Categorias abaixo de 8 devem gerar melhorias automaticas e acionar `product-evolution-planner` quando o pedido for auditoria ou evolucao de produto.
