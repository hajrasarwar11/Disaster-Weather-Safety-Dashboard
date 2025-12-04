from clients.weather_alert_client import WeatherAlertClient
from clients.earthquake_client import EarthquakeClient

class DataAggregator:
    """
    Aggregates data from multiple APIs (Weather Alerts + Earthquakes)
    and produces a unified safety report.
    """

    def __init__(self):
        self.weather_client = WeatherAlertClient()
        self.eq_client = EarthquakeClient()

    def get_combined_report(self, lat, lon):
        """
        Returns a dictionary containing:
        - weather alerts
        - recent earthquakes
        """

        weather_data = self.weather_client.fetch_data(lat, lon)
        earthquake_data = self.eq_client.fetch_data()

        report = {
            "Weather Alerts": weather_data.get("alerts", []),
            "Recent Earthquakes": earthquake_data.get("earthquakes", [])
        }

        return report
