from fastapi import APIRouter
from app.schemas.gis_schema import GISRequest
from app.services.gis_service import analyze_location

router = APIRouter(
    prefix="/gis",
    tags=["GIS"]
)

@router.post("/analyze")
def analyze(request: GISRequest):
    return analyze_location(request.latitude, request.longitude)