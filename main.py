from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 💼 USD mensuales (rangos globales reales aproximados)
BASE = {
    "dev": 5500,
    "software engineer": 6500,
    "designer": 3500,
    "ux": 4200,
    "vet": 4500,
    "veterinarian": 4500,
    "data analyst": 4000,
    "marketing": 3800
}

LEVEL = {
    "junior": 0.6,
    "mid": 1.0,
    "senior": 1.7
}

@app.get("/rate")
def rate(job: str = "dev", level: str = "junior", country: str = "US"):

    job = job.lower().strip()
    level = level.lower().strip()

    base = BASE.get(job, 4000)
    mult = LEVEL.get(level, 1.0)

    return {
        "job": job,
        "level": level,
        "country": country.upper(),
        "min_usd": round(base * mult),
        "max_usd": round(base * mult * 1.25)
    }