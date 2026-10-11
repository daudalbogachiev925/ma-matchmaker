from typing import List
from app.models import Company
from app.core.scoring import strategic_fit
from app.core.synergy import synergy_estimate

def build_report(acquirer: Company, target: Company) -> str:
    fit = strategic_fit(acquirer, target)
    syn = synergy_estimate(acquirer, target)
    return f"""
РЕКОМЕНДАЦИЯ ПО M&A

Акквирер: {acquirer.name} ({acquirer.industry}, {acquirer.geography})
Цель: {target.name} ({target.industry}, {target.geography})
Оценка цели: {target.valuation_m:.0f}M
Strategic fit: {fit}/100
Ожидаемые синергии: {syn:.1f}M
Комбинированная стоимость: {acquirer.valuation_m + target.valuation_m + syn:.1f}M

Обоснование:
- Расширение в регион {target.geography}
- Дополнение по технологиям (tech {target.tech_score:.0f} vs {acquirer.tech_score:.0f})
- Синергии: {syn:.1f}M
"""
