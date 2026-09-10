from __future__ import annotations
import importlib.util, os, sys
from pathlib import Path
from types import ModuleType
from typing import Callable
from . import reference_stoch

RiskFn = Callable[[dict], dict]
_CACHED: tuple[str, RiskFn] | None = None

def _load(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location("asml_p5_stoch_sandbox", path)
    if spec is None or spec.loader is None:
        raise ImportError(str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules["asml_p5_stoch_sandbox"] = mod
    spec.loader.exec_module(mod)
    return mod

def get_risk(*, force_reload: bool = False) -> tuple[str, RiskFn]:
    global _CACHED
    if _CACHED is not None and not force_reload:
        return _CACHED
    explicit = os.environ.get("ASML_P5_SOLVER_PATH")
    if explicit:
        p = Path(explicit).expanduser().resolve()
        if p.is_dir():
            p = p / "solver.py"
        if p.is_file():
            mod = _load(p)
            fn = getattr(mod, "risk", None) or getattr(mod, "solve", None)
            if fn is None:
                raise AttributeError(str(p))
            _CACHED = (str(p), fn)
            return _CACHED
    bench = os.environ.get("ASML_BENCH_ROOT")
    if bench:
        p = Path(bench).expanduser().resolve() / "labs" / "p5-stochastics" / "solver.py"
        if p.is_file():
            mod = _load(p)
            fn = getattr(mod, "risk", None) or getattr(mod, "solve", None)
            if fn is None:
                raise AttributeError(str(p))
            _CACHED = (str(p), fn)
            return _CACHED
    _CACHED = ("reference", reference_stoch.risk)
    return _CACHED

def reset_loader_cache() -> None:
    global _CACHED
    _CACHED = None
