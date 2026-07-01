# Team Telemetry

> Finalidade: consolidar uso do AI Engineering Framework por projeto, time e organizacao sem armazenar prompts, secrets ou codigo sensivel.

## Principio central

O framework e versionado em um repositorio. A telemetria de uso do time deve ficar em outro repositorio ou pasta central, para evitar conflitos, poluir historico do framework e misturar codigo com dados operacionais.

## Estrutura recomendada

```text
ai-framework-telemetry/
  projects/
    umbra/
      contributors/
        user-<hash>/
          MISSION_LEDGER.md
          EXECUTION_METRICS.md
          TOKEN_METRICS.md
          SKILL_USAGE.md
          EXECUTION_MEMORY_INDEX.md
          USAGE_REPORT.md
          USAGE_REPORT.json
      reports/
        USAGE_REPORT.md
        USAGE_REPORT.json
    irisys/
    rifsmart/
  team/
    reports/
      USAGE_REPORT.md
      USAGE_REPORT.json
```

## Politica de privacidade

Permitido:

- metadados curtos de missao;
- modo, superficie e modelo recomendado;
- baseline/actual units estimados;
- retries e erros evitados;
- skills usadas;
- sinais de desperdicio/economia;
- aprendizado reutilizavel sem dados privados.

Proibido:

- prompts completos;
- secrets, tokens, connection strings ou chaves;
- codigo longo;
- dados pessoais;
- conteudo de cliente;
- logs completos.

## Comando padrao

```powershell
python tools/collect_execution_metrics.py `
  --project umbra `
  --team Otus7 `
  --telemetry-root ..\ai-framework-telemetry `
  --publish
```

## Cadencia

- Rodar ao final de missoes executaveis relevantes.
- Rodar antes de relatorios de uso.
- Promotion review a cada 10 missoes reais, ou antes quando houver falha critica repetida.

## Governanca

- O script consolida e recomenda; nao altera comportamento do framework sozinho.
- Mudancas em rules, skills, workflows ou templates continuam exigindo aprovacao humana.
- O repositorio de telemetria deve ter revisao de PR como qualquer artefato operacional.
