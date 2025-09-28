from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from decision import decision_engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/battery/status")
def battery_status():
    df = pd.read_excel("dummy.xlsx")
    last = df.iloc[-1]
    return {
        "SOC": float(last["SOC"]),
        "Voltage": float(last["Voltage"]),
        "Current": float(last["Current"]),
        "Load": float(last["Load"]),
        "PV": float(last["PV"])
    }

@app.get("/battery/logs")
def battery_logs():
    df = pd.read_excel("dummy.xlsx")
    return df.to_dict(orient="records")

@app.get("/battery/recommendations")
def battery_recommendations():
    df = pd.read_excel("dummy.xlsx")
    return decision_engine(df)
