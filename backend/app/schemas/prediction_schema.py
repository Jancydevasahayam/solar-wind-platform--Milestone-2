from pydantic import BaseModel


class PredictionRequest(BaseModel):
    average_solar: float
    temperature: float



class WindPredictionRequest(BaseModel):
    average_wind_speed: float
    temperature: float



class SolarEnergyPredictionRequest(BaseModel):
    irradiance: float
    temperature: float



class WindEnergyPredictionRequest(BaseModel):
    wind_speed: float
    temperature: float