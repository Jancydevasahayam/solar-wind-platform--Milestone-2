def predict_solar_potential(avg_solar, temperature):
    """
    Simple solar prediction logic.
    """

    if avg_solar >= 5:
        potential = "High"
    elif avg_solar >= 4:
        potential = "Medium"
    else:
        potential = "Low"

    return {
        "average_solar_irradiance": avg_solar,
        "average_temperature": temperature,
        "solar_potential": potential
    }



def calculate_site_score(nasa_data, weather_data):
    """
    Calculates renewable energy site suitability
    using NASA and weather data.
    """

    # Extract solar irradiance safely
    solar_irradiance = nasa_data.get("solar_irradiance", 0)

    if isinstance(solar_irradiance, dict):
        values = list(solar_irradiance.values())
        solar_irradiance = sum(values) / len(values) if values else 0


    # Solar classification
    if solar_irradiance >= 5:
        solar_potential = "High"

    elif solar_irradiance >= 4:
        solar_potential = "Medium"

    else:
        solar_potential = "Low"



    # Extract wind speed safely
    wind_speed = weather_data.get("wind_speed", 0)

    if isinstance(wind_speed, dict):
        values = list(wind_speed.values())
        wind_speed = float(values[0]) if values else 0


    # Wind classification
    if wind_speed >= 7:
        wind_potential = "High"

    elif wind_speed >= 4:
        wind_potential = "Medium"

    else:
        wind_potential = "Low"



    # Recommendation
    if solar_potential == "High" and wind_potential == "High":
        recommendation = "Highly Suitable"

    elif solar_potential == "Low" and wind_potential == "Low":
        recommendation = "Not Suitable"

    else:
        recommendation = "Moderately Suitable"


    return {
        "solar_potential": solar_potential,
        "wind_potential": wind_potential,
        "recommendation": recommendation
    }



# ---------------- Wind Prediction API Service ----------------

def predict_wind_potential(avg_wind_speed, temperature):
    """
    Simple wind prediction logic.
    """

    if avg_wind_speed >= 8:
        potential = "High"

    elif avg_wind_speed >= 5:
        potential = "Medium"

    else:
        potential = "Low"


    return {
        "average_wind_speed": avg_wind_speed,
        "average_temperature": temperature,
        "wind_potential": potential
    }