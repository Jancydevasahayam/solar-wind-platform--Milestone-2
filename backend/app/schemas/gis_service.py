def analyze_location(latitude, longitude):
    """
    Dummy GIS analysis.
    Later we'll replace this with real GIS calculations.
    """

    elevation = 50          # meters
    land_cover = "Open Land"
    slope = 3.2             # degrees

    if slope < 5:
        suitability = "Highly Suitable"
    elif slope < 10:
        suitability = "Moderately Suitable"
    else:
        suitability = "Not Suitable"

    return {
        "latitude": latitude,
        "longitude": longitude,
        "elevation": elevation,
        "land_cover": land_cover,
        "slope": slope,
        "suitability": suitability
    }