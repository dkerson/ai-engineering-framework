# Framework Recommendations

> Gerado: 2026-06-29 - v2.17.0

## MCP Portability v2.17.0

1. Usar `rules/mcp-portability.md` em qualquer configuracao MCP.
2. Preferir ClickUp remoto `https://mcp.clickup.com/mcp` com OAuth no cliente.
3. Preferir GitHub remoto `https://api.githubcopilot.com/mcp/` com OAuth no cliente.
4. Usar `npx -y @mcp-collection/mssql-mcp` para MSSQL local, sem path de usuario.
5. Separar credenciais por conexao (`MSSQL_*`, `MSSQL_FISCAL_*`).

## No Hardcode Governance v2.16.0

1. Usar `rules/no-hardcode.md` em features/reviews que criem modulos, menus, permissoes, status, URLs, thresholds, seeds ou regras variaveis.
2. Usar `hardcode-scanner` para scans dirigidos em projetos consumidores.
3. Em modulos/menus/roles/permissoes/status, escanear seed/bootstrap/policies antes de docs, migrations e bibliotecas geradas.
4. Quando houver evidencia do usuario (screenshot, arquivo ou linha), iniciar por esse padrao e por arquivos equivalentes.
5. Classificar achados como real ou falso positivo antes de corrigir.
6. Preferir banco/parametro/config/env/registry/feature flag para valores variaveis.
7. Seeds de produto devem ser idempotentes e preservar customizacoes.

## Execution Reliability v2.15.0

1. Usar `rules/execution-loop-control.md` em bugs e validacoes com retry; apos 2 falhas com a mesma hipotese, replanejar.
2. Usar `rules/frontend-runtime-validation.md` em telas/rotas/HTML antes de aceitar evidencia visual.
3. Usar `rules/regression-boundary.md` quando uma correcao tocar layout, router, provider, CSS global, componente base, hook ou cliente API.
4. Validar rotas/testes canario quando arquivo compartilhado for alterado.

## Security Intelligence v2.14.0

1. Usar `authorization-specialist` para RBAC/ABAC, roles, scopes, tenants e matriz de permissoes.
2. Usar `permission-cache-reviewer` sempre que permissao for cacheada em memoria, sessao, claims, edge ou Redis.
3. Usar `threat-modeler` antes de mudancas sensiveis em auth, multi-tenant, dados sensiveis ou producao.
4. Manter `security-review` como revisor geral, nao como substituto de arquitetura segura.

## Context Hygiene v2.13.0

1. Avaliar Context Health em missoes longas, mudancas de plano e antes de validacoes amplas.
2. Usar Compacted Snapshot quando contexto poluido misturar decisoes, hipoteses antigas e outputs brutos.
3. Registrar em Token Metrics apenas quando a compactacao evitar desperdicio real.

## Execution Intelligence v2.12.1

1. Usar Fast Path antes do NLME completo para pedidos simples e baixo risco.
2. Registrar apenas metadados curtos em Mission Ledger, Skill Usage e Token Metrics.
3. Nunca permitir auto-mutacao do framework; evolucao automatica deve parar em recomendacao.
4. Rodar auditoria de fronteiras de skills apenas depois de dados reais de uso.
5. Automatizar inventario/metricas somente se o ledger manual mostrar valor recorrente.

## MCP Readiness v2.11

1. Validar **user-mssql** localmente -> sqlserver active (read-only prod).
2. **postgres + pgvector** para RAG quando Postgres disponivel.
3. docker/github: manter under-review ate aprovacao.

## Capability Architecture

1. **Adotar capability-first** em toda missao de tecnologia nova (OCR, voice, agents).
2. **RAG Stable** apos primeiro projeto consumidor validar guardrails em producao.
3. **OCR Capability** - proximo candidato Planned -> In Development (depende de RAG ingestao).

## COS v2.10

1. **Capability-first** e politica, nao convencao.
2. **PROJECT_CAPABILITIES** substitui listagem de skills por projeto.
3. **OCR** proxima capability Planned -> Approved.

## RAG Intelligence

1. Definir vector DB plugin (postgres pgvector ou dedicado) quando projeto consumir RAG.
2. Benchmark com rag-evaluator antes de go-live.
3. Confidence threshold por projeto via template configuravel.

## Geral

1. Manter distincao knowledge-engine (Hub) vs knowledge-architect (KB RAG).
2. Nao implementar RAG em Umbra/Irisys/SmartRifa ate missao explicita de produto aprovada.
