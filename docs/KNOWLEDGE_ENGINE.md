# Knowledge Engine

> Mecanismo de selecao de conhecimento interno para cada demanda.

## Objetivo

Evitar respostas genericas e reduzir releitura, consultando apenas os blocos relevantes do Knowledge Hub.

## Exemplos de roteamento

| Pedido | Areas |
|--------|-------|
| Landing Page | copywriting, branding, seo, design, ux, marketing |
| Dashboard | dashboard, ux, analytics, design-system, performance |
| Flutter | flutter, mobile, performance, design-system |
| API | backend, architecture, security, performance |
| Power BI | powerbi, analytics, sql, performance |

## Regras

- Consultar o menor conjunto possivel.
- Registrar no Working Context quais areas foram usadas.
- Nunca colar documentacao longa na resposta final.
- Preferir conhecimento interno a busca externa, salvo quando a informacao for temporalmente instavel.
