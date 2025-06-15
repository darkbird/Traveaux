from typing import Dict, Optional
import json # For pretty printing in logs
from .base_connector import BaseAPIConnector

class CatFactConnector(BaseAPIConnector):
    def __init__(self):
        super().__init__(base_url="https://catfact.ninja")
        # This connector does not require an API key for its public endpoints.

    def get(self, endpoint: str = "fact", params: Optional[Dict] = None) -> Dict:
        """
        Simulates a GET request to the Cat Fact API.
        Default endpoint is "fact".
        """
        full_url = f"{self.base_url}/{endpoint}"
        params_str = json.dumps(params) if params else "{}"
        log_message = f"SIMULATING: GET request to {full_url} with params {params_str}"
        print(log_message) # Using print for simulation, logger is better for production

        # Hardcoded example response
        return {
            "fact": "Simulated: Cats have over 100 vocal sounds, while dogs have about 10.",
            "length": 70 # Adjusted length to match the new fact
        }

    def post(self, endpoint: str, data: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict:
        """
        Simulates a POST request. The Cat Fact API doesn't typically use POST for facts,
        so this is a generic simulation.
        """
        full_url = f"{self.base_url}/{endpoint}"
        data_str = json.dumps(data) if data else "{}"
        params_str = json.dumps(params) if params else "{}"

        log_message = (
            f"SIMULATING: POST request to {full_url} "
            f"with data {data_str} and params {params_str}"
        )
        print(log_message) # Using print for simulation

        # Hardcoded example response
        return {
            "message": f"Simulated POST to {endpoint} successful",
            "data_received": data,
            "params_received": params
        }
