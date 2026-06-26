# RAG Intelligence — Security

## Regras

1. **Permission Aware Retrieval** — nunca retornar chunk de documento não autorizado.
2. **Prompt Injection** — `prompt-injection-reviewer` valida input antes do retrieval.
3. **Conversation Memory** — nunca persistir PII ou secrets na memória.
4. **Knowledge Governance** — versionamento obrigatório; audit trail em alterações.
5. **Confidence threshold** — não responder abaixo do limite configurado.

## Dados sensíveis

- Proibido indexar credenciais, tokens ou dados pessoais sem política explícita.
- Seguir `rules/rag/security.md` e `rules/infrastructure-secrets.md`.

## Ações que exigem Review/Council (em projetos futuros)

- Indexação de base com dados regulados (LGPD, HIPAA)
- Alteração de política de permissão em produção
- Reindex completo em ambiente produtivo

## Referências

- `rules/rag/security.md`
- `rules/rag/permission-rules.md`
- `checklists/rag/prompt-injection.md`
