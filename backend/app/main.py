from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models.base import Base
from app.models.site import Site

from app.routers import prediction
from app.routers import environmental
from app.routers import dashboard
from app.routers import gis


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Solar & Wind Deployment Intelligence Platform"
)


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register Routers
app.include_router(prediction.router)
app.include_router(environmental.router)
app.include_router(dashboard.router)
app.include_router(gis.router)


# Root Endpoint
@app.get("/")
def root():
    return {
        "message": "Solar & Wind Deployment Intelligence Platform API is running!"
    }