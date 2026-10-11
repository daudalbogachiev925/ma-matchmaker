from pydantic import BaseModel, Field

class CompanyBase(BaseModel):
    name: str
    revenue_m: float = Field(gt=0)
    ebitda_margin: float = Field(ge=0, le=1)
    growth_yoy: float = 0.0
    market_share: float = 0.0
    tech_score: float = 0.0
    geography: str
    industry: str
    valuation_m: float = Field(gt=0)
    shares_outstanding: float = 100_000_000

class CompanyCreate(CompanyBase):
    pass

class CompanyRead(CompanyBase):
    id: int
    ebitda_m: float

    class Config:
        from_attributes = True

class MatchResult(BaseModel):
    candidate_id: int
    candidate_name: str
    strategic_fit: int
    similarity: float
    synergy_m: float
    combined_value_m: float
    final_score: float

class DealRequest(BaseModel):
    acquirer_id: int
    target_id: int
    premium: float = 0.25
    cash_ratio: float = 0.5

class DealResult(BaseModel):
    acquirer: str
    target: str
    deal_price_m: float
    cash_m: float
    shares_m: float
    combined_valuation_m: float
    eps_acquirer: float
    eps_combined: float
    accretive: bool
