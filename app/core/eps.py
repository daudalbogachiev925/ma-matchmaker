from app.models import Company
from app.core.synergy import synergy_estimate

TAX_RATE = 0.30
SHARE_PRICE = 100.0

def eps_acquirer(company: Company) -> float:
    net_income = company.ebitda_m * (1 - TAX_RATE)
    return net_income * 1e6 / company.shares_outstanding

def eps_after_deal(acquirer: Company, target: Company,
                   premium: float = 0.25, cash_ratio: float = 0.5) -> dict:
    deal_price = target.valuation_m * (1 + premium)
    synergy = synergy_estimate(acquirer, target)

    combined_ebitda = acquirer.ebitda_m + target.ebitda_m + synergy
    combined_ni = combined_ebitda * (1 - TAX_RATE)

    new_shares = deal_price * (1 - cash_ratio) * 1e6 / SHARE_PRICE
    total_shares = acquirer.shares_outstanding + new_shares

    eps_before = eps_acquirer(acquirer)
    eps_after = combined_ni * 1e6 / total_shares

    return {
        "deal_price_m": deal_price,
        "cash_m": deal_price * cash_ratio,
        "shares_m": new_shares,
        "eps_acquirer": eps_before,
        "eps_combined": eps_after,
        "accretive": eps_after > eps_before,
        "combined_ebitda": combined_ebitda,
    }
