from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
import numpy as np
from app.database import get_db
from app.models import Company
from app.schemas import MatchResult
from app.core.scoring import similarity_to, strategic_fit
from app.core.synergy import synergy_estimate

router = APIRouter()

@router.get("/{acquirer_id}", response_model=List[MatchResult])
def match(acquirer_id: int, top: int = Query(10, le=50),
          db: Session = Depends(get_db)):
    acquirer = db.query(Company).get(acquirer_id)
    if not acquirer:
        raise HTTPException(404, "Acquirer not found")
    others = db.query(Company).filter(Company.id != acquirer_id).all()
    if not others:
        return []
    sims = similarity_to(acquirer, others)
    results = []
    for c, s in zip(others, sims):
        fit = strategic_fit(acquirer, c)
        syn = synergy_estimate(acquirer, c)
        combined = acquirer.valuation_m + c.valuation_m + syn
        score = fit * 0.5 + s * 20 + syn / 100
        results.append(MatchResult(
            candidate_id=c.id, candidate_name=c.name,
            strategic_fit=fit, similarity=float(s),
            synergy_m=syn, combined_value_m=combined,
            final_score=float(score)))
    results.sort(key=lambda r: r.final_score, reverse=True)
    return results[:top]
