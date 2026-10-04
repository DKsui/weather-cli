from validation import validate_coordinates
# Weather CLI application
from weather_api import get_weather

def get_coordinates():
    try:
        latitude = float(input("Enter latitude (-90 to 90): "))
        longitude = float(input("Enter longitude (-180 to 180): "))
    except ValueError:
        print("Coordinates must be numeric values.")
        return None
    try:
        validate_coordinates(latitude, longitude)
    except ValueError as error:
        print(error)
        return None
    return latitude, longitude

def main():
    coordinates = get_coordinates()
    if coordinates is None:
        return
    latitude, longitude = coordinates
    weather = get_weather(latitude, longitude)
    if weather is None:
        print("Failed to retrieve weather data.")
        return
    print(f"Temperature: " 
          f"{weather['temperature']}" 
          f"{weather['temperature_unit']}"
    )
    print(f"Feels like: "
          f"{weather['feels_like']}"
          f"{weather['feels_like_unit']}"
    )
    print(f"Humidity: "
          f"{weather['humidity']}"
          f"{weather['humidity_unit']}"
    )
    print(f"Wind speed: "
          f"{weather['wind_speed']}"
          f"{weather['wind_speed_unit']}"
    )

if __name__ == "__main__":
    main()