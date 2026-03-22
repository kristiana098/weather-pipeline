import os
import json
import requests
from dotenv import load_dotenv
from datetime import date, timedelta

load_dotenv()


def fetch_weather() -> list[dict]:
    """
    Fetch weather data from a weather API.

    Returns a list of weather dictionaries, each with keys:
        location, date, temperature, precipitation, wind
    """

      

    api_key = os.getenv("AV_API_KEY")

    locations = {
        "Aalborg": (57.048, 9.9187),
        "Athens": (37.9838, 23.7275),
        "Copenhagen": (55.6761, 12.5683)  # change if needed
    }

    tomorrow = (date.today() + timedelta(days=1)).isoformat()

    results = []

    for name, (lat, lon) in locations.items():
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}"
            f"&daily=temperature_2m_max,precipitation_sum,windspeed_10m_max"
            f"&timezone=auto"
        )

        response = requests.get(url,verify=False)
        data = response.json()

        results.append({
            "location": name,
            "date": tomorrow,
            "temperature": data["daily"]["temperature_2m_max"][1],
            "precipitation": data["daily"]["precipitation_sum"][1],
            "wind": data["daily"]["windspeed_10m_max"][1],
        })

    return results


if __name__ == "__main__":
    weather = fetch_weather()
    for w in weather:
        print(w)