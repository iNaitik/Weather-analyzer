from config import API_KEY, base_url
import requests

def get_weather_data(city_name):
    parameters = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(base_url, params=parameters)
    data = response.json()

    data_dict = {
        "name": data["name"],
        "weather": data["weather"],
        "main": data["main"],
        "wind": data["wind"]
    }

    return data_dict