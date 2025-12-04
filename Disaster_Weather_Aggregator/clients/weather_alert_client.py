import os
import requests
from dotenv import load_dotenv
from .base_client import BaseAPIClient
from logger import logging

load_dotenv()

class WeatherAlertClient(BaseAPIClient):
    """Fetches current weather data using OpenWeather free API."""

    def __init__(self):
        super().__init__(base_url="https://api.openweathermap.org/data/2.5/")
        self._api_key = os.getenv("OPENWEATHER_API_KEY")
        if not self._api_key:
            logging.error("OpenWeather API key not found in environment variables.")

    def fetch_data(self, latitude, longitude):
        """Fetch current weather for given lat & lon and return a readable summary."""
        if not self._api_key:
            return {"alerts": ["Weather data not available"]}

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={self._api_key}&units=metric"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            weather_list = data.get("weather", [])
            main_weather = weather_list[0]["main"] if weather_list else "Unknown"
            description = weather_list[0]["description"] if weather_list else "Unknown"
            temp = data.get("main", {}).get("temp", "N/A")

            summary = f"Weather: {main_weather} ({description}), Temp: {temp}°C"
            logging.info(f"Weather data fetched successfully for ({latitude}, {longitude})")
            return {"alerts": [summary]}

        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP Error while fetching weather: {e}")
            return {"alerts": ["Weather data not available"]}
        except requests.exceptions.ConnectionError:
            logging.error("Network Error: Could not connect to OpenWeather API.")
            return {"alerts": ["Weather data not available"]}
        except Exception as e:
            logging.error(f"Unexpected Error: {e}")
            return {"alerts": ["Weather data not available"]}
