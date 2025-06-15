from typing import Dict as PyDict, Any
from typing_extensions import TypedDict
import datetime

class QualityDataPoint(TypedDict):
    data_point_id: str # Added for unique identification
    agent_id: str
    metric_name: str
    value: float
    timestamp: str # ISO format string
    context: PyDict[str, Any] # Flexible dictionary for additional context
