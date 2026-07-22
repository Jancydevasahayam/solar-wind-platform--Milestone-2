from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.site import Site


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/site/{site_id}")
def get_site_dashboard(
    site_id: int,
    db: Session = Depends(get_db)
):

    site = db.query(Site).filter(
        Site.id == site_id
    ).first()


    if not site:
        raise HTTPException(
            status_code=404,
            detail="Site not found"
        )


    return {
        "site_id": site.id,

        "location": {
            "latitude": site.latitude,
            "longitude": site.longitude
        },

        "assessment": {
            "solar_potential": site.solar_potential,
            "wind_potential": site.wind_potential,
            "recommendation": site.recommendation
        }
    }