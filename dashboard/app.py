import os
import requests
import pandas as pd
import streamlit as st
import plotly.express as px

API = os.getenv("API_URL", "http://api:8000")
st.set_page_config(page_title="M&A Matchmaker", layout="wide")
st.title("M&A Matchmaker")

@st.cache_data(ttl=30)
def fetch(path):
    return requests.get(f"{API}{path}").json()

companies = pd.DataFrame(fetch("/api/companies"))
if companies.empty:
    st.warning("Нет компаний")
    st.stop()

acquirer_id = st.sidebar.selectbox(
    "Акквирер", companies.id.tolist(),
    format_func=lambda i: companies[companies.id==i].name.iloc[0])
premium = st.sidebar.slider("Премия", 0.0, 1.0, 0.25)
cash_ratio = st.sidebar.slider("Доля cash", 0.0, 1.0, 0.5)

if st.sidebar.button("Найти кандидатов"):
    matches = pd.DataFrame(fetch(f"/api/matching/{acquirer_id}?top=10"))
    st.session_state["matches"] = matches

if "matches" in st.session_state:
    m = st.session_state["matches"]
    st.subheader("Топ кандидатов")
    st.plotly_chart(px.scatter(m, x="strategic_fit", y="synergy_m",
                                size="combined_value_m", text="candidate_name"))

    target_id = st.selectbox(
        "Симуляция сделки",
        m.candidate_id.tolist(),
        format_func=lambda i: m[m.candidate_id==i].candidate_name.iloc[0])

    if st.button("Симулировать"):
        deal = requests.post(f"{API}/api/simulation/deal", json={
            "acquirer_id": acquirer_id, "target_id": int(target_id),
            "premium": premium, "cash_ratio": cash_ratio,
        }).json()
        st.json(deal)
