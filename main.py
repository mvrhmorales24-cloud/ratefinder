from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir frontend (Netlify)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/rate")
def get_rate(job: str, level: str, country: str):

    job = job.lower()
    level = level.lower()
    country = country.upper()

    try:
        min_sal, max_sal = SALARIES[country][job][level]
    except KeyError:
        min_sal, max_sal = (1000, 2000)

    return {
        "job": job,
        "level": level,
        "country": country,
        "min": min_sal,
        "max": max_sal
    }