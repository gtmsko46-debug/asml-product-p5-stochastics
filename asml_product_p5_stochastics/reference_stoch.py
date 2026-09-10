"""SEED stochastics from stochastics-resist-v1 — watts vs pulse arrival."""
from __future__ import annotations
import math

LCDU = 1.2
DOSE_TO_SIZE = 30.0
ACID_DIFF = 8.0


def risk(row: dict) -> dict:
    dose = float(row.get("dose_mj_cm2", DOSE_TO_SIZE))
    pulse_rate = float(row.get("pulse_rate_mhz", 100.0))
    photons_per_pulse = float(row.get("photons_per_pulse", 1e12))
    blur = float(row.get("resist_blur_nm", ACID_DIFF))
    # shot-noise-ish: more dose helps; pulse structure modulates effective photons
    effective = dose * (0.7 + 0.3 * math.tanh(pulse_rate / 50.0)) * (photons_per_pulse / 1e12) ** 0.25
    lcdu = LCDU * math.sqrt(DOSE_TO_SIZE / max(effective, 1e-6)) * (1.0 + 0.02 * blur)
    defect_proxy = max(0.0, lcdu - 0.8) / 2.0
    return {
        "lcdu_nm_3sigma": float(lcdu),
        "defect_risk_proxy": float(defect_proxy),
        "effective_dose_proxy": float(effective),
        "assumption_card_id": "stochastics-resist-v1",
        "note": "More watts help only if arrival statistics cooperate — synthetic.",
    }
