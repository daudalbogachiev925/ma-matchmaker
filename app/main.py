from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.api import companies, matching, simulation

Base.metadata.create_all(bind=engine)

app = FastAPI(title="M&A Matchmaker", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])

app.include_router(companies.router, prefix="/api/companies", tags=["companies"])
app.include_router(matching.router, prefix="/api/matching", tags=["matching"])
app.include_router(simulation.router, prefix="/api/simulation", tags=["simulation"])

@app.get("/health")
def health():
    return {"status": "ok"}
