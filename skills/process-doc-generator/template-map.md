# Mapa — Process Doc Generator

> Mapeamento seções ↔ placeholders do template `docs/templates/process-doc.html`

## Metadados hero

| Campo | Placeholder |
|-------|-------------|
| Título | `{{TITULO}}` |
| Intro | `{{INTRO}}` |
| Versão | `{{META_VERSAO}}` |
| Data | `{{META_DATA}}` |
| Sistema | `{{META_SISTEMA}}` |
| Público | `{{META_PUBLICO}}` |

## Seções

| # | id HTML | Conteúdo |
|---|---------|----------|
| 1 | `#introducao` | Contexto e objetivo do documento |
| 2 | `#acesso` | Permissões, rotas, pré-requisitos |
| 3 | `#visao-geral` | Fluxo resumido, atores |
| 4 | `#passo-a-passo` | Núcleo — `.step-block` numerados |
| 5 | `#decisoes` | Ramificações if/else |
| 6 | `#papeis` | Responsabilidades |
| 7 | `#dicas` | Boas práticas |
| 8 | `#faq` | Troubleshooting |
| 9 | `#glossario` | Termos |
| 10 | `#versionamento` | Histórico |

## Diferença vs EF

| | EF | Processo |
|--|-----|----------|
| Pasta | `docs/specs/` | `docs/processes/` |
| Prefixo | `EF_*` | `PROC_*` |
| Foco | Kickoff, requisitos | Passo a passo operacional |

Referência: `docs/pmo/relatorio-sprint-clickup-guia-usuario.*`
