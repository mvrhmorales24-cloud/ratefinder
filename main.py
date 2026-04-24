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

# 💼 base global USD (referencia internacional)
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

# 📊 nivel
LEVEL = {
    "junior": 0.6,
    "mid": 1.0,
    "senior": 1.7
}

# 🌍 AJUSTE REAL POR PAÍS (multiplicador de mercado)
# basado en poder adquisitivo + salarios tech promedio
COUNTRY_FACTOR = {
    "US": 1.0,
    "CA": 0.85,
    "UK": 0.75,
    "EU": 0.7,
    "CL": 0.25,
    "MX": 0.22,
    "AR": 0.18
}

@app.get("/rate")
def rate(job: str = "dev", level: str = "junior", country: str = "US"):

    job = job.lower().strip()
    level = level.lower().strip()
    country = country.upper().strip()

    base = BASE.get(job, 4000)
    mult = LEVEL.get(level, 1.0)
    country_mult = COUNTRY_FACTOR.get(country, 0.5)

    # 💡 fórmula realista de mercado
    min_salary = base * mult * country_mult
    max_salary = base * mult * 1.25 * country_mult

    return {
        "job": job,
        "level": level,
        "country": country,
        "min": round(min_salary),
        "max": round(max_salary)
    }