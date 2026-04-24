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

# 💼 base USD mensual (mercado global realista)
BASE = {
    "dev": 5500,
    "software engineer": 6500,
    "designer": 3500,
    "ux": 4200,
    "vet": 4500,
    "veterinarian": 4500,
    "data analyst": 4000,
    "marketing": 3800,
    "product manager": 7000
}

# 📊 experiencia
LEVEL = {
    "junior": 0.6,
    "mid": 1.0,
    "senior": 1.7
}

# 🌍 PPP (ajuste realista por país)
COUNTRY = {
    "US": 1.00,
    "CA": 0.86,
    "UK": 0.78,
    "EU": 0.72,
    "DE": 0.72,
    "FR": 0.70,
    "ES": 0.65,
    "CL": 0.28,
    "MX": 0.25,
    "AR": 0.20,
    "BR": 0.30,
    "CO": 0.24,
    "PE": 0.23
}

# 💱 visual conversion (solo UI reference)
FX = {
    "USD": 1,
    "CLP": 900,
    "CAD": 1.35,
    "EUR": 0.92
}

@app.get("/rate")
def rate(job: str, level: str, country: str):

    job = job.lower().strip()
    level = level.lower().strip()
    country = country.upper().strip()

    base = BASE.get(job, 4000)
    lvl = LEVEL.get(level, 1.0)
    ctry = COUNTRY.get(country, 0.5)

    min_usd = base * lvl * ctry
    max_usd = base * lvl * 1.25 * ctry

    return {
        "job": job,
        "level": level,
        "country": country,
        "min_usd": round(min_usd),
        "max_usd": round(max_usd),
        "fx": FX
    }