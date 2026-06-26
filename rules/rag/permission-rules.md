# Permission Rules — RAG

- Retrieval filtra por tenant/user/role **no query**, não pós-processamento apenas.
- Nunca retornar chunk de documento sem permissão explícita.
- Audit log de acessos negados (em implementação futura).
