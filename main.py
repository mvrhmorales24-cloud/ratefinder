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

# 💼 salarios base globales (USD/mes, rangos reales tech global)
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

# 📊 experiencia laboral estándar global
LEVEL = {
    "junior": 0.6,
    "mid": 1.0,
    "senior": 1.7
}

# 🌍 factor país (PPP simplificado realista basado en mercado laboral)
COUNTRY = {
    "US": 1.00,
    "CA": 0.86,
    "UK": 0.78,
    "DE": 0.72,
    "FR": 0.70,
    "ES": 0.65,
    "EU": 0.72,
    "CL": 0.28,
    "MX": 0.25,
    "AR": 0.20,
    "BR": 0.30,
    "CO": 0.24,
    "PE": 0.23
}

@app.get("/rate")
def rate(job: str, level: str, country: str):

    job = job.lower().strip()
    level = level.lower().strip()
    country = country.upper().strip()

    base = BASE.get(job, 4000)
    lvl = LEVEL.get(level, 1.0)
    ctry = COUNTRY.get(country, 0.5)

    min_salary = base * lvl * ctry
    max_salary = base * lvl * 1.25 * ctry

    return {
        "job": job,
        "level": level,
        "country": country,
        "currency": "USD",
        "min": round(min_salary),
        "max": round(max_salary)
    }