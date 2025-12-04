import requests
from abc import ABC, abstractmethod

class BaseAPIClient(ABC):
    """
    Abstract base class for all API clients.
    Defines the structure and common behavior.
    """

    def __init__(self, base_url):
        self._base_url = base_url  # Encapsulation (private variable)

    @abstractmethod
    def fetch_data(self, *args, **kwargs):
        """
        Abstract method to fetch data from API.
        Must be implemented in child classes.
        """
        pass

    def _make_request(self, endpoint, params=None):
        """
        Common method to make an HTTP GET request.
        """
        try:
            response = requests.get(
                self._base_url + endpoint,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            print("HTTP Error:", e)
            return None

        except requests.exceptions.ConnectionError:
            print("Network Error: Could not connect to API.")
            return None

        except Exception as e:
            print("Unexpected Error:", e)
            return None
