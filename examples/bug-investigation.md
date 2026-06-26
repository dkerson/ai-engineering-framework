# Exemplo: Investigação de Bug

**Pedido:** "Umbra apresentou erro ao salvar pedido"

**Orchestrator:** tipo=bug

**Pipeline executado:**
1. context-builder → monorepo .NET+Angular
2. bug-hunter → NullRef OrderService:42
3. tech-lead → fix validation CustomerId
4. backend → patch 3 lines
5. qa → 2 unit tests pass
6. code-review → approved
7. release-notes → "Fixed: erro ao salvar pedido"
