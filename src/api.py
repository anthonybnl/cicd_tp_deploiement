"""
Lancement en mode DEV : uvicorn src.api:app --reload-dir api --reload --port 3000
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="OnMangeQuoi API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok", "message": "l'api fonctionne correctement"}
