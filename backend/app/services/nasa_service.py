import requests

BASE_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"

def get_nasa_power_data(latitude: float, longitude: float):

    params = {
        "parameters": "ALLSKY_SFC_SW_DWN,T2M,PRECTOTCORR",
        "community": "RE",
        "longitude": longitude,
        "latitude": latitude,
        "start": "20240101",
        "end": "20240131",
        "format": "JSON"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return {"error": "Unable to fetch NASA POWER data"}

    data = response.json()

    parameters = data["properties"]["parameter"]

    return {
        "solar_irradiance": parameters["ALLSKY_SFC_SW_DWN"],
        "temperature": parameters["T2M"],
        "rainfall": parameters["PRECTOTCORR"]
    }