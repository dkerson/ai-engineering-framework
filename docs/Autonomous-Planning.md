# Autonomous Planning

> Política NLME — o framework decide skills, plugins, capabilities e workflows sem input técnico do usuário.

## Princípio

O usuário descreve **objetivo de negócio**. O framework seleciona automaticamente:

- Mission Type
- Workflows
- Skills (pipeline mínimo)
- Capabilities (COS)
- Plugins (quando infra/MCP)
- Modo operacional (Fast/Standard/Review/Council)
- Validações

## Algoritmo

```text
1. Mission Type (Mission Catalog)
2. Workflows mapeados (_index.md)
3. Domínios envolvidos
4. capability-resolver → capabilities COS
5. plugin-resolver → se integração externa
6. project-resolver → registry + overlay
7. Montar skills_pipeline (máx. necessário, token economy)
8. Escalonar modo operacional por risco
```

## O usuário nunca precisa dizer

- Nomes de skills
- Workflows
- Plugins ou MCPs
- Modo Fast/Standard/Review/Council
- Domínios técnicos

## Exceções — perguntar (mínimo)

| Gap | Pergunta permitida |
|-----|-------------------|
| Projeto desconhecido | "Qual produto: Umbra, Irisys ou outro?" |
| Ambiente produção vs dev | "É produção ou ambiente de teste?" |
| Escopo implementação vs só análise | Só se frase contraditória |

Máximo **3 perguntas** por missão. Nunca interrogatório.

## Responsável

`mission-builder` + `capability-resolver` + Orchestrator.

## Referências

- `docs/Mission-Confidence.md`
- `rules/token-economy.md`
- `skills/mission-builder/SKILL.md`
