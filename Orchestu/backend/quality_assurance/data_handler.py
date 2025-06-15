from typing import List, Dict
import uuid
import datetime
from .models import QualityDataPoint # Assuming models.py is in the same directory

class QualityDataHandler:
    def __init__(self):
        self.data_points: List[QualityDataPoint] = []
        print("QualityDataHandler initialized.")

    def record_data_point(self, data: Dict) -> Dict: # Expecting a dict, will construct QualityDataPoint
        """
        Records a new quality data point.
        The input 'data' is expected to be a dictionary that can be used to create QualityDataPoint.
        It will be augmented with a data_point_id and a current timestamp if not provided.
        """

        # Basic validation for required fields from the input dictionary
        required_fields = ['agent_id', 'metric_name', 'value']
        if not all(field in data for field in required_fields):
            # Log the error and return an error response
            error_message = f"Missing one or more required fields: {required_fields}"
            print(f"Error recording data point: {error_message}")
            return {"status": "error", "message": error_message}

        # Construct the QualityDataPoint, adding id and timestamp
        # This ensures all QualityDataPoint instances stored are complete.
        new_data_point: QualityDataPoint = {
            "data_point_id": str(uuid.uuid4()),
            "agent_id": data['agent_id'],
            "metric_name": data['metric_name'],
            "value": float(data['value']), # Ensure value is float
            "timestamp": data.get('timestamp', datetime.datetime.utcnow().isoformat()),
            "context": data.get('context', {})
        }

        self.data_points.append(new_data_point)
        log_message = f"Recorded quality data: {new_data_point}"
        print(log_message) # Using print for now, logger is preferred for production

        return {"status": "success", "message": "Quality data point recorded", "data": new_data_point}

    def get_data_points_for_agent(self, agent_id: str) -> List[QualityDataPoint]:
        """
        Retrieves all quality data points associated with a specific agent_id.
        """
        agent_specific_data = [dp for dp in self.data_points if dp['agent_id'] == agent_id]
        print(f"Retrieved {len(agent_specific_data)} data points for agent_id: {agent_id}")
        return agent_specific_data

    def get_all_data_points(self) -> List[QualityDataPoint]:
        """
        Retrieves all recorded quality data points.
        """
        print(f"Retrieved all {len(self.data_points)} data points.")
        return self.data_points
