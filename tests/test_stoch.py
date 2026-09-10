from asml_product_p5_stochastics import stochastic_risk
from asml_product_p5_stochastics.loader import reset_loader_cache
import pytest

@pytest.fixture(autouse=True)
def _e(monkeypatch):
    monkeypatch.delenv("ASML_BENCH_ROOT", raising=False)
    reset_loader_cache()

def test_smoke():
    r = stochastic_risk({})
    assert r.lcdu_nm_3sigma > 0
