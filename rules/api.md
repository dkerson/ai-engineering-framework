# API

> Finalidade: Design de APIs REST consistente.

## Regras

- Recursos pluralizados: /orders não /order
- HTTP verbs corretos: GET read, POST create, PUT/PATCH update, DELETE remove
- Status codes semânticos: 201 created, 404 not found, 422 validation
- Paginação em listagens: page, pageSize ou cursor
- Versionamento quando breaking change
