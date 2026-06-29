# Token Economy — Regras Obrigatórias



> Finalidade: minimizar consumo de tokens sem sacrificar qualidade. Aplicável a **todas** as skills e execuções.



Complemento obrigatório: `rules/hierarchical-orchestration.md`

Complemento de budget: `rules/token-budget-policy.md`

Complemento de higiene de contexto: `rules/context-hygiene.md`

Complemento de confiabilidade de execucao: `rules/execution-loop-control.md`

Complemento de runtime frontend: `rules/frontend-runtime-validation.md`

Complemento de regressao: `rules/regression-boundary.md`

Complemento anti-hardcode: `rules/no-hardcode.md`



## Regras absolutas

Strategic Intelligence Layer:

- Nunca abre arquivos
- Nunca executa comandos
- Nunca chama skills diretamente
- Nunca implementa codigo
- Apenas interpreta, planeja e entrega Mission Brief ao Orchestrator

Natural Language Mission Engine (NLME):

- mission-translator, mission-builder, prompt-builder nunca abrem codigo do projeto
- Nunca expoem Structured Prompt ao usuario
- Entregam Mission Package ao SIL



Skills **nunca** devem:



- Ler o projeto inteiro

- Repetir contexto já no Working Context

- Responder com textos longos (Council: máx. 150 palavras/skill)

- Abrir arquivos sem necessidade

- Executar validações desnecessárias

- Auto-iniciar — somente via Orchestrator

Quando o contexto ativo ficar poluido, o Orchestrator deve compactar o Working Context antes de continuar. A compactacao preserva decisoes, evidencias, arquivos relevantes, plano ativo, validacoes e riscos; outputs brutos, hipoteses invalidadas e planos substituidos devem ser descartados operacionalmente.



O Orchestrator reutiliza contexto já obtido. Se uma skill analisou um arquivo, outra **deve** reutilizar essa análise.

Quando uma tentativa falhar, a proxima acao deve seguir `rules/execution-loop-control.md`: registrar Attempt Ledger, mudar variavel relevante e parar de repetir a mesma hipotese apos 2 falhas.

Ao criar ou alterar valores variaveis (ambiente, dominio, autorizacao, seeds, modulos, menus, status, thresholds), aplicar `rules/no-hardcode.md` antes de implementar.



## Modo mínimo



O Orchestrator escolhe o **menor modo seguro**:



```

Fast → Standard → Review → Technical Council

```



Não escalar modo sem justificativa de risco.

### Fast Path antes do NLME completo

Antes de acionar `mission-translator`, `mission-builder`, `prompt-builder`, SIL e COS, o Orchestrator deve verificar `rules/token-budget-policy.md`.

Use Fast Path quando o pedido for simples, direto e baixo risco. Exemplos: confirmar status, explicar um arquivo, rodar um comando simples, corrigir texto/typo, atualizar documentacao estreita ou responder uma pergunta de governanca usando documentos vivos.

Use o caminho completo NLME/SIL/COS quando houver ambiguidade, estrategia, multiplos dominios, produto/design/growth/data, arquitetura, auth, banco, seguranca, producao ou transformacao ampla.



## Investigação dirigida



**SEMPRE** localizar antes de ler em massa:



1. Mensagem de erro / stack trace

2. Arquivo e linha indicados

3. Função, componente ou endpoint envolvido

4. Working Context — arquivos já analisados



**NUNCA** percorrer todo o projeto "para entender contexto".

### SQL e dados (v2.1+)

Ao analisar SQL ou divergência de dados, seguir ordem em `rules/data/query-performance.md`:

1. Consulta enviada → 2. Erro/divergência → 3. Tabela principal → 4. Joins → 5. Filtros → 6. Agregações → 7. Procedures/views → 8. Plano de execução → 9. Índices → 10. API/tela se necessário

Não ler projeto inteiro. Demandas híbridas: `hybrid-flow-planner` define escopo mínimo por domínio.

### Growth, Brand e assets (v2.2+)

Antes de buscar ou gerar imagens, `asset-intelligence` deve:

1. Analisar se o asset e necessario.
2. Verificar assets existentes no projeto.
3. Verificar biblioteca interna/design system.
4. Decidir o tipo de recurso: logo, icone, SVG, ilustracao, imagem, mockup, screenshot ou outro.
5. So entao sugerir fonte publica, criacao ou otimizacao.

Nao criar dependencia visual externa quando icone, SVG ou asset interno resolver.

### Knowledge Hub (v2.3+)

O `knowledge-engine` deve consultar apenas areas relevantes em `knowledge/`:

- Landing Page: copywriting, branding, seo, design, ux, marketing
- Dashboard: dashboard, ux, analytics, design-system, performance
- Flutter: flutter, mobile, performance, design-system

Registrar no Working Context as areas consultadas. Nao copiar documentos inteiros para respostas ou entre skills.

### Infrastructure Intelligence (v2.6+)

Infrastructure Missions devem consultar primeiro registries existentes:

1. `infrastructure/projects/`
2. `infrastructure/registry/`
3. `infrastructure/catalog/`
4. Knowledge Hub de infraestrutura

Nao escanear projeto inteiro se o registry ja responder. Nunca carregar ou registrar credenciais reais.



## Leitura de arquivos



| Fazer | Não fazer |

|-------|-----------|

| Ler arquivo do erro + imports diretos | Abrir dezenas de arquivos por precaução |

| Usar grep/search para achar símbolos | Listar diretórios inteiros |

| Reutilizar análise do Working Context | Reler arquivo já catalogado |

| Ler testes do módulo alterado | Ler toda a suíte de testes |



## Contexto na conversa



- Resumir descobertas em 2–5 bullets no Working Context

- Avaliar `Context Health` em missoes longas, mudancas de plano e antes de validacoes amplas

- Criar `Compacted Snapshot` quando o contexto estiver `Polluted`

- Nunca repetir código já citado

- Citar trechos com `startLine:endLine:path` — não colar arquivo inteiro

- Evitar respostas longas; preferir ação + resumo



## Implementação



- **Menor alteração possível** que resolve o problema

- Evitar refatorações grandes não solicitadas

- Não adicionar abstrações "para o futuro"

- Não adicionar comentários óbvios



## Validação



| Modo | Validar |

|------|---------|

| Fast | Nenhuma (salvo pedido explícito) |

| Standard | QA — testes do módulo |

| Review | Critic + Validator |

| Council | Validator completo |



| Cenário | Executar |

|---------|----------|

| Bug fix pontual | Teste(s) do módulo afetado |

| Nova feature | Testes novos + relacionados |

| Refatoração ampla | Suíte do pacote |

| Build completo | Apenas Review/Council ou merge/deploy |

### Frontend runtime e regressao

Para telas, rotas, HTML e layout:

- validar porta/URL corretas antes de aceitar evidencia;
- confirmar cache/bundle coerente com a alteracao;
- checar console e network para erros novos relevantes;
- coletar evidencia visual ou DOM da rota alvo;
- aplicar `rules/regression-boundary.md` quando arquivo compartilhado for alterado;
- validar canarios definidos no Boundary Map antes de marcar pronto.



## Build e deploy



- Não rodar build completo após cada micro-alteração

- Frontend em watch: confiar no compilador do usuário quando aplicável

- CI local só quando Validator exigir



## Skills e rules



- Carregar apenas skills do pipeline atual (Orchestrator decide)

- Referenciar rules por link — não copiar conteúdo inteiro

- Usar templates de saída — não reinventar formato



## Resposta final



Somente o **Orchestrator** entrega ao usuário via `templates/final-response.md` — conciso, acionável, sem redundância.

## Execution Intelligence

Ao encerrar uma mission, registrar somente sinais uteis e baratos:

- `framework/operating-system/MISSION_LEDGER.md` para resumo da execucao.
- `framework/operating-system/SKILL_USAGE.md` para skills realmente usadas.
- `framework/operating-system/TOKEN_METRICS.md` para waste/savings.
- `framework/operating-system/PROMOTION_CRITERIA.md` para decidir quando um aprendizado vira recomendacao.

Nao registrar prompts completos, segredos, codigo longo ou dados privados. Nao alterar o framework automaticamente: registrar, recomendar e aguardar aprovacao.

