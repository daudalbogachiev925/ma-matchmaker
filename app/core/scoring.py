import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from typing import List
from app.models import Company

FEATURES = ["revenue_m", "ebitda_margin", "growth_yoy",
            "market_share", "tech_score", "valuation_m"]

def _vectorize(companies: List[Company]):
    X = np.array([[getattr(c, f) for f in FEATURES] for c in companies])
    return StandardScaler().fit_transform(X)

def similarity_to(acquirer: Company, others: List[Company]) -> np.ndarray:
    all_c = [acquirer] + others
    X = _vectorize(all_c)
    sim = cosine_similarity(X[0:1], X)[0]
    return sim[1:]

def strategic_fit(acquirer: Company, target: Company) -> int:
    score = 0
    if target.geography != acquirer.geography:
        score += 20
    if target.tech_score > acquirer.tech_score:
        score += 15
    if target.growth_yoy > acquirer.growth_yoy:
        score += 20
    if 0.1 < target.revenue_m / acquirer.revenue_m < 1.0:
        score += 25
    if target.ebitda_margin > 0.15:
        score += 10
    if target.industry == acquirer.industry:
        score += 10
    return score
