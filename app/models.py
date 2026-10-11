from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False, index=True)
    revenue_m = Column(Float, nullable=False)
    ebitda_margin = Column(Float, nullable=False)
    growth_yoy = Column(Float, default=0.0)
    market_share = Column(Float, default=0.0)
    tech_score = Column(Float, default=0.0)
    geography = Column(String, index=True)
    industry = Column(String, index=True)
    valuation_m = Column(Float, nullable=False)
    shares_outstanding = Column(Float, default=100_000_000)

    @property
    def ebitda_m(self):
        return self.revenue_m * self.ebitda_margin
