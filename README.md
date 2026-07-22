# Solar & Wind Deployment Intelligence Platform

Full-stack application for evaluating solar and wind deployment potential. The project includes a FastAPI backend for environmental, GIS, dashboard, and prediction APIs, plus a React frontend for the user interface.

## Project Structure

```text
backend/
  app/
    main.py              FastAPI application entry point
    database.py          PostgreSQL connection setup
    routers/             API route modules
    services/            Data and prediction services
    ml/                  Solar and wind model helpers
frontend/
  public/                Static frontend assets
  src/                   React source code
```

## Prerequisites

- Python 3.10+
- Node.js and npm
- PostgreSQL

The backend currently expects PostgreSQL to be available at:

```text
postgresql://postgres:2004@localhost:5432/solar_wind_db
```

## Run the Backend

From the repository root:

```powershell
cd backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

The API runs at `http://127.0.0.1:8000`.

## Run the Frontend

From the repository root:

```powershell
cd frontend
npm install
npm start
```

The frontend runs at `http://localhost:3000` and calls the backend at `http://127.0.0.1:8000`.

## Available Frontend Scripts

```powershell
npm start
npm test
npm run build
```

## Notes

- Backend CORS is configured for `http://localhost:3000` and `http://127.0.0.1:3000`.
- Database tables are created automatically when the FastAPI app starts.
- External environmental data services use HTTP requests from the backend service layer.
