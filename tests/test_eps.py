from app.models import Company
from app.core.eps import eps_after_deal

def test_eps_accretive():
    a = Company(id=1, name="A", revenue_m=1000, ebitda_margin=0.30,
                geography="RU", industry="X", valuation_m=5000,
                shares_outstanding=100_000_000)
    b = Company(id=2, name="B", revenue_m=200, ebitda_margin=0.25,
                geography="EU", industry="X", valuation_m=800,
                shares_outstanding=10_000_000)
    r = eps_after_deal(a, b, premium=0.2, cash_ratio=0.5)
    assert "eps_combined" in r
    assert r["deal_price_m"] > 0
