# Modos de Operação

> Finalidade: o Orchestrator escolhe **um** modo por tarefa para balancear qualidade e consumo de tokens.

## Visão geral

Antes dos modos operacionais, o Strategic Intelligence Layer pode escolher um Mission Mode: Analysis, Planning, Implementation, Validation, Continuous Improvement, Innovation, Emergency ou Learning. O Mission Mode não substitui Fast/Standard/Review/Council; ele orienta o Orchestrator.

Quando a execucao acontecer no Codex, selecionar tambem o modelo e o nivel de raciocinio conforme
`../docs/CODEX_MODEL_SELECTION.md`. O modo operacional define o processo; o modelo Codex define a
capacidade de raciocinio disponivel para executar esse processo com seguranca.

```mermaid
flowchart TB
    U[Pedido do usuário] --> O[Orchestrator]
    O --> M{Modo?}
    M -->|Fast| F[Executa sozinho]
    M -->|Standard| S[Context → Técnica → QA]
    M -->|Review| R[Context → Técnicas → Critic → Validator]
    M -->|Council| C[Technical Council → Planner → Exec → Validator]
    F --> E[Entrega]
    S --> E
    R --> E
    C --> E
```

## MODE 1 — Fast

**Usar para:** perguntas, dúvidas, documentação simples, pequenas alterações (1 arquivo, sem risco).

```
Orchestrator → Executa sozinho → Entrega
```

- Nenhuma outra skill é chamada
- Resposta direta e concisa
- Working Context mínimo ou ausente

**Sinais:** "o que é", "como funciona", "explique", typo, comentário, doc de 1 parágrafo

## MODE 2 — Standard

**Usar para:** bugs pequenos, melhorias pontuais, features pequenas (1–2 módulos, baixo risco).

```
Orchestrator → Context Builder → Skill Técnica → QA → Entrega
```

- Context Builder só se contexto insuficiente
- Uma skill técnica principal (backend, api, react, etc.)
- QA valida fix/feature mínima
- Sem Critic salvo regressão óbvia

**Sinais:** bug isolado, ajuste de UI, endpoint simples, teste faltando

## MODE 3 — Review

**Usar para:** alteração estrutural, banco, autenticação, pagamentos, integrações, performance.

```
Orchestrator → Context Builder → Skills Técnicas → Critic → Validator → Entrega
```

- Múltiplas skills técnicas se necessário
- Critic obrigatório antes de considerar pronto
- Validator obrigatório (testes, lint, build quando aplicável)
- Risk Reviewer se auth/dados sensíveis

**Sinais:** migration, OAuth, webhook, query lenta, mudança de contrato API

## MODE 4 — Technical Council

**Usar para:** risco elevado, múltiplos módulos (>3), mudanças arquiteturais, refatorações grandes, incidentes críticos, produção, decisão técnica importante.

```
Orchestrator → Technical Council → Decision Maker → Implementation Planner
    → Execução (skills técnicas) → Validator → Entrega
```

- Conselho montado sob demanda — ver `technical-council.md`
- Decision Maker resolve conflitos (nunca fala com usuário)
- Usuário vê **somente decisão consolidada**

**Sinais:** "refatorar módulo inteiro", incidente produção, nova arquitetura, pagamentos, >3 módulos

## Matriz de decisão rápida

| Fator | Fast | Standard | Review | Council |
|-------|------|----------|--------|---------|
| Arquivos afetados | 0–1 | 1–3 | 2–5 | >3 ou arquitetura |
| Risco | Muito baixo | Baixo | Médio | Alto/Crítico |
| Módulos | 1 | 1–2 | 2–3 | >3 |
| Produção | Não | Não | Possível | Sim/incidente |
| Auth/DB/Pagamento | Não | Não | Sim | Sim + conselho |

## Matriz Codex

| Modo | Modelo sugerido | Raciocinio sugerido |
|------|-----------------|---------------------|
| Fast | `GPT-5.3-Codex-Spark` ou `GPT-5.4-Mini` | `Baixa` |
| Standard | `GPT-5.4-Mini` ou `GPT-5.4` | `Media` |
| Review | `GPT-5.4` ou `GPT-5.5` | `Alta` |
| Technical Council | `GPT-5.5` | `Altissimo` |

Para Umbra RAG, usar `GPT-5.5` com `Alta` durante implementacao e `Altissimo` para decisoes de arquitetura, seguranca, banco, permissoes, deploy ou producao.

## Escalonamento

O Orchestrator pode **subir** de modo durante a execução se descobrir maior complexidade:

```
Fast → Standard → Review → Technical Council
```

Nunca **descer** de modo sem reavaliar risco.

## Mapeamento workflow → modo sugerido

| Workflow | Modo padrão | Escala para Council se |
|----------|-------------|------------------------|
| bug | Standard | produção, >3 módulos |
| feature | Standard/Review | auth, pagamento, arquitetura |
| incident | Council | sempre (produção) |
| refactor | Review/Council | grande escopo |
| review | Fast/Standard | N/A |
| documentation | Fast | N/A |
| security | Review/Council | sempre Council se auth |
| architecture | Council | sempre |
| database | Review/Council | migration em produção |
| marketing | Standard/Review | redesign amplo, rebranding, Product Audit, >3 módulos ou decisão de marca crítica |
| infrastructure-mission | Standard/Review | credenciais, seguranca, producao, multiplos ambientes ou integracao critica |
