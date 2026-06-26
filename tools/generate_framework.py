#!/usr/bin/env python3
"""Gerador do Personal AI Framework — skills, workflows, rules, templates, checklists."""
from pathlib import Path

ROOT = Path(__file__).parent.parent

SKILL_TEMPLATE = '''---
name: {name}
description: >-
  {description}
---

# {title}

## Objetivo

{objective}

## Quando usar

{when_use}

## Quando NÃO usar

{when_not}

## Responsabilidades

{responsibilities}

## Entradas esperadas

{inputs}

## Saídas esperadas

{outputs}

## Checklist

{checklist}

## Integração com outras skills

{integration}

## Exemplos

{examples}

## Referências

{references}
'''

SKILLS = [
    ("context-builder", "Context Builder", "Monta contexto mínimo do projeto lendo AGENTS.md, context/ e estrutura de pastas. Usar quando o projeto é desconhecido ou o escopo precisa de mapeamento inicial.", "Fornecer contexto suficiente para execução sem leitura excessiva de arquivos.", "- Projeto novo ou desconhecido\n- Início de bug/feature sem contexto claro\n- Orchestrator solicita contexto", "- Contexto já carregado na sessão\n- Tarefa pontual em arquivo único conhecido", "1. Ler AGENTS.md do projeto\n2. Ler `context/` do projeto ou Personal-AI\n3. Mapear estrutura (pastas principais, stack)\n4. Identificar área afetada pelo pedido\n5. Resumir em bullets (máx. 10)", "- Pedido do usuário\n- AGENTS.md do repo\n- `Personal-AI/context/*`", "- Resumo de contexto (stack, arquitetura, área)\n- Lista de arquivos candidatos a investigação", "- [ ] AGENTS.md lido\n- [ ] Stack identificada\n- [ ] Área afetada mapeada\n- [ ] Resumo conciso produzido", "- **Upstream:** orchestrator\n- **Downstream:** bug-hunter, tech-lead, software-architect", "**Input:** Bug em API desconhecida\n**Output:** \"Monorepo .NET 8 + Angular 19. Erro em Umbra.Api/Controllers/OrdersController.\"", "- `rules/token-economy.md`\n- `context/architecture.md`"),
    ("product-owner", "Product Owner", "Define valor, escopo, prioridade e critérios de aceite para features e melhorias. Usar em novas funcionalidades, refinamento de requisitos ou decisões de escopo.", "Traduzir necessidade de negócio em requisitos acionáveis.", "- Nova feature ou melhoria\n- Escopo ambíguo\n- Priorização necessária", "- Bug fix técnico puro\n- Refatoração interna sem impacto de produto", "1. Clarificar problema e valor\n2. Definir escopo in/out\n3. Escrever critérios de aceite (Given/When/Then)\n4. Identificar riscos de produto\n5. Priorizar MVP vs nice-to-have", "- Pedido do usuário\n- Contexto de negócio (`context/business.md`)", "- User stories ou requisitos\n- Critérios de aceite\n- Escopo delimitado", "- [ ] Valor de negócio claro\n- [ ] Critérios de aceite testáveis\n- [ ] Escopo in/out definido\n- [ ] Riscos identificados", "- **Upstream:** orchestrator\n- **Downstream:** functional-spec, ux", "**Input:** \"Login com Google\"\n**Output:** CA1: Usuário clica \"Entrar com Google\" → redireciona OAuth → sessão criada.", "- `templates/feature-request.md`\n- `checklists/feature.md`"),
    ("functional-spec", "Functional Spec", "Produz especificação funcional detalhada. Usar após product-owner ou para documentar comportamento esperado.", "Descrever O QUE o sistema faz do ponto de vista do usuário/negócio.", "- Feature nova\n- Documentação funcional\n- Alinhamento antes de implementação", "- Spec técnica de implementação (usar technical-spec)\n- Bug fix pontual", "1. Descrever fluxos principais e alternativos\n2. Definir regras de negócio\n3. Listar entradas/saídas por tela/API\n4. Mapear casos de erro\n5. Usar `templates/functional-spec.md`", "- Requisitos do product-owner\n- Contexto de domínio", "- Documento de spec funcional\n- Diagramas de fluxo (se necessário)", "- [ ] Fluxos happy path + edge cases\n- [ ] Regras de negócio explícitas\n- [ ] Mensagens de erro definidas\n- [ ] Critérios de aceite linkados", "- **Upstream:** product-owner, context-builder\n- **Downstream:** ux, technical-spec, tech-lead", "**Input:** Feature de carrinho\n**Output:** Spec com fluxos adicionar/remover/checkout.", "- `templates/functional-spec.md`"),
    ("technical-spec", "Technical Spec", "Produz especificação técnica de implementação. Usar após functional-spec ou para decisões de design.", "Descrever COMO implementar: componentes, contratos, dados, integrações.", "- Feature complexa\n- Documentação técnica\n- Antes de implementação multi-camada", "- Spec funcional pura\n- Fix trivial one-liner", "1. Definir componentes e responsabilidades\n2. Especificar contratos (API, eventos)\n3. Modelar dados e migrations\n4. Listar dependências e riscos técnicos\n5. Usar `templates/technical-spec.md`", "- Functional spec\n- Decisões do software-architect", "- Technical spec document\n- Diagrama de componentes (opcional)", "- [ ] Componentes com SRP\n- [ ] Contratos definidos\n- [ ] Modelo de dados claro\n- [ ] Riscos técnicos listados", "- **Upstream:** functional-spec, software-architect\n- **Downstream:** tech-lead, backend, api, database", "**Input:** Login OAuth\n**Output:** Spec com endpoints, tokens, middleware, entidades.", "- `templates/technical-spec.md`\n- `rules/architecture.md`"),
    ("software-architect", "Software Architect", "Toma decisões arquiteturais, define padrões e ADRs. Usar em features complexas, refatorações estruturais ou dúvidas de design.", "Garantir soluções escaláveis, coerentes com arquitetura existente.", "- Decisão arquitetural\n- Feature multi-módulo\n- Refatoração estrutural\n- Integração complexa", "- Alteração localizada\n- Tarefa já coberta por padrão existente", "1. Analisar arquitetura atual (`context/architecture.md`)\n2. Propor opções com trade-offs\n3. Recomendar abordagem\n4. Gerar ADR se decisão significativa\n5. Validar SOLID e boundaries", "- Context builder output\n- Functional/technical requirements", "- Decisão arquitetural\n- ADR (`templates/adr.md`) se aplicável", "- [ ] Opções avaliadas\n- [ ] Trade-offs documentados\n- [ ] Coerência com arquitetura existente\n- [ ] ADR gerado se necessário", "- **Upstream:** functional-spec, context-builder\n- **Downstream:** technical-spec, tech-lead", "**Input:** Event-driven vs REST\n**Output:** ADR recomendando outbox pattern.", "- `templates/adr.md`\n- `rules/architecture.md`\n- `rules/solid.md`"),
    ("tech-lead", "Tech Lead", "Planeja implementação técnica: ordem de tarefas, arquivos afetados, estratégia de fix/feature.", "Transformar specs em plano de execução concreto e mínimo.", "- Após specs ou diagnóstico de bug\n- Antes de implementação\n- Divisão de trabalho", "- Implementação trivial de 1 arquivo\n- Tarefa puramente documental", "1. Listar arquivos a alterar (estimativa)\n2. Definir ordem de implementação\n3. Identificar riscos e dependências\n4. Estimar validações necessárias\n5. Aplicar token economy no plano", "- Spec ou diagnóstico do bug-hunter\n- Context builder output", "- Plano numerado de implementação\n- Lista de arquivos candidatos", "- [ ] Plano com passos claros\n- [ ] Escopo mínimo definido\n- [ ] Validações identificadas\n- [ ] Sem over-engineering", "- **Upstream:** bug-hunter, software-architect, functional-spec\n- **Downstream:** backend, api, react, flutter, database", "**Input:** Bug em save order\n**Output:** 1) Ler OrdersController 2) Verificar service 3) Fix validation 4) Test unitário.", "- `rules/token-economy.md`\n- `workflows/_process.md`"),
    ("backend", "Backend", "Implementa lógica server-side: services, controllers, domain, infra. Usar em tarefas backend .NET, Node, Python, etc.", "Implementar alterações server-side seguindo camadas e convenções do projeto.", "- Lógica de negócio server-side\n- Controllers, services, workers\n- Integrações backend", "- Frontend puro (usar react)\n- SQL puro sem camada (usar database)", "1. Ler convenções (`AGENTS.md`, `context/coding-standards.md`)\n2. Implementar menor diff possível\n3. Respeitar camadas (Api → App → Domain → Infra)\n4. Tratar erros e validações\n5. Não alterar appsettings/secrets sem preservar valores", "- Plano do tech-lead\n- Technical spec", "- Código implementado\n- Testes se aplicável", "- [ ] Camadas respeitadas\n- [ ] Validação de entrada\n- [ ] Erros tratados\n- [ ] Sem secrets expostos\n- [ ] Diff mínimo", "- **Upstream:** tech-lead, api, database\n- **Downstream:** qa, code-review", "**Input:** Endpoint criar pedido\n**Output:** Controller + Service + DTO + teste unitário.", "- `rules/clean-code.md`\n- `checklists/backend.md`"),
    ("api", "API", "Define e implementa contratos REST/GraphQL: endpoints, DTOs, validação, documentação OpenAPI.", "Garantir APIs consistentes, versionadas e bem documentadas.", "- Novo endpoint\n- Alteração de contrato\n- Integração externa via API", "- Lógica de negócio interna (backend)\n- UI components (react)", "1. Definir método, path, request/response\n2. Validar inputs (400) e auth (401/403)\n3. Documentar OpenAPI/Swagger\n4. Seguir convenções REST do projeto\n5. Usar `rules/api.md`", "- Technical spec\n- Functional spec", "- Endpoints implementados\n- Contrato documentado", "- [ ] Status codes corretos\n- [ ] Validação de input\n- [ ] Paginação/filtros se listagem\n- [ ] Swagger atualizado\n- [ ] Breaking changes identificados", "- **Upstream:** tech-lead, functional-spec\n- **Downstream:** backend, qa", "**Input:** GET /api/orders?page=1\n**Output:** Endpoint paginado com OrderListDto.", "- `rules/api.md`\n- `checklists/api.md`"),
    ("database", "Database", "Schema, migrations, queries, índices, performance SQL. Usar em alterações de banco de dados.", "Gerenciar persistência de forma segura e performática.", "- Migration nova\n- Query lenta\n- Modelagem de entidades\n- Índices", "- ORM config trivial sem schema change\n- Lógica de aplicação pura", "1. Analisar schema atual\n2. Criar migration reversível\n3. Otimizar queries (evitar N+1)\n4. Validar índices\n5. Usar `templates/migration.md`", "- Technical spec\n- Entity model", "- Migration scripts\n- Queries otimizadas", "- [ ] Migration up/down testada\n- [ ] Índices adequados\n- [ ] Sem data loss\n- [ ] Naming consistente\n- [ ] Rollback plan", "- **Upstream:** tech-lead, software-architect\n- **Downstream:** backend, qa", "**Input:** Campo status em orders\n**Output:** Migration AddStatusToOrders + índice.", "- `rules/database.md`\n- `checklists/database.md`\n- `templates/migration.md`"),
    ("react", "React", "Implementa frontend React/Next.js: components, hooks, state, routing.", "Desenvolver UI React seguindo padrões do projeto.", "- Componentes React/Next\n- Hooks, state management\n- Integração com API frontend", "- Flutter mobile (usar flutter)\n- Backend API", "1. Ler estrutura (`features/`, `core/`)\n2. Componentes pequenos e focados\n3. Tipagem TypeScript estrita\n4. Acessibilidade básica\n5. Mensagens UI em pt-BR se projeto BR", "- UX spec\n- API contracts", "- Componentes implementados\n- Testes se aplicável", "- [ ] Tipos corretos\n- [ ] Loading/error states\n- [ ] Responsivo se aplicável\n- [ ] Sem console.log\n- [ ] A11y básica", "- **Upstream:** ux, tech-lead, api\n- **Downstream:** qa, code-review", "**Input:** Tela login Google\n**Output:** LoginComponent + OAuth redirect handler.", "- `checklists/frontend.md`\n- `rules/clean-code.md`"),
    ("flutter", "Flutter", "Implementa apps mobile Flutter: widgets, state, navigation, platform channels.", "Desenvolver UI mobile Flutter com performance e UX nativa.", "- Telas Flutter\n- Widgets, BLoC/Riverpod\n- Integração mobile API", "- Web React (usar react)\n- Backend puro", "1. Seguir arquitetura do projeto (features/layers)\n2. Widgets composáveis\n3. State management consistente\n4. Testes widget quando crítico\n5. Platform-specific via channels se necessário", "- Mobile UX spec\n- API contracts", "- Telas/widgets implementados", "- [ ] State management correto\n- [ ] Performance (const, listView.builder)\n- [ ] Offline handling se aplicável\n- [ ] Testes widget críticos", "- **Upstream:** mobile-ux, tech-lead\n- **Downstream:** qa, code-review", "**Input:** Tela home dashboard\n**Output:** DashboardScreen + provider + API service.", "- `checklists/frontend.md`"),
    ("qa", "QA", "Estratégia de testes, casos de teste, validação manual/automática.", "Garantir qualidade via testes direcionados — não suíte completa desnecessária.", "- Após implementação\n- Validação de fix\n- Plano de testes para feature", "- Implementação de código (skills técnicas)\n- Review de código puro", "1. Derivar casos do functional spec / bug report\n2. Executar testes relacionados apenas\n3. Verificar edge cases críticos\n4. Documentar `templates/test-plan.md` se feature grande\n5. Reportar falhas ao tech-lead", "- Implementação concluída\n- Critérios de aceite", "- Resultado de testes\n- Casos adicionais se gaps", "- [ ] Happy path validado\n- [ ] Edge cases críticos\n- [ ] Regressão mínima ok\n- [ ] Testes relacionados executados", "- **Upstream:** backend, react, flutter, api\n- **Downstream:** code-review", "**Input:** Fix validação email\n**Output:** 3 casos: válido, inválido, vazio — todos passando.", "- `rules/testing.md`\n- `checklists/feature.md`\n- `templates/test-plan.md`"),
    ("playwright", "Playwright", "Testes E2E com Playwright: fluxos críticos, selectors, CI integration.", "Automatizar testes end-to-end de fluxos críticos.", "- E2E de fluxo crítico\n- Regressão UI automatizada\n- CI E2E pipeline", "- Testes unitários (qa)\n- Testes de API isolados", "1. Identificar fluxos críticos (login, checkout, etc.)\n2. Page Object Model\n3. Selectors estáveis (data-testid)\n4. Rodar apenas spec relacionado\n5. Integrar CI se projeto tiver", "- QA test plan\n- Fluxos funcionais", "- Specs Playwright\n- Resultado de execução", "- [ ] Fluxos críticos cobertos\n- [ ] Selectors estáveis\n- [ ] Sem flaky waits fixos\n- [ ] Screenshots on failure", "- **Upstream:** qa, ux\n- **Downstream:** devops (CI)", "**Input:** Fluxo login\n**Output:** login.spec.ts com OAuth mock.", "- `rules/testing.md`"),
    ("bug-hunter", "Bug Hunter", "Diagnóstico sistemático: reproduzir, isolar, encontrar causa raiz.", "Encontrar causa raiz com investigação mínima e dirigida.", "- Qualquer bug ou erro\n- Comportamento inesperado\n- Antes de implementar fix", "- Feature nova\n- Review de código", "1. Capturar erro/stack/logs\n2. Reproduzir passos mínimos\n3. Bisect: isolar camada (UI/API/DB)\n4. Localizar arquivo+linha\n5. Documentar causa raiz (`templates/root-cause-analysis.md` se complexo)", "- Mensagem de erro\n- Steps to reproduce\n- Logs", "- Causa raiz identificada\n- Arquivo(s) afetado(s)\n- Hipótese de fix", "- [ ] Reproduzido\n- [ ] Camada isolada\n- [ ] Arquivo/linha localizados\n- [ ] Causa raiz documentada\n- [ ] Leitura mínima de arquivos", "- **Upstream:** context-builder\n- **Downstream:** tech-lead, backend, etc.", "**Input:** Erro 500 ao salvar pedido\n**Output:** NullReference em OrderService.Save line 42 — CustomerId null.", "- `templates/bug-report.md`\n- `templates/root-cause-analysis.md`\n- `rules/token-economy.md`"),
    ("performance", "Performance", "Profiling, benchmarks, otimização de gargalos. Usar quando algo está lento ou consome recursos excessivos.", "Identificar e resolver gargalos com medição antes/depois.", "- Lentidão reportada\n- Timeout, high CPU/memory\n- Otimização solicitada", "- Feature nova sem problema perf\n- Premature optimization", "1. Medir baseline (tempo, queries, memória)\n2. Identificar top bottleneck (80/20)\n3. Aplicar fix mínimo\n4. Medir novamente\n5. Documentar ganho", "- Sintoma de lentidão\n- Logs/metrics se disponíveis", "- Métricas before/after\n- Fix aplicado ou recomendado", "- [ ] Baseline medido\n- [ ] Gargalo identificado\n- [ ] Fix mínimo aplicado\n- [ ] Melhoria quantificada\n- [ ] Sem otimização prematura", "- **Upstream:** orchestrator\n- **Downstream:** database, backend, devops", "**Input:** API lista 10s\n**Output:** N+1 em OrderItems — eager load reduziu para 200ms.", "- `checklists/performance.md`\n- `templates/root-cause-analysis.md`"),
    ("code-review", "Code Review", "Revisa código/PR por qualidade, lógica, testes e convenções.", "Garantir qualidade antes de merge — foco em issues reais.", "- PR review\n- Auto-revisão pós-implementação\n- Feedback de código", "- Implementação de features\n- Diagnóstico de bugs", "1. Ler diff apenas (não projeto inteiro)\n2. Verificar lógica, edge cases, security\n3. Checar testes adequados\n4. Classificar: Critical / Suggestion / Nice-to-have\n5. Usar `checklists/review.md`", "- Diff/PR\n- Contexto da mudança", "- Feedback estruturado\n- Aprovação ou lista de fixes", "- [ ] Lógica correta\n- [ ] Edge cases\n- [ ] Testes adequados\n- [ ] Convenções seguidas\n- [ ] Sem secrets/debug code", "- **Upstream:** qa, skills técnicas\n- **Downstream:** security-review (condicional)", "**Input:** PR com 3 files changed\n**Output:** 1 Critical (SQL injection), 2 Suggestions.", "- `rules/clean-code.md`\n- `rules/solid.md`\n- `checklists/review.md`"),
    ("release-notes", "Release Notes", "Produz notas de release para usuários/stakeholders.", "Comunicar mudanças de forma clara para release.", "- Bug fix em release\n- Feature pronta para deploy\n- Comunicação pós-deploy", "- Changelog técnico (usar changelog)\n- Durante desenvolvimento", "1. Listar mudanças user-facing\n2. Agrupar: Added/Fixed/Changed/Removed\n3. Linguagem não-técnica para usuários\n4. Usar `templates/release-notes.md`", "- Changelog\n- PRs merged", "- Release notes document", "- [ ] User-facing only\n- [ ] Agrupado por tipo\n- [ ] Sem jargão técnico excessivo\n- [ ] Breaking changes destacados", "- **Upstream:** qa, code-review\n- **Downstream:** deployment", "**Input:** Release v2.3\n**Output:** \"Added: Login Google. Fixed: erro ao salvar pedido.\"", "- `templates/release-notes.md`\n- `checklists/release.md`"),
    ("changelog", "ChangeLog", "Registro técnico de mudanças para desenvolvedores.", "Manter histórico técnico de alterações.", "- Feature concluída\n- Após merge significativo", "- Release notes user-facing (release-notes)", "1. Listar commits/PRs relevantes\n2. Formato Keep a Changelog\n3. Linkar issues/PRs\n4. Usar `templates/changelog.md`", "- PRs, commits\n- Implementação concluída", "- Entrada de changelog", "- [ ] Formato consistente\n- [ ] Breaking changes section\n- [ ] Links para PRs", "- **Upstream:** code-review\n- **Downstream:** release-notes", "**Input:** Feature OAuth\n**Output:** \"## [Unreleased] ### Added - Google OAuth login (#123)\"", "- `templates/changelog.md`"),
    ("ux", "UX", "Experiência de usuário web: fluxos, wireframes textuais, acessibilidade.", "Definir experiência usable e acessível antes/durante implementação.", "- Nova tela/fluxo web\n- Melhoria de usabilidade\n- Antes de implementação frontend", "- Mobile app (mobile-ux)\n- Backend puro", "1. Mapear user journey\n2. Definir estados: loading, empty, error\n3. Hierarquia visual e CTA\n4. A11y: contraste, keyboard, labels\n5. Wireframe textual", "- Functional spec\n- Product owner requirements", "- Fluxos UX\n- Requisitos de interface\n- Wireframes textuais", "- [ ] Happy path claro\n- [ ] Error/empty states\n- [ ] A11y considerada\n- [ ] Mobile-first se aplicável", "- **Upstream:** functional-spec\n- **Downstream:** react", "**Input:** Checkout flow\n**Output:** 3 steps, progress indicator, error em pagamento.", "- `checklists/frontend.md`"),
    ("mobile-ux", "Mobile UX", "Experiência mobile: gestos, navegação, platform guidelines.", "Definir UX mobile seguindo iOS/Android guidelines.", "- App mobile\n- Telas Flutter/RN\n- Gestos e navegação", "- Web desktop (ux)\n- Backend", "1. Seguir Material/Cupertino guidelines\n2. Thumb zone, bottom nav\n3. Offline states\n4. Push/deep links se aplicável\n5. Platform-specific patterns", "- Functional spec\n- Mobile requirements", "- Mobile UX spec\n- Navigation map", "- [ ] Platform guidelines\n- [ ] Gesture navigation\n- [ ] Offline handling\n- [ ] Safe areas", "- **Upstream:** functional-spec\n- **Downstream:** flutter", "**Input:** App banking\n**Output:** Tab nav + biometric login flow.", "- `checklists/frontend.md`"),
    ("prompt-engineer", "Prompt Engineer", "Otimiza prompts para LLMs: clareza, estrutura, few-shot, constraints.", "Criar prompts eficazes para agentes e automações.", "- Criar/otimizar prompt\n- Skill ou agent config\n- Automação LLM", "- Implementação de código\n- Bug fix", "1. Definir objetivo e output format\n2. Adicionar constraints e negative prompts\n3. Few-shot examples se necessário\n4. Testar iterativamente\n5. Usar `templates/prompt.md`", "- Objetivo do prompt\n- Exemplos de input/output", "- Prompt otimizado\n- Variantes testadas", "- [ ] Objetivo claro\n- [ ] Output format definido\n- [ ] Constraints explícitos\n- [ ] Exemplos concretos", "- **Upstream:** agent-creator\n- **Downstream:** agent-creator, skill-builder", "**Input:** Prompt vago para code review\n**Output:** Prompt estruturado com checklist e severity levels.", "- `templates/prompt.md`"),
    ("agent-creator", "Agent Creator", "Cria configurações de agentes: instruções, tools, handoffs.", "Projetar agentes especializados para automações.", "- Novo agente Codex/Cursor\n- Automação multi-step\n- Agent handoffs", "- Skill simples (skill-builder)\n- Código de aplicação", "1. Definir persona e escopo\n2. Listar tools/skills disponíveis\n3. Definir handoff rules\n4. Testar com casos reais\n5. Documentar limites", "- Objetivo do agente\n- prompt-engineer output", "- Agent config\n- Documentação de uso", "- [ ] Escopo delimitado\n- [ ] Tools corretas\n- [ ] Handoffs definidos\n- [ ] Testado com 2+ casos", "- **Upstream:** prompt-engineer\n- **Downstream:** skill-builder", "**Input:** Agente de triagem de bugs\n**Output:** Agent que classifica e roteia para bug-hunter.", "- `skills/orchestrator/SKILL.md`"),
    ("commercial", "Commercial", "Aspectos comerciais: propostas, pricing, contratos, ROI.", "Alinhar soluções técnicas com viabilidade comercial.", "- Proposta comercial\n- Pricing feature\n- ROI de solução", "- Implementação técnica pura\n- Bug fix", "1. Identificar valor entregue\n2. Estimar esforço vs retorno\n3. Riscos comerciais\n4. Proposta estruturada", "- Requisito de negócio\n- `context/business.md`", "- Análise comercial\n- Recomendação go/no-go", "- [ ] Valor quantificado\n- [ ] Esforço estimado\n- [ ] Riscos comerciais\n- [ ] Recomendação clara", "- **Upstream:** product-owner\n- **Downstream:** functional-spec", "**Input:** Feature premium analytics\n**Output:** ROI positivo em 6 meses, pricing tier Pro.", "- `context/business.md`"),
    ("support", "Support", "Triagem de suporte: classificar ticket, reproduzir, escalar.", "Resolver ou encaminhar tickets de suporte eficientemente.", "- Ticket de suporte\n- Reclamação de usuário\n- Triagem inicial", "- Desenvolvimento de feature\n- Code review", "1. Classificar severidade e impacto\n2. Reproduzir se possível\n3. Workaround temporário se urgente\n4. Escalar para bug-hunter se técnico\n5. Comunicar status ao usuário", "- Ticket/descrição\n- Logs/screenshots", "- Resolução ou escalonamento\n- Comunicação ao usuário", "- [ ] Severidade classificada\n- [ ] Reproduzido ou N/A\n- [ ] Workaround se aplicável\n- [ ] Escalonado se necessário", "- **Upstream:** orchestrator\n- **Downstream:** bug-hunter, deployment", "**Input:** \"Não consigo login\"\n**Output:** Escalado P2 — OAuth callback 404, bug-hunter.", "- `workflows/support.md`"),
    ("deployment", "Deployment", "Implantação: release, rollback, smoke tests, feature flags.", "Executar deploy seguro com validação pós-deploy.", "- Deploy produção/staging\n- Rollback\n- Release pipeline", "- Desenvolvimento local\n- Code review", "1. Verificar checklist pre-deploy\n2. Executar pipeline ou instruir passos\n3. Smoke tests pós-deploy\n4. Monitorar erros iniciais\n5. Plano de rollback documentado", "- Release notes\n- Artefatos buildados", "- Deploy concluído\n- Smoke test results", "- [ ] Pre-deploy checklist ok\n- [ ] Deploy executado\n- [ ] Smoke tests passando\n- [ ] Rollback plan ready", "- **Upstream:** qa, release-notes\n- **Downstream:** support (monitoring)", "**Input:** Deploy v2.3\n**Output:** Staging ok, prod deployed, smoke login OK.", "- `checklists/deploy.md`\n- `workflows/deployment.md`"),
    ("finance", "Finance", "Aspectos financeiros: billing, custos cloud, invoicing.", "Avaliar impacto financeiro de decisões técnicas.", "- Billing feature\n- Cost optimization\n- Pricing técnico", "- UI/UX pura\n- Bug fix sem impacto financeiro", "1. Identificar fluxo monetário\n2. Compliance (PCI, etc.) se pagamentos\n3. Estimar custos infra\n4. Documentar requisitos financeiros", "- Commercial analysis\n- Feature requirements", "- Requisitos financeiros\n- Estimativa de custos", "- [ ] Fluxo monetário mapeado\n- [ ] Compliance verificada\n- [ ] Custos estimados", "- **Upstream:** commercial, product-owner\n- **Downstream:** functional-spec, security-review", "**Input:** Stripe integration\n**Output:** PCI scope, webhook idempotency required.", "- `context/business.md`"),
    ("data", "Data", "Analytics, ETL, pipelines, relatórios, data modeling.", "Soluções de dados: pipelines, queries analíticas, dashboards.", "- Pipeline ETL\n- Relatório/analytics\n- Data modeling", "- CRUD app simples (backend)\n- UI sem dados", "1. Definir fontes e destinos\n2. Modelar dados analíticos\n3. Pipeline idempotente\n4. Validar qualidade dos dados\n5. Documentar schema analítico", "- Requisitos de reporting\n- Sources disponíveis", "- Pipeline/queries\n- Documentação de dados", "- [ ] Schema definido\n- [ ] Pipeline idempotente\n- [ ] Data quality checks\n- [ ] Performance acceptable", "- **Upstream:** product-owner\n- **Downstream:** backend, qa", "**Input:** Dashboard vendas\n**Output:** ETL daily + star schema + API aggregation.", "- `context/domain.md`"),
    ("devops", "DevOps", "CI/CD, Docker, infra, monitoring, IaC.", "Automatizar build, deploy e observabilidade.", "- Pipeline CI/CD\n- Docker/K8s\n- Monitoring/alerting\n- Infra changes", "- Código applicativo\n- UX design", "1. Analisar pipeline existente\n2. Alteração mínima no CI/CD\n3. Secrets via vault/env — nunca commit\n4. Health checks e monitoring\n5. Documentar runbook", "- Repo structure\n- Deploy requirements", "- Pipeline config\n- Runbook updates", "- [ ] Pipeline verde\n- [ ] Secrets seguros\n- [ ] Health checks\n- [ ] Rollback testado", "- **Upstream:** performance, deployment\n- **Downstream:** deployment, qa", "**Input:** Build lento 15min\n**Output:** Cache npm/dotnet — 4min.", "- `checklists/deploy.md`\n- `rules/security.md`"),
    ("security-review", "Security Review", "Análise de segurança: OWASP, auth, secrets, injection.", "Identificar vulnerabilidades antes de merge/deploy.", "- Auth/pagamentos/PII\n- Após code-review em área sensível\n- Solicitação explícita", "- UI cosmética\n- Docs sem código", "1. OWASP Top 10 checklist\n2. Auth/authz flows\n3. Input validation, injection\n4. Secrets scan\n5. Usar `checklists/security.md`", "- Code diff\n- Architecture de auth", "- Security findings\n- Severity classification", "- [ ] Injection checked\n- [ ] Auth/authz valid\n- [ ] Secrets not exposed\n- [ ] HTTPS/TLS\n- [ ] Dependencies scanned", "- **Upstream:** code-review\n- **Downstream:** backend (fixes)", "**Input:** PR login endpoint\n**Output:** Medium — rate limiting missing.", "- `rules/security.md`\n- `checklists/security.md`"),
    ("skill-builder", "Skill Builder", "Cria novas skills seguindo o padrão exato do Personal AI Framework.", "Padronizar criação e registro de novas skills.", "- Nova skill necessária\n- Skill existente desatualizada\n- Expansão do framework", "- Criar agent completo (agent-creator)\n- Implementar código", "1. Definir nome (kebab-case) e description (third person + triggers)\n2. Preencher todas seções do SKILL.md template\n3. Criar pasta `skills/<name>/SKILL.md`\n4. Registrar em `workflows/_index.md` e `AGENTS.md`\n5. Adicionar exemplo em `examples/` se útil\n6. Manter <500 linhas; progressive disclosure", "- Propósito da skill\n- Trigger scenarios\n- Integrações", "- SKILL.md completo\n- Registros atualizados", "- [ ] Frontmatter name + description\n- [ ] Todas 9 seções preenchidas\n- [ ] <500 linhas\n- [ ] Registrado no índice\n- [ ] Exemplo concreto", "- **Upstream:** agent-creator, orchestrator\n- **Downstream:** (nova skill)", "**Input:** Skill para migrations EF\n**Output:** skills/ef-migrations/SKILL.md registrada.", "- Template: seções deste SKILL.md\n- `rules/token-economy.md`"),
]

WORKFLOWS_EXTRA = {
    "incident": ("Incidente", "Bug Hunter → Tech Lead → [fix urgente] → Deployment → Release Notes", "bug-hunter, tech-lead, deployment, release-notes", "checklists/bug.md"),
    "refactor": ("Refatoração", "Context → Architect → Tech Lead → Impl → QA → Review", "context-builder, software-architect, tech-lead, code-review", "checklists/review.md"),
    "database": ("Database", "Context → Database → Backend → QA → Review", "context-builder, database, backend, qa, code-review", "checklists/database.md"),
    "api": ("API", "Func Spec → API → Backend → QA → Review", "functional-spec, api, backend, qa, code-review", "checklists/api.md"),
    "integration": ("Integração", "Func Spec → Architect → API → Backend → QA → Review", "functional-spec, software-architect, api, backend", "checklists/api.md"),
    "devops": ("DevOps", "Context → DevOps → QA → Review", "context-builder, devops, qa, code-review", "checklists/deploy.md"),
    "testing": ("Testes", "QA → Playwright* → Review", "qa, playwright, code-review", "checklists/feature.md"),
    "architecture": ("Arquitetura", "Context → Architect → Technical Spec → Review", "context-builder, software-architect, technical-spec", "checklists/review.md"),
    "product": ("Produto", "Product Owner → Functional Spec", "product-owner, functional-spec", "checklists/feature.md"),
    "ux": ("UX", "UX → Func Spec → Review", "ux, functional-spec, code-review", "checklists/frontend.md"),
    "mobile": ("Mobile", "Mobile UX → Flutter* → QA → Review", "mobile-ux, flutter, qa, code-review", "checklists/frontend.md"),
    "security": ("Segurança", "Security Review → [fix] → QA → Review", "security-review, qa, code-review", "checklists/security.md"),
    "data": ("Dados", "Data → Backend → QA → Review", "data, backend, qa, code-review", "checklists/backend.md"),
    "commercial": ("Comercial", "Commercial → Func Spec", "commercial, functional-spec", "checklists/feature.md"),
    "finance": ("Financeiro", "Finance → Func Spec → Review", "finance, functional-spec, code-review", "checklists/review.md"),
    "deployment": ("Implantação", "Deployment → QA → Release Notes", "deployment, qa, release-notes", "checklists/deploy.md"),
    "support": ("Suporte", "Support → Bug Hunter* → [resolução]", "support, bug-hunter", "checklists/bug.md"),
}

RULES = {
    "clean-code": ("Clean Code", "Código legível, funções pequenas, nomes expressivos, DRY sem over-abstraction.", [
        "Funções ≤30 linhas quando possível",
        "Nomes revelam intenção — sem abreviações obscuras",
        "Um nível de abstração por função",
        "Evitar comentários que repetem código",
        "Early return em vez de nesting profundo",
        "Sem código morto ou comentado",
    ]),
    "solid": ("SOLID", "Princípios SOLID para design orientado a objetos.", [
        "S — Uma razão para mudar por classe/módulo",
        "O — Aberto para extensão, fechado para modificação",
        "L — Subtipos substituíveis",
        "I — Interfaces específicas, não gordas",
        "D — Depender de abstrações",
    ]),
    "architecture": ("Architecture", "Decisões arquiteturais consistentes e documentadas.", [
        "Respeitar camadas existentes do projeto",
        "Boundaries claros entre módulos",
        "ADR para decisões significativas",
        "Evitar acoplamento circular",
        "Preferir composição sobre herança",
    ]),
    "performance": ("Performance", "Otimização baseada em medição.", [
        "Medir antes de otimizar",
        "Atacar o gargalo principal (80/20)",
        "Cache com invalidação explícita",
        "Lazy loading quando apropriado",
        "Evitar premature optimization",
    ]),
    "naming": ("Naming", "Convenções de nomenclatura consistentes.", [
        "Classes: PascalCase (C#), PascalCase components (React)",
        "Métodos/funções: verbo + substantivo (GetOrderById)",
        "Bool: Is/Has/Can prefix",
        "Constantes: UPPER_SNAKE ou PascalCase conforme linguagem",
        "Arquivos: kebab-case ou convenção do framework",
    ]),
    "git": ("Git", "Práticas Git seguras.", [
        "Commits atômicos com mensagem clara",
        "Nunca force push main/master sem autorização",
        "Nunca commitar secrets",
        "Não commitar salvo pedido explícito do usuário",
        "Branch descritiva: feat/, fix/, refactor/",
    ]),
    "security": ("Security", "Segurança em código e infra.", [
        "Validar toda input externa",
        "Parameterized queries — nunca SQL concat",
        "Secrets em env/vault — nunca no código",
        "Princípio do menor privilégio",
        "HTTPS everywhere; cookies secure/httpOnly",
    ]),
    "testing": ("Testing", "Testes úteis e direcionados.", [
        "Testar comportamento, não implementação",
        "AAA: Arrange, Act, Assert",
        "Um assert lógico por teste quando possível",
        "Rodar apenas testes relacionados à mudança",
        "E2E para fluxos críticos; unit para lógica",
    ]),
    "api": ("API", "Design de APIs REST consistente.", [
        "Recursos pluralizados: /orders não /order",
        "HTTP verbs corretos: GET read, POST create, PUT/PATCH update, DELETE remove",
        "Status codes semânticos: 201 created, 404 not found, 422 validation",
        "Paginação em listagens: page, pageSize ou cursor",
        "Versionamento quando breaking change",
    ]),
    "database": ("Database", "Boas práticas de banco de dados.", [
        "Migrations reversíveis (up/down)",
        "Índices em colunas de filtro/join frequentes",
        "Evitar SELECT * em produção",
        "Transações para operações multi-step",
        "Naming: snake_case ou PascalCase conforme ORM",
    ]),
    "documentation": ("Documentation", "Documentação útil e mantível.", [
        "Documentar WHY, não WHAT óbvio",
        "README com setup reproduzível",
        "API docs auto-geradas quando possível",
        "ADRs para decisões arquiteturais",
        "Manter docs próximos ao código",
    ]),
}

TEMPLATES = {
    "functional-spec": "# Especificação Funcional\n\n> Projeto: [nome] | Feature: [nome] | Data: [data]\n\n## Objetivo\n[Valor de negócio]\n\n## Escopo\n**In:** ...\n**Out:** ...\n\n## Personas\n- [Persona]: [necessidade]\n\n## Fluxos\n### Fluxo principal\n1. ...\n\n### Fluxos alternativos\n- ...\n\n## Regras de negócio\n- RN01: ...\n\n## Critérios de aceite\n- [ ] CA01: Given ... When ... Then ...\n",
    "technical-spec": "# Especificação Técnica\n\n> Feature: [nome] | Autor: [agent] | Data: [data]\n\n## Visão geral\n[Resumo técnico]\n\n## Componentes\n| Componente | Responsabilidade |\n|------------|------------------|\n| ... | ... |\n\n## Modelo de dados\n```\n[Entidades e relações]\n```\n\n## API / Contratos\n| Método | Path | Request | Response |\n|--------|------|---------|----------|\n| ... | ... | ... | ... |\n\n## Dependências\n- ...\n\n## Riscos técnicos\n- ...\n",
    "bug-report": "# Bug Report\n\n## Resumo\n[1 linha]\n\n## Severidade\n[P1/P2/P3/P4]\n\n## Passos para reproduzir\n1. ...\n\n## Comportamento esperado\n...\n\n## Comportamento atual\n...\n\n## Ambiente\n- OS: ...\n- Browser/App: ...\n- Versão: ...\n\n## Logs/Stack\n```\n...\n```\n",
    "feature-request": "# Feature Request\n\n## Título\n...\n\n## Problema\n[O que o usuário precisa]\n\n## Proposta\n[Solução sugerida]\n\n## Critérios de aceite\n- [ ] ...\n\n## Prioridade\n[Alta/Média/Baixa]\n",
    "adr": "# ADR-[NNN]: [Título]\n\n## Status\n[Proposed | Accepted | Deprecated]\n\n## Contexto\n[Forças e constraints]\n\n## Decisão\n[O que foi decidido]\n\n## Consequências\n### Positivas\n- ...\n### Negativas\n- ...\n",
    "release-notes": "# Release Notes — v[X.Y.Z]\n\n## Added\n- ...\n\n## Changed\n- ...\n\n## Fixed\n- ...\n\n## Removed\n- ...\n\n## Breaking Changes\n- ...\n",
    "changelog": "# Changelog\n\nFormato [Keep a Changelog](https://keepachangelog.com/).\n\n## [Unreleased]\n### Added\n- ...\n### Fixed\n- ...\n",
    "prompt": "# Prompt Template\n\n## Role\n[Você é...]\n\n## Objective\n[Objetivo claro]\n\n## Constraints\n- [Restrição 1]\n- [Não fazer X]\n\n## Output Format\n```\n[Formato esperado]\n```\n\n## Examples\n### Input\n...\n### Output\n...\n",
    "root-cause-analysis": "# Root Cause Analysis\n\n## Incidente\n[Descrição]\n\n## Timeline\n| Hora | Evento |\n|------|--------|\n| ... | ... |\n\n## Causa raiz\n[5 Whys ou análise]\n\n## Fix aplicado\n...\n\n## Prevenção\n- [ ] ...\n",
    "test-plan": "# Test Plan\n\n## Escopo\n[O que testar]\n\n## Casos de teste\n| ID | Cenário | Steps | Expected |\n|----|---------|-------|----------|\n| T01 | ... | ... | ... |\n\n## Ambiente\n...\n\n## Critérios de saída\n- [ ] Todos P1 passando\n",
    "migration": "# Migration Plan\n\n## Migration\n[Nome]\n\n## Up\n```sql\n...\n```\n\n## Down\n```sql\n...\n```\n\n## Impacto\n- Tabelas: ...\n- Downtime: ...\n\n## Rollback\n[Procedimento]\n",
}

CHECKLISTS = {
    "bug": ["Reproduzido localmente", "Causa raiz identificada", "Fix mínimo aplicado", "Teste de regressão", "Sem efeitos colaterais", "Release note se aplicável"],
    "feature": ["Critérios de aceite atendidos", "Testes novos/atualizados", "Docs atualizadas", "UI pt-BR se aplicável", "Code review ok", "Changelog atualizado"],
    "api": ["Contrato documentado", "Validação input", "Status codes corretos", "Auth/authz", "Paginação se listagem", "Breaking changes comunicados"],
    "frontend": ["Loading/error/empty states", "Responsivo", "A11y básica", "Tipagem correta", "Sem console.log", "Mensagens pt-BR"],
    "backend": ["Camadas respeitadas", "Validação entrada", "Erros tratados", "Logs adequados", "Sem secrets", "Testes unitários"],
    "database": ["Migration reversível", "Índices adequados", "Sem data loss", "Testado up/down", "Naming consistente"],
    "performance": ["Baseline medido", "Gargalo identificado", "Fix aplicado", "Melhoria quantificada", "Sem regressão funcional"],
    "review": ["Lógica correta", "Edge cases", "Testes adequados", "Convenções", "Sem debug code", "Diff mínimo"],
    "release": ["Changelog atualizado", "Release notes", "Version bump", "Smoke tests", "Rollback plan"],
    "security": ["Input validation", "Auth/authz", "No secrets in code", "Injection prevention", "Dependencies scanned", "HTTPS/TLS"],
    "migration": ["Up script testado", "Down script testado", "Backup plan", "Downtime estimado", "Rollback documentado"],
    "deploy": ["Pre-deploy checklist", "Secrets configurados", "Health checks", "Smoke tests pós-deploy", "Monitoring ativo", "Rollback testado"],
}

CONTEXT = {
    "architecture": "# Architecture Context\n\n> Copie este arquivo para cada projeto e preencha.\n\n## Visão geral\n[Monolito / Microservices / Modular monolith]\n\n## Camadas\n```\n[Diagrama ou lista de camadas]\n```\n\n## Módulos principais\n| Módulo | Responsabilidade |\n|--------|------------------|\n| ... | ... |\n\n## Integrações externas\n- ...\n",
    "business": "# Business Context\n\n## Empresa / Produto\n[Nome, segmento]\n\n## Usuários\n[Personas principais]\n\n## Modelo de negócio\n[Como monetiza]\n\n## Glossário\n| Termo | Definição |\n|-------|----------|\n| ... | ... |\n",
    "patterns": "# Patterns Context\n\n## Padrões utilizados\n- Repository Pattern\n- CQRS\n- Event Sourcing\n- ...\n\n## Anti-patterns a evitar\n- ...\n\n## Referências internas\n- [Link para ADRs]\n",
    "tech-stack": "# Tech Stack Context\n\n## Backend\n- Linguagem: \n- Framework: \n- ORM: \n- DB: \n\n## Frontend\n- Framework: \n- State: \n- CSS: \n\n## Infra\n- Cloud: \n- CI/CD: \n- Container: \n",
    "domain": "# Domain Context\n\n## Entidades principais\n| Entidade | Descrição |\n|----------|----------|\n| ... | ... |\n\n## Regras de negócio críticas\n- RN01: ...\n\n## Eventos de domínio\n- ...\n",
    "coding-standards": "# Coding Standards Context\n\n## Geral\n- Idioma UI: pt-BR\n- Commits: conventional commits\n\n## Backend\n[Convenções específicas]\n\n## Frontend\n[Convenções específicas]\n\n## Linting\n[Comandos e configs]\n",
}

EXAMPLES = {
    "bug-investigation": "# Exemplo: Investigação de Bug\n\n**Pedido:** \"Umbra apresentou erro ao salvar pedido\"\n\n**Orchestrator:** tipo=bug\n\n**Pipeline executado:**\n1. context-builder → monorepo .NET+Angular\n2. bug-hunter → NullRef OrderService:42\n3. tech-lead → fix validation CustomerId\n4. backend → patch 3 lines\n5. qa → 2 unit tests pass\n6. code-review → approved\n7. release-notes → \"Fixed: erro ao salvar pedido\"\n",
    "feature-oauth": "# Exemplo: Feature OAuth\n\n**Pedido:** \"Implemente Login com Google\"\n\n**Pipeline:** product-owner → functional-spec → ux → architect → tech-lead → backend+api → qa → review → changelog\n\n**Artefatos:** functional-spec.md, ADR-001 OAuth provider, 4 endpoints, 12 tests\n",
    "pr-review": "# Exemplo: PR Review\n\n**Pedido:** \"Revise esta Pull Request\"\n\n**Pipeline:** code-review → security-review\n\n**Output:** 1 Critical (missing auth), 2 Suggestions, Approved after fixes\n",
    "performance-api": "# Exemplo: Performance\n\n**Pedido:** \"API de pedidos está lenta\"\n\n**Pipeline:** performance → database → backend → qa\n\n**Resultado:** N+1 fix, 10s → 180ms\n",
    "documentation-screen": "# Exemplo: Documentação\n\n**Pedido:** \"Documente a tela de KB\"\n\n**Pipeline:** context-builder → technical-spec → functional-spec → review\n",
    "new-skill": "# Exemplo: Nova Skill\n\n**Pedido:** \"Preciso de skill para EF migrations\"\n\n**Pipeline:** skill-builder\n\n**Output:** skills/ef-migrations/SKILL.md + registro no _index.md\n",
}


def write_skill(name, title, description, objective, when_use, when_not, responsibilities, inputs, outputs, checklist, integration, examples, references):
    resp_lines = responsibilities if isinstance(responsibilities, str) else "\n".join(f"{i}. {r}" for i, r in enumerate(responsibilities.split("\n"), 1)) if "\n" in str(responsibilities) else responsibilities
    content = SKILL_TEMPLATE.format(
        name=name,
        description=description,
        title=title,
        objective=objective,
        when_use=when_use,
        when_not=when_not,
        responsibilities=resp_lines,
        inputs=inputs,
        outputs=outputs,
        checklist=checklist,
        integration=integration,
        examples=examples,
        references=references,
    )
    path = ROOT / "skills" / name / "SKILL.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main():
    # Skills
    for args in SKILLS:
        write_skill(*args)

    # Extra workflows
    for key, (title, pipeline, skills, checklist) in WORKFLOWS_EXTRA.items():
        content = f"""# Workflow: {title}

> Pipeline automático — ver `workflows/_index.md`

## Trigger
`{key}`

## Pipeline

```
{pipeline}
```

## Skills
{', '.join(f'`{s}`' for s in skills.split(', '))}

## Checklist
- `{checklist}`
- `checklists/review.md`

## Rules
- `rules/token-economy.md`
"""
        (ROOT / "workflows" / f"{key}.md").write_text(content, encoding="utf-8")

    for sub in ("rules", "templates", "checklists", "context", "examples", "workflows"):
        (ROOT / sub).mkdir(parents=True, exist_ok=True)

    # Rules
    for key, (title, desc, items) in RULES.items():
        body = f"# {title}\n\n> Finalidade: {desc}\n\n## Regras\n\n" + "\n".join(f"- {i}" for i in items) + "\n"
        (ROOT / "rules" / f"{key}.md").write_text(body, encoding="utf-8")

    # Templates
    for key, body in TEMPLATES.items():
        header = f"<!-- Template: {key} — Personal AI Framework -->\n\n"
        (ROOT / "templates" / f"{key}.md").write_text(header + body, encoding="utf-8")

    # Checklists
    for key, items in CHECKLISTS.items():
        body = f"# Checklist: {key.replace('-', ' ').title()}\n\n> Finalidade: validação para tarefas tipo `{key}`.\n\n" + "\n".join(f"- [ ] {i}" for i in items) + "\n"
        (ROOT / "checklists" / f"{key}.md").write_text(body, encoding="utf-8")

    # Context
    for key, body in CONTEXT.items():
        (ROOT / "context" / f"{key}.md").write_text(body, encoding="utf-8")

    # Examples
    for key, body in EXAMPLES.items():
        (ROOT / "examples" / f"{key}.md").write_text(body, encoding="utf-8")

    print(f"Generated framework at {ROOT}")
    print(f"Skills: {len(list((ROOT / 'skills').glob('*/SKILL.md')))}")
    print(f"Workflows: {len(list((ROOT / 'workflows').glob('*.md')))}")
    print(f"Rules: {len(list((ROOT / 'rules').glob('*.md')))}")


if __name__ == "__main__":
    main()
