from app.models import Company
from app.core.scoring import strategic_fit

def make(name, geo, ind, rev=100, growth=0.1, tech=50, share=0.1,
         val=500, ebitda=0.2):
    return Company(id=1, name=name, revenue_m=rev, ebitda_margin=ebitda,
                   growth_yoy=growth, market_share=share, tech_score=tech,
                   geography=geo, industry=ind, valuation_m=val)

def test_geo_bonus():
    a = make("A", "RU", "Fintech")
    b = make("B", "EU", "Fintech")
    assert strategic_fit(a, b) >= 20

def test_growth_bonus():
    a = make("A", "RU", "Fintech", growth=0.05)
    b = make("B", "RU", "Fintech", growth=0.3)
    assert strategic_fit(a, b) >= 20
