from flask import Blueprint, jsonify, request

# To access agents_db, we need to import it.
# This assumes routes.py is in the parent directory and agents_db is accessible.
# If app is structured as a package, relative imports are better.
# For now, let's assume direct access for simplicity, might need adjustment.
from .routes import agents_db  # Trying to import agents_db
from .orchestration.engine import OrchestrationEngine
from .orchestration.flow_schema import OrchestrationFlow # For type hinting if needed, and validation

orchestration_bp = Blueprint('orchestration', __name__, url_prefix='/orchestration')

@orchestration_bp.route('/agents/<agent_id>/orchestrate', methods=['POST'])
def orchestrate_agent_flow(agent_id):
    # 1. Retrieve the agent
    agent = agents_db.get(agent_id)
    if not agent:
        return jsonify({"message": f"Agent {agent_id} not found"}), 404

    # 2. Get flow from request body
    flow_data = request.json
    if not flow_data:
        return jsonify({"message": "No orchestration flow provided in request body"}), 400

    # Basic validation for the flow structure (can be more robust)
    if 'steps' not in flow_data or not isinstance(flow_data['steps'], list):
        return jsonify({"message": "Invalid flow structure: 'steps' list is missing or not a list."}), 400
    if 'flow_id' not in flow_data or 'name' not in flow_data : # Enforcing fields added to OrchestrationFlow
         return jsonify({"message": "Invalid flow structure: 'flow_id' or 'name' is missing."}), 400


    # 3. Instantiate OrchestrationEngine and execute flow
    engine = OrchestrationEngine()

    # The engine expects an OrchestrationFlow typed dict.
    # For now, we pass the raw dict, assuming it matches the structure.
    # In a real app, you might want to validate/deserialize into the TypedDict.
    execution_logs = engine.execute_flow(agent_id=agent_id, flow=flow_data) # Pass flow_data as OrchestrationFlow

    # 4. Return execution logs
    return jsonify({
        "agent_id": agent_id,
        "flow_id": flow_data.get('flow_id', 'N/A'),
        "flow_name": flow_data.get('name', 'Unnamed Flow'),
        "execution_logs": execution_logs
    }), 200
