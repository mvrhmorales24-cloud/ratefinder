from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("rates.json", "r", encoding="utf-8-sig") as f:
    data = json.load(f)

@app.get("/rate")
def get_rate(job: str, level: str, country: str):
    item = data[job][level][country]

    return {
        "job": job,
        "level": level,
        "country": country,
        "min": item["min"],
        "max": item["max"],
        "range": f"{item['min']} - {item['max']}",
        "source": item["source"]
    }