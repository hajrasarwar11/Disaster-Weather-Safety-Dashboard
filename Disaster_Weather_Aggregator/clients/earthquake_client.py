from .base_client import BaseAPIClient
from logger import logging

class EarthquakeClient(BaseAPIClient):
    """
    Fetches earthquake data from USGS Earthquake API.
    """

    def __init__(self):
        base_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"
        super().__init__(base_url)

    def fetch_data(self, magnitude="2.5", timeframe="day"):
        """
        Fetch recent earthquakes based on magnitude and timeframe.

        magnitude: 1.0, 2.5, 4.5, etc.
        timeframe: hour, day, week, month.
        """
        endpoint = f"{magnitude}_{timeframe}.geojson"
        data = self._make_request(endpoint)

        if not data:
            logging.warning(f"No earthquake data received for magnitude={magnitude}, timeframe={timeframe}")
            return {"earthquakes": []}

        logging.info(f"Earthquake data fetched successfully for magnitude={magnitude}, timeframe={timeframe}")
        return {
            "earthquakes": data["features"]
        }