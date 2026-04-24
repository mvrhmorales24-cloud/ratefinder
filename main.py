from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# -----------------------------
# CORS (frontend Netlify)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# BASE DE DATOS SIMPLIFICADA
# -----------------------------
SALARIES = {
    "CL": {
        "design": {
            "junior": (800000, 1200000),
            "mid": (1200000, 1800000),
            "senior": (1800000, 2500000),
        },
        "developer": {
            "junior": (1000000, 1500000),
            "mid": (1500000, 2200000),
            "senior": (2200000, 3500000),
        },
        "vet": {
            "junior": (900000, 1300000),
            "senior": (1500000, 2200000),
        }
    },
    "US": {
        "design": {
            "junior": (3000, 4500),
            "mid": (4500, 7000),
            "senior": (7000, 12000),
        },
        "developer": {
            "junior": (4000, 6000),
            "mid": (6000, 9000),
            "senior": (9000, 14000),
        },
        "vet": {
            "junior": (3500, 5000),
            "senior": (6000, 9000),
        }
    }
}

# -----------------------------
# NORMALIZACIÓN INTELIGENTE
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
# ENDPOINT PRINCIPAL
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
            "min": min_sal,
            "max": max_sal
        }

    except KeyError:
        return {
            "job": job,
            "level": level,
            "country": country,
            "min": 1000,
            "max": 2000,
            "note": "No exact match, showing fallback estimate"
        }