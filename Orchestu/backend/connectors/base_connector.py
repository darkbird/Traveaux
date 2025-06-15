import abc
from typing import Dict, Optional

class BaseAPIConnector(abc.ABC):
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url
        self.api_key = api_key
        if self.api_key:
            print(f"{self.__class__.__name__} initialized with base_url: {self.base_url} and an API key.")
        else:
            print(f"{self.__class__.__name__} initialized with base_url: {self.base_url} (no API key).")

    @abc.abstractmethod
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Sends a GET request to the specified endpoint.
        """
        pass

    @abc.abstractmethod
    def post(self, endpoint: str, data: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict:
        """
        Sends a POST request to the specified endpoint.
        """
        pass

    # You could also add put, delete, etc. as needed.
    # def put(self, endpoint: str, data: Optional[Dict] = None) -> Dict:
    #     pass
    #
    # def delete(self, endpoint: str) -> Dict:
    #     pass
