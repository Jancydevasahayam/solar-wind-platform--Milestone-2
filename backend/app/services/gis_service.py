def analyze_location(latitude, longitude):
    """
    Dummy GIS analysis.
    """

    elevation = 50
    land_cover = "Open Land"
    slope = 3.2

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