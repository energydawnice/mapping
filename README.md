# Battery Admin Project

This project provides a web-based admin panel for monitoring and managing a battery energy storage system (BESS) for a microgrid with PV and genset integration.

## Project Structure

```
.
├── backend/           # FastAPI backend server
│   ├── main.py       # API endpoints
│   ├── decision.py   # Decision engine for recommendations
│   ├── requirements.txt
│   └── dummy.xlsx    # Sample data source
├── frontend/         # React frontend application
│   ├── src/
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   │   └── index.html
│   └── package.json
└── README.md         # This file
```

## Backend (FastAPI)

The backend provides REST API endpoints for battery monitoring and recommendations.

### Setup

1. Go to `backend/` directory:
   ```bash
   cd backend/
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

4. API will be available at: `http://localhost:8000`

### API Endpoints

- `GET /battery/status` - Get current battery status (SOC, Voltage, Current, Load, PV)
- `GET /battery/logs` - Get historical battery data logs
- `GET /battery/recommendations` - Get operational recommendations based on current conditions

## Frontend (React)

The frontend provides a dashboard for visualizing battery status and recommendations.

### Setup

1. Go to `frontend/` directory:
   ```bash
   cd frontend/
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

4. Application will open at: `http://localhost:3000`

## Features

- **Real-time Monitoring**: View current battery SOC, voltage, current, load, and PV generation
- **Historical Data**: Access to logged battery data over time
- **Decision Support**: Intelligent recommendations based on:
  - SOC levels (min: 20%, max: 90%)
  - Load conditions (genset minimum: 44 kW)
  - PV generation (capacity: 65 kWp)
  - Genset operation optimization

## System Parameters

- **GENSET_MIN**: 44 kW - Minimum genset operation load
- **PV_CAPACITY**: 65 kWp - Photovoltaic system capacity
- **SOC_MIN**: 20% - Minimum state of charge
- **SOC_MAX**: 90% - Maximum state of charge

## Data Source

Currently using `dummy.xlsx` as a data source. This should be replaced with real Modbus communication for production deployment.

## Future Enhancements

- Replace Excel data source with Modbus TCP/RTU integration
- Add real-time data streaming with WebSocket
- Implement data logging to database
- Add user authentication and authorization
- Create advanced analytics and reporting features
