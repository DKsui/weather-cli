import requests

def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "wind_speed_10m"
        ),
    }
    try:
        response = requests.get(
            url,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        current = data["current"]
        units = data["current_units"]
        return {
            "temperature": current["temperature_2m"],
            "temperature_unit": units["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "humidity_unit": units["relative_humidity_2m"],
            "feels_like": current["apparent_temperature"],
            "feels_like_unit": units["apparent_temperature"],
            "wind_speed": current["wind_speed_10m"],
            "wind_speed_unit": units["wind_speed_10m"],
        }
    except requests.RequestException as error:
        print(f"Request failed: {error}")
        return None
    except (KeyError, TypeError) as error:
        print(f"Unexpected response structure: {error}")
        return None