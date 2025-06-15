import json # For pretty printing payload in log, not strictly necessary

class N8NConnector:
    def __init__(self, n8n_base_url: str = "http://localhost:5678", api_key: str = "dummy_api_key"):
        self.n8n_base_url = n8n_base_url
        self.api_key = api_key # Placeholder for future use
        print(f"N8NConnector initialized with base_url: {self.n8n_base_url} and api_key: {self.api_key}")

    def trigger_workflow(self, workflow_tag_or_id: str, payload: dict) -> dict:
        """
        Simulates triggering an n8n workflow.
        In a real implementation, this would make an HTTP POST request to n8n.
        """
        # For logging, we can pretty-print the JSON payload if it's complex
        try:
            payload_str = json.dumps(payload, indent=2)
        except TypeError:
            payload_str = str(payload)

        log_message = (
            f"Simulating: Triggering n8n workflow '{workflow_tag_or_id}' "
            f"at {self.n8n_base_url} with API key '{self.api_key}'. Payload:\n{payload_str}"
        )
        print(log_message) # Using print for simulation, a logger would be better in production

        # Simulate a successful response from n8n
        return {
            "status": "simulated_success",
            "workflow_id": workflow_tag_or_id,
            "message": "n8n workflow trigger simulated successfully.",
            "triggered_by_payload": payload
        }
