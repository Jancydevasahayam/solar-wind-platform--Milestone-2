import requests

API_KEY = "2d75b4bac6885c7f80c3f8eded9a49a4"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(latitude: float, longitude: float):

    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return {
            "status_code": response.status_code,
            "response": response.text
        }

    data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
        "wind_direction": data["wind"]["deg"]
    }