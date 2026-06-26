# Exemplo: Capability Mission — RAG

**Pedido:** "Quais Capabilities estão prontas?"

**Modo:** Fast

**Pipeline:** Orchestrator → capability-manager → CAPABILITY_REGISTRY

**Resposta:** RAG Intelligence (Ready v1.0.0); demais Planned.

---

**Pedido:** "Como implementar assistente FAQ?" (framework-only)

**Modo:** Standard

**Pipeline:** capability-resolver → rag-orchestrator → rag-architect → knowledge-architect

**Nota:** Plano de arquitetura — **sem código em Umbra/Irisys/SmartRifa**.
