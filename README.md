# Battery Admin Project

## Backend (FastAPI)
1. Go to `backend/`
2. Install deps: `pip install -r requirements.txt`
3. Run: `uvicorn main:app --reload`
4. API runs at: `http://localhost:8000`

## Frontend (React)
1. Go to `frontend/`
2. Run `npm install`
3. Run `npm start`
4. Opens at: `http://localhost:3000`

## Features
- API endpoints for `/battery/status`, `/battery/logs`, `/battery/recommendations`
- Frontend dashboard with status + recommendations
- Dummy Excel used as data source (replace with real Modbus later)
import os
import pandas as pd
import zipfile

# Create project structure
base_dir = "my-admin-project"
backend_dir = os.path.join(base_dir, "backend")
frontend_dir = os.path.join(base_dir, "frontend", "src")
os.makedirs(backend_dir, exist_ok=True)
os.makedirs(frontend_dir, exist_ok=True)

# ---------------- BACKEND FILES ----------------
# main.py
main_py = """from fastapi import FastAPI
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
"""

# decision.py
decision_py = """import pandas as pd

GENSET_MIN = 44   # kW mínimo operación
PV_CAPACITY = 65  # kWp
SOC_MIN = 20      # %
SOC_MAX = 90      # %

def decision_engine(df):
    last = df.iloc[-1]
    soc = last["SOC"]
    load = last["Load"]
    pv   = last["PV"]
    recs = []

    if soc < SOC_MIN:
        recs.append("🔴 SOC bajo → cargar batería (forzar carga con genset/PV).")
    elif soc > SOC_MAX:
        recs.append("🟢 SOC alto → limitar carga, priorizar consumo directo.")

    if pv > 0 and load < GENSET_MIN:
        recs.append("⚠️ Load bajo → posible curtail de FV para respetar mínimo del genset.")

    if load > GENSET_MIN and soc < 50:
        recs.append("✅ Mantener genset ON para sostener la carga.")

    if not recs:
        recs.append("🔵 Condiciones normales, sin acción inmediata.")

    return {"Time": str(last["Time"]), "SOC": soc, "Load": load, "PV": pv, "Recs": recs}
"""

# requirements.txt
requirements_txt = """fastapi
uvicorn
pandas
openpyxl
"""

# dummy.xlsx
dummy_data = pd.DataFrame({
    "Time":["12:00","13:00","14:00"],
    "SOC":[75,72,68],
    "Voltage":[305.2,306.5,307.1],
    "Current":[-12.3,-10.8,-9.4],
    "Load":[60,80,74],
    "PV":[45,55,50]
})

# ---------------- FRONTEND ----------------
package_json = """{
  "name": "battery-admin",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "start": "react-scripts start"
  }
}
"""

app_js = """import React, { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState({});
  const [recs, setRecs] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/battery/status")
      .then(res => res.json())
      .then(setStatus);
    fetch("http://localhost:8000/battery/recommendations")
      .then(res => res.json())
      .then(data => setRecs(data.Recs));
  }, []);

  return (
    <div style={{padding:"20px"}}>
      <h2>Dawnice Battery Admin Panel</h2>
      <p><b>SOC:</b> {status.SOC}%</p>
      <p><b>Voltage:</b> {status.Voltage} V</p>
      <p><b>Current:</b> {status.Current} A</p>
      <p><b>Load:</b> {status.Load} kW</p>
      <p><b>PV:</b> {status.PV} kW</p>

      <h3>⚡ Recommendations:</h3>
      <ul>
        {recs.map((r,i)=><li key={i}>{r}</li>)}
      </ul>
    </div>
  );
}

export default App;
"""

# ---------------- README ----------------
readme_txt = """# Battery Admin Project

## Backend (FastAPI)
1. Go to `backend/`
2. Install deps: `pip install -r requirements.txt`
3. Run: `uvicorn main:app --reload`
4. API runs at: `http://localhost:8000`

## Frontend (React)
1. Go to `frontend/`
2. Run `npm install`
3. Run `npm start`
4. Opens at: `http://localhost:3000`

## Features
- API endpoints for `/battery/status`, `/battery/logs`, `/battery/recommendations`
- Frontend dashboard with status + recommendations
- Dummy Excel used as data source (replace with real Modbus later)
"""

# Write backend files
with open(os.path.join(backend_dir, "main.py"), "w") as f:
    f.write(main_py)

with open(os.path.join(backend_dir, "decision.py"), "w") as f:
    f.write(decision_py)

with open(os.path.join(backend_dir, "requirements.txt"), "w") as f:
    f.write(requirements_txt)

dummy_data.to_excel(os.path.join(backend_dir, "dummy.xlsx"), index=False)

# Write frontend files
with open(os.path.join(base_dir, "frontend", "package.json"), "w") as f:
    f.write(package_json)

with open(os.path.join(frontend_dir, "App.js"), "w") as f:
    f.write(app_js)

# Write README
with open(os.path.join(base_dir, "README.md"), "w") as f:
    f.write(readme_txt)

# Create ZIP
zip_name = "my-admin-project.zip"
with zipfile.ZipFile(zip_name, 'w') as zipf:
    for root, _, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, base_dir))

zip_name
