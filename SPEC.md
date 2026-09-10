# asml-product-p5-stochastics — Product Spec (M0)

**Parent:** asml-bench [#48](https://github.com/gtmsko46-debug/asml-bench/issues/48)  
**Stage:** Spec → Build → Review → Ship  
**Rule:** Bots orchestrate; all *solver/sandbox* code via lasercode (Foreman→Operator). Docs/spec PRs OK offline.

## Champion job
Stochastic defect vs dose / FEL pulse structure — do more watts help or is arrival statistics the lever?

## Public API (target)
```python
from asml_product_p5_stochastics import stochastic_risk
report = stochastic_risk(dose=..., pulse_structure=..., resist=...)
```

## Lab bind
| Field | Value |
|-------|-------|
| Sandbox | `labs/p5-stochastics/solver.py` |
| Frozen eval | product stochastics eval; FEL-05 feed when KEEP |
| Assumption card | `stochastics-pulse-v1` |
| Dual-gate | dual-gate; starved list LIFTED — real Spec→Build |
| HOLDOUT | pin when EI freezes product holdout (no eval edits by solvers) |

## KEEP / promote bar
- Dual-provider KEEP on same frozen eval + digest
- Critic clear (no oracle / metric reuse)
- Repro Bot clean-tree PASS
- Diplomat dual stamp before product `reference_*` sync

## Must not
- Edit `eval.py` / `fixture/*` from solver tickets
- Ship single-provider KEEP as product baseline
- Claim fab-grounded numbers (synthetic cards only)

## Milestones
1. **M0 Spec** — this document + README champion job (this PR)
2. **M1 Package** — importable module + SEED `reference_*` + tests
3. **M2 Dual-gate** — HT pair via Foreman; Critic+Repro+Diplomat
4. **M3 Ship** — `reference_*` sync + ship-queue Issue close

## Bay
Queued behind P1 deepen / P2 HT-1023/1024 unless CoS assigns spare Operator. Spec/docs do not steal bay.
