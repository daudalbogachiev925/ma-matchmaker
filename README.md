# ma-matchmaker
Описание: платформа поиска M&amp;A-кандидатов. Скоринг, синергии, симуляция сделки, EPS-аккреция, отчёт для совета директоров.  Стек: Python, FastAPI, PostgreSQL, scikit-learn, Streamlit, Docker.

# ma-matchmaker

Платформа поиска M&A-кандидатов с оценкой синергий и EPS-аккреции.

## Возможности
- База компаний (revenue, EBITDA, geography, industry)
- Скоринг strategic fit
- Cosine similarity по ML-фичам
- Оценка синергий
- Симуляция сделки: премия, cash/shares, EPS-accretion
- Генерация отчёта для совета директоров
- Streamlit-дашборд

## Быстрый старт

cp .env.example .env
docker-compose up --build

API: http://localhost:8000/docs
Dashboard: http://localhost:8501

## Пример

curl -X POST http://localhost:8000/api/companies \
  -H "Content-Type: application/json" \
  -d '{"name":"Acme","revenue_m":1000,"ebitda_margin":0.25,"growth_yoy":0.15,
       "market_share":0.1,"tech_score":70,"geography":"RU","industry":"Fintech",
       "valuation_m":5000,"shares_outstanding":100000000}'

curl http://localhost:8000/api/matching/1

## Тесты

pytest tests/ -v

## Лицензия
MIT
