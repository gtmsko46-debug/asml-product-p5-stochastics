from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Any, Mapping
from .loader import get_risk

ASSUMPTION_CARD = "stochastics-resist-v1"

@dataclass
class StochReport:
    lcdu_nm_3sigma: float
    defect_risk_proxy: float
    effective_dose_proxy: float
    assumption_card_id: str = ASSUMPTION_CARD
    note: str = "Synthetic pulse vs dose trade."
    solver_source: str = "reference"
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def stochastic_risk(row: Mapping[str, Any] | None = None) -> StochReport:
    source, fn = get_risk()
    out = fn(dict(row or {}))
    return StochReport(
        lcdu_nm_3sigma=float(out["lcdu_nm_3sigma"]),
        defect_risk_proxy=float(out["defect_risk_proxy"]),
        effective_dose_proxy=float(out["effective_dose_proxy"]),
        assumption_card_id=str(out.get("assumption_card_id", ASSUMPTION_CARD)),
        note=str(out.get("note", "Synthetic.")),
        solver_source=source,
    )
