from pydantic import BaseModel

class GISRequest(BaseModel):
    latitude: float
    longitude: float