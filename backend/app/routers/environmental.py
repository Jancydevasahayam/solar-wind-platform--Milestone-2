from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.site import Site
from app.schemas.environment import LocationRequest

from app.services.nasa_service import get_nasa_power_data
from app.services.weather_service import get_weather_data
from app.services.prediction_service import calculate_site_score


router = APIRouter(
    prefix="/environment",
    tags=["Environmental Data"]
)


@router.post("/location")
def receive_location(
    location: LocationRequest,
    db: Session = Depends(get_db)
):

    # Get NASA solar data
    nasa_data = get_nasa_power_data(
        latitude=location.latitude,
        longitude=location.longitude
    )


    # Get weather data
    weather_data = get_weather_data(
        latitude=location.latitude,
        longitude=location.longitude
    )


    # Calculate suitability
    assessment = calculate_site_score(
        nasa_data,
        weather_data
    )


    # Save location result
    site = Site(
        latitude=location.latitude,
        longitude=location.longitude,
        solar_potential=assessment["solar_potential"],
        wind_potential=assessment["wind_potential"],
        recommendation=assessment["recommendation"]
    )


    db.add(site)
    db.commit()
    db.refresh(site)


    return {
        "site_id": site.id,
        "latitude": site.latitude,
        "longitude": site.longitude,
        "nasa_data": nasa_data,
        "weather_data": weather_data,
        "assessment": assessment
    }