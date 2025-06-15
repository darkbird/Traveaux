from typing import List, Dict as PyDict # Renaming to avoid conflict
from typing_extensions import TypedDict

class OrchestrationFlowStep(TypedDict):
    step_id: str
    task_type: str
    params: PyDict[str, any]

class OrchestrationFlow(TypedDict):
    flow_id: str # Added a flow_id for better identification
    name: str    # Added a name for the flow
    steps: List[OrchestrationFlowStep]
