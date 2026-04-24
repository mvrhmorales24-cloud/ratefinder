from fastapi import FastAPI

app = FastAPI()

@app.get("/rate")
def get_rate(job: str, level: str, country: str):

    job = job.lower()
    level = level.lower()

    # 💰 base salaries (ejemplo simple pero consistente)
    base_salaries = {
        "dev": 2500,
        "developer": 2500,
        "designer": 1800,
        "ux": 2000,
        "vet": 2200,
        "veterinarian": 2200
    }

    base = base_salaries.get(job, 1500)

    # 📊 level multiplier (FIX MID)
    multipliers = {
        "junior": 1.0,
        "mid": 1.5,
        "senior": 2.2
    }

    multiplier = multipliers.get(level, 1.0)

    min_salary = base * multiplier
    max_salary = base * multiplier * 1.3

    # 🌍 safe fallback country formatting
    country = country.upper() if country else "UNKNOWN"

    return {
        "job": job,
        "level": level,
        "country": country,
        "min": int(min_salary),
        "max": int(max_salary)
    }