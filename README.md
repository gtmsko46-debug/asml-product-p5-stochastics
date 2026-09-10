# asml-product-p5-stochastics

**Stochastic defect vs dose / FEL pulse structure — do more watts help or is arrival statistics the lever?**

| | |
|--|--|
| Spec | [`SPEC.md`](SPEC.md) · asml-bench [#48](https://github.com/gtmsko46-debug/asml-bench/issues/48) |
| Factory | [FACTORY.md](https://github.com/gtmsko46-debug/asml-bench/blob/main/products/FACTORY.md) |
| Stage | **Spec (M0)** — package/build waits bay |

```bash
# after M1
pip install -e '.[dev]'
```

Sandbox hill-climbs live on asml-bench (`labs/p5-stochastics/solver.py`); set `ASML_BENCH_ROOT` to pick up live weights once the loader exists.
