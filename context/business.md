# Business Context — Umbra

> Contexto de negócio do portal Umbra (Otus7).

## Empresa / Produto

**Umbra** — portal interno da **Otus7** para colaboradores. Centraliza administração do portal, relatórios PMO (ClickUp) e base de conhecimento (Irisys/KB).

## Usuários

| Persona | Necessidade |
|---------|-------------|
| Colaborador Otus7 | Acessar KB, relatórios PMO, notificações |
| Admin portal | Gerir usuários, papéis, permissões, parâmetros, auditoria |
| PMO / gestão | Dashboards sprint ClickUp, referências, imports Excel |
| Editor KB | Manter artigos e menu da base de conhecimento |

## Modelo de acesso

- Login via **Microsoft Entra ID** (conta corporativa)
- **Pré-registro obrigatório** — admin cadastra e-mail antes do primeiro login
- Permissões granulares por módulo (`admin.*`, `pmo.*`, `kb.*`)
- System admin: permissão wildcard `portal.*`

## Módulos de negócio

### Admin
Gestão de identidades portal: usuários, papéis, permissões, logs de auditoria, parâmetros de sistema, notificações.

### PMO (ClickUp)
Importação de relatórios sprint (.xlsx), dashboards analíticos, tabelas de referência (status, prioridades, tiers de cliente).

### KB (Irisys)
Base de conhecimento com menu hierárquico, artigos HTML, geração assistida por IA (Cursor Cloud Agent).

## Glossário

| Termo | Definição |
|-------|-----------|
| Portal | Sistema Umbra — distinto de Entra ID |
| Pré-registro | Usuário cadastrado por e-mail antes do primeiro login Entra |
| Permissão | Código `perm:modulo.acao` (ex.: `kb.read`) |
| Papel (Role) | Agrupamento de permissões atribuível a usuários |
| PMO | Project Management Office — módulo ClickUp |
| KB | Knowledge Base — módulo Irisys |
| Sprint report | Relatório Excel importado do ClickUp |
| Artigo KB | Documento HTML armazenado em blob |

## Idioma

Textos de UI e mensagens ao usuário: **português do Brasil (pt-BR)**.

## Restrições para agentes

- Não commitar salvo pedido explícito
- Não alterar `appsettings*.json` sem preservar `ConnectionStrings` e `AzureAd`
- Não versionar segredos
