# Team Telemetry

> Como usar o AI Engineering Framework com um time inteiro e consolidar relatorios de uso/economia.

## Objetivo

Permitir que cada pessoa use o framework localmente e publique metadados curtos para um repositorio central da Otus7. O relatorio consolidado mostra uso por projeto/time, economia operacional estimada, retries evitados, erros evitados, skills mais usadas e quando uma promotion review esta vencida.

## Repositorios

Use dois repositorios separados:

```text
ai-engineering-framework/
  rules/
  skills/
  templates/
  tools/collect_execution_metrics.py

ai-framework-telemetry/
  projects/
  team/
```

O primeiro e o framework. O segundo guarda apenas telemetria operacional.

## Criar o repo de telemetria

No Git da Otus7, crie um repositorio como:

```text
Otus7/ai-framework-telemetry
```

Clone ao lado do framework:

```powershell
git clone https://github.com/Otus7/ai-framework-telemetry.git ..\ai-framework-telemetry
```

## Publicar uso local

Depois de uma missao relevante:

```powershell
python tools/collect_execution_metrics.py `
  --project umbra `
  --team Otus7 `
  --telemetry-root ..\ai-framework-telemetry `
  --publish
```

Troque `umbra` por `irisys`, `rifsmart` ou outro projeto.

## O que o comando gera

No framework local:

```text
framework/operating-system/reports/USAGE_REPORT.md
framework/operating-system/reports/USAGE_REPORT.json
```

No repo de telemetria:

```text
projects/{project}/contributors/{user-hash}/...
projects/{project}/reports/USAGE_REPORT.md
team/reports/USAGE_REPORT.md
```

Por padrao, o usuario e anonimizado como `user-<hash>`.

## Relatorios disponiveis

- Missoes registradas.
- Missoes concluidas.
- Entradas estruturadas de execucao.
- Baseline units.
- Actual units.
- Economia operacional estimada.
- Retries avoided.
- Errors avoided.
- Uso por modo.
- Uso por superficie.
- Modelos recomendados.
- Skills usadas.
- Waste signals.
- Savings signals.
- Promotion review due.

## Seguranca

Nao publique:

- prompts completos;
- secrets;
- tokens;
- connection strings;
- logs completos;
- dados de cliente;
- codigo longo.

O repo central deve ser tratado como dado operacional interno da Otus7.

## Workflow recomendado

1. Cada pessoa roda o framework normalmente.
2. Ao final de uma missao relevante, roda o coletor com `--publish`.
3. Faz commit/push no repo `ai-framework-telemetry`.
4. Um responsavel revisa o relatorio do time.
5. A cada 10 missoes reais, roda promotion review.

## Exemplo de rotina

```powershell
cd C:\Users\Douglas\Documents\ai-engineering-framework
python tools/collect_execution_metrics.py --project umbra --team Otus7 --telemetry-root ..\ai-framework-telemetry --publish

cd ..\ai-framework-telemetry
git status
git add .
git commit -m "chore: update ai framework telemetry"
git push
```

## Limite importante

A economia ainda e estimada por unidades operacionais. Nao converter para tokens reais ou custo financeiro sem telemetria confiavel de modelo/input/output/cache.
