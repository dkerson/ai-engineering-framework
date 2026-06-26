# Usando o Framework em Projetos

> Umbra, Irisys e outros consumidores via Git Submodule.

## Instalação

Ver `docs/INSTALL.md`. Caminhos aceitos: `Personal-AI/`, `.ai/`, `ai-engineering-framework/`.

No `AGENTS.md` do projeto:

```markdown
## AI Engineering Framework
Bootstrap: [Personal-AI/AGENTS.md](Personal-AI/AGENTS.md) → `Personal-AI/skills/orchestrator/SKILL.md`
```

## Contexto por projeto

O framework fornece templates; o **projeto consumidor** preenche:

| Arquivo | Conteúdo |
|---------|----------|
| `context/tech-stack.md` | Stack (Angular, .NET, SQL Server, ...) |
| `context/business.md` | Regras de negócio do produto |
| `context/architecture.md` | Módulos e integrações |
| `context/semantic-layer/` | Override local da camada semântica |

Copiar de `context/_template/` ao iniciar.

## Equipe de desenvolvimento

Fluxos Standard/Review/Council como em v2.0 — sem mudança de bootstrap.

## Equipe de Dados/BI

1. Pedidos de SQL, Power BI, divergência, relatórios → Orchestrator classifica `data` ou `hybrid`
2. Preencher `context/semantic-layer/` com conceitos Otus/Irisys reais
3. Usar templates em `templates/data/` para pedidos estruturados
4. MCP SQL (ex.: user-mssql) quando disponível no projeto — após esgotar consulta enviada

## Demandas híbridas (típicas Umbra/Irisys)

- Relatório no portal + API + procedure
- Task ClickUp alterando indicador
- Suporte reportando divergência

O agente monta Hybrid Flow automaticamente — usuário não escolhe skills.

## Precedência

1. Instruções do usuário
2. `AGENTS.md` do projeto (ex.: Umbra `AGENTS.md`)
3. Framework `AGENTS.md`
4. Orchestrator

## Resposta

- Dev geral: `templates/final-response.md`
- Dados/BI: `templates/data/final-response-data.md`
- Híbrido: combinar ambos conforme Orchestrator
