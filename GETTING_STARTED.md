# Getting Started with Battery Admin

This guide will help you set up and run the Battery Admin project on your local machine.

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- npm or yarn

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/energydawnice/mapping.git
cd mapping
```

### 2. Set Up the Backend

```bash
# Navigate to backend directory
cd backend

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the backend server
uvicorn main:app --reload
```

The backend will be available at: `http://localhost:8000`

#### Test the Backend

You can test the backend API endpoints:

```bash
# In a new terminal, while the server is running
cd backend
python test_api.py
```

Or test manually with curl:

```bash
curl http://localhost:8000/battery/status
curl http://localhost:8000/battery/logs
curl http://localhost:8000/battery/recommendations
```

### 3. Set Up the Frontend

```bash
# In a new terminal, navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The frontend will automatically open at: `http://localhost:3000`

## API Documentation

Once the backend is running, you can access the interactive API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
.
├── backend/              # FastAPI backend server
│   ├── main.py          # API endpoints definition
│   ├── decision.py      # Decision engine logic
│   ├── dummy.xlsx       # Sample data source
│   ├── requirements.txt # Python dependencies
│   └── test_api.py      # API testing script
│
├── frontend/            # React frontend application
│   ├── src/
│   │   ├── App.js       # Main React component
│   │   └── index.js     # React entry point
│   ├── public/
│   │   └── index.html   # HTML template
│   └── package.json     # Node.js dependencies
│
├── README.md            # Project documentation
└── GETTING_STARTED.md   # This file
```

## Troubleshooting

### Backend Issues

**Port 8000 already in use:**
```bash
# Use a different port
uvicorn main:app --reload --port 8001
```

**Module not found errors:**
```bash
# Make sure you're in the backend directory and venv is activated
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend Issues

**Port 3000 already in use:**
- The React dev server will automatically prompt you to use a different port (Y/N)

**npm install fails:**
```bash
# Clear npm cache and try again
npm cache clean --force
npm install
```

**Cannot connect to backend:**
- Make sure the backend server is running on port 8000
- Check CORS settings in `backend/main.py`
- Update the API URL in `frontend/src/App.js` if using a different port

## Next Steps

1. Replace `dummy.xlsx` with real Modbus communication
2. Add database for persistent data storage
3. Implement user authentication
4. Add more advanced analytics and visualizations
5. Deploy to production environment

## Support

For issues and questions, please open an issue on the GitHub repository.
