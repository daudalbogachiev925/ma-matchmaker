def test_health(client):
    assert client.get("/health").json()["status"] == "ok"

def test_create_company(client):
    payload = {
        "name": "Acme", "revenue_m": 1000, "ebitda_margin": 0.25,
        "growth_yoy": 0.15, "market_share": 0.1, "tech_score": 70,
        "geography": "RU", "industry": "Fintech", "valuation_m": 5000,
        "shares_outstanding": 100_000_000,
    }
    r = client.post("/api/companies", json=payload)
    assert r.status_code == 201
    assert r.json()["name"] == "Acme"
