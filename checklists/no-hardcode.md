# Checklist: No Hardcode

> Finalidade: revisar se uma mudanca introduz valores fixos que deveriam ser configuraveis.

- [ ] Nenhum secret, token, senha ou connection string no codigo
- [ ] URLs, hosts, portas e providers via env/config/registry
- [ ] IDs de cliente, tenant, usuario, empresa, perfil ou role nao fixos
- [ ] Status, modulos, menus e categorias via banco/config ou enum justificado
- [ ] Permissoes/scopes/roles definidos por policy/matriz, nao strings soltas sem fonte
- [ ] Numeros magicos convertidos para parametro, constante nomeada ou configuracao
- [ ] Seeds sao idempotentes e preservam customizacoes
- [ ] Defaults podem ser sobrescritos por banco/configuracao quando aplicavel
- [ ] Fallback seguro definido quando parametro/config estiver ausente
- [ ] Achados de scan classificados como real ou falso positivo
