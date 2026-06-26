# Token Economy — Regras Obrigatórias

> Finalidade: minimizar consumo de tokens sem sacrificar qualidade. Aplicável a **todas** as skills e execuções.

Complemento obrigatório: `rules/hierarchical-orchestration.md`

## Regras absolutas

Skills **nunca** devem:

- Ler o projeto inteiro
- Repetir contexto já no Working Context
- Responder com textos longos (Council: máx. 150 palavras/skill)
- Abrir arquivos sem necessidade
- Executar validações desnecessárias
- Auto-iniciar — somente via Orchestrator

O Orchestrator reutiliza contexto já obtido. Se uma skill analisou um arquivo, outra **deve** reutilizar essa análise.

## Modo mínimo

O Orchestrator escolhe o **menor modo seguro**:

```
Fast → Standard → Review → Technical Council
```

Não escalar modo sem justificativa de risco.

## Investigação dirigida

**SEMPRE** localizar antes de ler em massa:

1. Mensagem de erro / stack trace
2. Arquivo e linha indicados
3. Função, componente ou endpoint envolvido
4. Working Context — arquivos já analisados

**NUNCA** percorrer todo o projeto "para entender contexto".

## Leitura de arquivos

| Fazer | Não fazer |
|-------|-----------|
| Ler arquivo do erro + imports diretos | Abrir dezenas de arquivos por precaução |
| Usar grep/search para achar símbolos | Listar diretórios inteiros |
| Reutilizar análise do Working Context | Reler arquivo já catalogado |
| Ler testes do módulo alterado | Ler toda a suíte de testes |

## Contexto na conversa

- Resumir descobertas em 2–5 bullets no Working Context
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
