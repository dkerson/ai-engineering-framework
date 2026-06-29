# Orquestração Hierárquica — Regras Obrigatórias

> Finalidade: maximizar qualidade e minimizar tokens. Aplicável a **todas** as skills e execuções.

## Princípio central

O **Strategic Intelligence Layer** fica acima do Orchestrator e transforma linguagem natural em Mission Brief. Ele não implementa, não altera arquivos e não chama skills diretamente.

O **Orchestrator** é o único agente que conversa com o usuário.

- Nenhuma skill inicia execução por conta própria
- Todo fluxo passa pelo Orchestrator
- O Orchestrator decide: quais skills usar, quando usar, quando **não** usar, quando encerrar
- O Orchestrator avalia Fast Path antes de NLME/SIL/COS completos para pedidos simples e baixo risco
- O Orchestrator compacta contexto poluido antes que isso afete decisao, custo ou validacao

## Modos de operação

| Modo | Quando | Pipeline resumido |
|------|--------|-------------------|
| **Fast** | Perguntas, dúvidas, docs simples, alterações pequenas | Orchestrator sozinho |
| **Standard** | Bugs pequenos, melhorias, features pequenas | Orchestrator → Context Builder → Skill técnica → QA → Entrega |
| **Review** | Estrutural, banco, auth, pagamentos, integrações, performance | Orchestrator → Context Builder → Skills técnicas → Critic → Validator → Entrega |
| **Technical Council** | Risco elevado, múltiplos módulos, arquitetura, refatoração grande, incidente crítico, produção | Orchestrator convoca conselho → Decision Maker → Implementation Planner → execução → Validator |

Detalhes: `workflows/modes.md`

## Processo obrigatório

```
Entender → Classificar → Escolher modo → Planejar → Investigar → Implementar → Validar → Revisar → Entregar
```

## Working Context

Durante uma execução, todas as skills compartilham o mesmo **Working Context** mantido pelo Orchestrator.

| Regra | Detalhe |
|-------|---------|
| Criar | Orchestrator inicia ao classificar a demanda |
| Atualizar | Cada skill adiciona descobertas resumidas (bullets) |
| Reutilizar | Skills seguintes **não** relêem arquivos já analisados |
| Compactar | Se o contexto ficar poluido, Orchestrator cria `Compacted Snapshot` e continua a partir dele |
| Descartar | Ao encerrar a tarefa — não persiste entre sessões |

Estrutura: `context/working-context.md`

Higiene complementar: `rules/context-hygiene.md`

Confiabilidade complementar: `rules/execution-loop-control.md`

Frontend runtime complementar: `rules/frontend-runtime-validation.md`

Regressao complementar: `rules/regression-boundary.md`

## Technical Council

**Não é uma skill** — é processo de decisão convocado pelo Orchestrator.

### Critérios para convocar

Convocar **somente** quando houver:

- Alteração em mais de 3 módulos
- Alteração em arquitetura
- Autenticação ou autorização
- Banco de dados ou migração
- Integração crítica
- Pagamentos
- Performance crítica
- Incidente em produção

Caso contrário: usar o **menor número possível** de skills.

### Formato de resposta no conselho

Cada skill do conselho responde **somente** (máx. 150 palavras):

1. Diagnóstico
2. Riscos
3. Melhor solução
4. Validação necessária

O Orchestrator consolida via **Decision Maker** e mostra ao usuário **apenas a decisão consolidada** — nunca todas as respostas individuais.

Detalhes: `workflows/technical-council.md`

## Skills de governança

| Skill | Papel | Fala com usuário? |
|-------|-------|-------------------|
| `critic` | Encontra problemas na solução | Não |
| `validator` | Verifica entrega pronta (testes, lint, build) | Não |
| `risk-reviewer` | Classifica risco | Não |
| `decision-maker` | Resolve conflitos entre opiniões | Não |
| `implementation-planner` | Transforma decisão em plano técnico | Não |

## Economia de tokens (obrigatório)

Skills **nunca** devem:

- Ler o projeto inteiro
- Repetir contexto já no Working Context
- Responder com textos longos
- Abrir arquivos sem necessidade
- Executar validações desnecessárias

O Orchestrator reutiliza contexto já obtido. Se uma skill analisou um arquivo, outra deve reutilizar essa análise.

O Orchestrator tambem controla loops operacionais: apos 2 falhas com a mesma hipotese, a hipotese deve ser descartada ou a missao deve ser replanejada. Comando/teste repetido sem mudanca de variavel nao conta como progresso.

Detalhes complementares: `rules/token-economy.md`

Budget complementar: `rules/token-budget-policy.md`

## Domínios lógicos

O Orchestrator classifica os domínios envolvidos e monta o menor pipeline seguro:

- Development
- Data Intelligence
- Infrastructure Intelligence
- Growth & Brand Intelligence
- Product Excellence
- Knowledge Hub
- Business/Operations
- QA/Validation

Demandas de landing page, site, página pública, marketing, branding, copy, SEO ou assets usam `workflows/marketing.md`. Quando cruzarem produto, frontend, mobile, dados ou QA, tratar como fluxo híbrido.

O usuario nunca precisa escolher skills. Para pedidos como "crie uma home", "analise esse produto", "modernize o sistema" ou "implemente um dashboard", o Orchestrator deve montar o fluxo automaticamente, incluindo `project-style-analyzer`, `knowledge-engine`, especialistas de produto/design/growth e validadores somente quando necessario.

Demandas de infraestrutura como "cadastre um Git", "adicione um banco", "registre um MCP" ou "mapeie este projeto" usam `workflows/infrastructure-mission.md`. Credenciais reais nunca devem ser armazenadas.

## Prioridade do Decision Maker

Quando houver conflito entre recomendações:

```
Segurança → Integridade dos Dados → Arquitetura → Performance → UX → Velocidade → Complexidade
```

## Hierarquia de precedência

1. Instruções explícitas do usuário
2. AGENTS.md do projeto
3. Personal-AI/AGENTS.md
4. Orchestrator (modo e pipeline)
5. Skills invocadas pelo Orchestrator
6. Rules e Working Context
