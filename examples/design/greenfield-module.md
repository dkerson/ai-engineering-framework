# Exemplo — GREENFIELD: novo módulo

**Input:** "Criar módulo de onboarding independente no portal"

**Design Mode:** GREENFIELD

**Pipeline:**
```
product-designer → ux-researcher → ux-designer → ui-designer → design-system
→ benchmark-specialist → component-library → react → design-reviewer
→ product-aesthetic-director → accessibility → qa
```

**Design DNA:** `templates/design/design-dna.md` — sem DS prévio → `design-dna-default.md`

**Reuso:** componentes `shared/ui/` do Umbra quando aplicável

**Gate:** reprova se Responsividade < 8 → mobile-designer + nova revisão
