from fastapi import FastAPI

app = FastAPI()

@app.get("/rate")
def get_rate(job: str = "dev", level: str = "junior", country: str = "CL"):

    job = job.lower().strip()
    level = level.lower().strip()

    base_salaries = {
        "dev": 2500,
        "developer": 2500,
        "designer": 1800,
        "ux": 2000,
        "vet": 2200,
        "veterinarian": 2200
    }

    level_multipliers = {
        "junior": 1.0,
        "mid": 1.5,
        "senior": 2.2
    }

    # fallback seguro
    base = base_salaries.get(job, 1500)
    multiplier = level_multipliers.get(level, 1.0)

    min_salary = int(base * multiplier)
    max_salary = int(base * multiplier * 1.3)

    return {
        "job": job,
        "level": level,
        "country": country.upper(),
        "min": min_salary,
        "max": max_salary
    }