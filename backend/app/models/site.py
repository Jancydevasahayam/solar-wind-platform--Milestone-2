from sqlalchemy import Column, Integer, Float, String
from app.models.base import Base

class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    solar_potential = Column(String)
    wind_potential = Column(String)
    recommendation = Column(String)