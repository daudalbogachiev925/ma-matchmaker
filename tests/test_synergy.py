from app.models import Company
from app.core.synergy import synergy_estimate

def test_synergy_positive():
    a = Company(id=1, name="A", revenue_m=100, ebitda_margin=0.2,
                geography="RU", industry="X", valuation_m=500)
    b = Company(id=2, name="B", revenue_m=80, ebitda_margin=0.15,
                geography="EU", industry="X", valuation_m=400)
    syn = synergy_estimate(a, b)
    assert syn > 0
    # 10% min(100,80)=8 + 5%(20+12)=1.6 => ~9.6
    assert abs(syn - 9.6) < 0.5
