from fastapi import APIRouter

from app.schemas.prediction_schema import (
    PredictionRequest,
    WindPredictionRequest,
    SolarEnergyPredictionRequest,
    WindEnergyPredictionRequest
)

from app.services.prediction_service import (
    predict_solar_potential,
    predict_wind_potential
)

from app.services.ml_prediction_service import (
    get_solar_energy_prediction,
    get_wind_energy_prediction
)


router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)



# Solar Classification
@router.post("/solar")
def solar_prediction(request: PredictionRequest):

    return predict_solar_potential(
        request.average_solar,
        request.temperature
    )



# Wind Classification
@router.post("/wind")
def wind_prediction(request: WindPredictionRequest):

    return predict_wind_potential(
        request.average_wind_speed,
        request.temperature
    )



# ML Solar Energy Prediction
@router.post("/solar-energy")
def solar_energy_prediction(
    request: SolarEnergyPredictionRequest
):

    return get_solar_energy_prediction(
        request.irradiance,
        request.temperature
    )



# ML Wind Energy Prediction
@router.post("/wind-energy")
def wind_energy_prediction(
    request: WindEnergyPredictionRequest
):

    return get_wind_energy_prediction(
        request.wind_speed,
        request.temperature
    )