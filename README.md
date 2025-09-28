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
