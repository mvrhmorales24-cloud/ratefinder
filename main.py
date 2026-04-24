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

# 💼 salarios base reales (USD global estimado)
BASE_SALARIES = {
    "dev": 5500,
    "developer": 5500,
    "software engineer": 6500,
    "designer": 3500,
    "ux": 4200,
    "vet": 5000,
    "veterinarian": 5000,
    "data analyst": 4500,
    "marketing": 3800
}

# 📊 niveles reales de mercado
LEVELS = {
    "junior": 0.6,
    "mid": 1.0,
    "senior": 1.8
}

# 🌍 monedas reales simplificadas
CURRENCY = {
    "US": 1,
    "CL": 950,
    "CA": 1.35,
    "MX": 17,
    "UK": 0.79,
    "EU": 0.92
}

@app.get("/rate")
def get_rate(job: str = "dev", level: str = "junior", country: str = "US"):

    job = job.lower().strip()
    level = level.lower().strip()
    country = country.upper().strip()

    base = BASE_SALARIES.get(job, 4500)
    mult = LEVELS.get(level, 1.0)
    currency = CURRENCY.get(country, 1)

    # 💰 USD realista
    min_usd = base * mult
    max_usd = base * mult * 1.25

    return {
        "job": job,
        "level": level,
        "country": country,
        "currency": currency,
        "min_usd": round(min_usd),
        "max_usd": round(max_usd)
    }