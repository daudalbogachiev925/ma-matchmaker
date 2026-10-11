from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Company
from app.schemas import CompanyCreate, CompanyRead

router = APIRouter()

@router.post("", response_model=CompanyRead, status_code=201)
def create(payload: CompanyCreate, db: Session = Depends(get_db)):
    if db.query(Company).filter(Company.name == payload.name).first():
        raise HTTPException(409, "Name exists")
    c = Company(**payload.model_dump())
    db.add(c)
    db.commit()
    db.refresh(c)
    return CompanyRead(**payload.model_dump(), id=c.id, ebitda_m=c.ebitda_m)

@router.get("", response_model=List[CompanyRead])
def list_all(db: Session = Depends(get_db)):
    rows = db.query(Company).all()
    return [CompanyRead(**{k: getattr(r, k) for k in
                           ["name","revenue_m","ebitda_margin","growth_yoy",
                            "market_share","tech_score","geography","industry",
                            "valuation_m","shares_outstanding"]},
                        id=r.id, ebitda_m=r.ebitda_m) for r in rows]

@router.get("/{company_id}", response_model=CompanyRead)
def get_one(company_id: int, db: Session = Depends(get_db)):
    c = db.query(Company).get(company_id)
    if not c:
        raise HTTPException(404)
    return CompanyRead(**{k: getattr(c, k) for k in
                          ["name","revenue_m","ebitda_margin","growth_yoy",
                           "market_share","tech_score","geography","industry",
                           "valuation_m","shares_outstanding"]},
                       id=c.id, ebitda_m=c.ebitda_m)
