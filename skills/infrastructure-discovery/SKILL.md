---
name: infrastructure-discovery
description: >-
  Discovers project infrastructure signals such as Git, Docker, Kubernetes, Terraform, runtimes, databases, cloud, monitoring, APIs and MCPs. Invoked only by the Orchestrator during Infrastructure Missions.
---

# Infrastructure Discovery

## Objetivo

Analisar um projeto e registrar sinais de infraestrutura sem alterar codigo.

## Detecta

Git, Docker, Compose, Kubernetes, Terraform, Helm, Node, Flutter, React, Nest, .NET, Java, Python, Redis, RabbitMQ, Kafka, Postgres, MySQL, SQL Server, Oracle, MongoDB, Elastic, Power BI, Supabase, Firebase, Azure, AWS, GCP, Sentry, Prometheus, Grafana, ClickUp, Jira, GitHub, GitLab, Bitbucket, Azure DevOps, OpenAPI, Swagger e similares.

## Regras

- Sempre registrar.
- Nunca alterar codigo.
- Nunca armazenar credenciais.
- Usar placeholders e env vars.

## Saidas

- Evidencias encontradas
- Lacunas
- Atualizacoes propostas para registry
- Riscos

## Referencias

- `docs/Infrastructure-Intelligence.md`
- `rules/infrastructure-secrets.md`
