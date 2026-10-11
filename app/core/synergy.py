from app.models import Company

def synergy_estimate(acquirer: Company, target: Company) -> float:
    revenue_synergy = min(acquirer.revenue_m, target.revenue_m) * 0.10
    cost_synergy = (acquirer.ebitda_m + target.ebitda_m) * 0.05
    return revenue_synergy + cost_synergy
