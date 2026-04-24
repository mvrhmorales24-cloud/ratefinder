from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS para Netlify
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# MONEDAS
# -----------------------------
CURRENCY = {
    "CL": "CLP",
    "US": "USD",
    "CA": "CAD",
    "UK": "GBP"
}

# -----------------------------
# SALARIOS REALISTAS (BASE)
# -----------------------------
SALARIES = {
    "CL": {
        "developer": {"junior": (1000000, 1500000), "mid": (1500000, 2500000), "senior": (2500000, 4000000)},
        "design": {"junior": (800000, 1200000), "senior": (2000000, 3000000)},
        "vet": {"junior": (900000, 1400000), "senior": (2000000, 3500000)},
    },
    "US": {
        "developer": {"junior": (45000, 70000), "mid": (70000, 110000), "senior": (120000, 180000)},
        "design": {"junior": (40000, 60000), "senior": (100000, 150000)},
        "vet": {"junior": (60000, 85000), "senior": (90000, 140000)},
    },
    "CA": {
        "developer": {"junior": (50000, 75000), "mid": (75000, 110000), "senior": (110000, 160000)},
        "design": {"junior": (45000, 65000), "senior": (90000, 130000)},
        "vet": {"junior": (65000, 90000), "senior": (100000, 150000)},
    },
    "UK": {
        "developer": {"junior": (30000, 45000), "mid": (45000, 70000), "senior": (80000, 120000)},
        "design": {"junior": (28000, 40000), "senior": (70000, 110000)},
        "vet": {"junior": (35000, 50000), "senior": (70000, 100000)},
    }
}

# -----------------------------
# NORMALIZACIÓN
# -----------------------------
def normalize_job(job: str):
    job = job.lower().strip()
    if job in ["dev", "developer", "software engineer", "programmer"]:
        return "developer"
    if job in ["design", "designer", "ux", "ui"]:
        return "design"
    if job in ["vet", "veterinarian", "veterinary"]:
        return "vet"
    return job

def normalize_level(level: str):
    level = level.lower().strip()
    if level in ["jr", "junior", "entry"]:
        return "junior"
    if level in ["mid", "intermediate"]:
        return "mid"
    if level in ["sr", "senior", "lead"]:
        return "senior"
    return level

# -----------------------------
# ENDPOINT
# -----------------------------
@app.get("/rate")
def get_rate(job: str, level: str, country: str):

    job = normalize_job(job)
    level = normalize_level(level)
    country = country.upper().strip()

    try:
        min_sal, max_sal = SALARIES[country][job][level]

        return {
            "job": job,
            "level": level,
            "country": country,
            "currency": CURRENCY.get(country, country),
            "min": min_sal,
            "max": max_sal
        }

    except KeyError:
        return {
            "job": job,
            "level": level,
            "country": country,
            "currency": CURRENCY.get(country, country),
            "min": 0,
            "max": 0,
            "note": "No data available"
        }