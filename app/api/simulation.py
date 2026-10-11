from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Company
from app.schemas import DealRequest, DealResult
from app.core.eps import eps_after_deal

router = APIRouter()

@router.post("/deal", response_model=DealResult)
def simulate(req: DealRequest, db: Session = Depends(get_db)):
    a = db.query(Company).get(req.acquirer_id)
    t = db.query(Company).get(req.target_id)
    if not a or not t:
        raise HTTPException(404, "Company not found")
    if a.id == t.id:
        raise HTTPException(400, "Same company")
    r = eps_after_deal(a, t, premium=req.premium, cash_ratio=req.cash_ratio)
    return DealResult(
        acquirer=a.name, target=t.name,
        deal_price_m=r["deal_price_m"],
        cash_m=r["cash_m"], shares_m=r["shares_m"],
        combined_valuation_m=a.valuation_m + t.valuation_m,
        eps_acquirer=r["eps_acquirer"],
        eps_combined=r["eps_combined"],
        accretive=r["accretive"])
