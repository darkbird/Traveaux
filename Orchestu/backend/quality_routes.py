from flask import Blueprint, jsonify, request
from .quality_assurance.data_handler import QualityDataHandler
# from .quality_assurance.models import QualityDataPoint # For type hinting if needed
from .routes import agents_db # To validate agent_id

quality_bp = Blueprint('quality', __name__, url_prefix='/quality')

# Instantiate the handler globally for this blueprint
# In a larger app, this might be managed by Flask app context or a DI framework
data_handler = QualityDataHandler()

@quality_bp.route('/data_point', methods=['POST'])
def record_quality_data_point_route():
    """
    Endpoint to record a new quality data point.
    Expects a JSON payload matching the structure of QualityDataPoint (partially).
    """
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    agent_id = data.get('agent_id')
    if not agent_id:
        return jsonify({"error": "agent_id is required"}), 400

    if agent_id not in agents_db:
        return jsonify({"error": f"Agent {agent_id} not found"}), 404

    # The data_handler.record_data_point will validate other required fields
    # and add data_point_id, timestamp.
    result = data_handler.record_data_point(data)

    if result["status"] == "success":
        return jsonify(result), 201 # 201 Created for successful recording
    else:
        return jsonify(result), 400 # Bad request if data was invalid


@quality_bp.route('/data_points/<agent_id>', methods=['GET'])
def get_agent_quality_data_points_route(agent_id: str):
    """
    Endpoint to retrieve all quality data points for a specific agent.
    """
    if agent_id not in agents_db:
        return jsonify({"error": f"Agent {agent_id} not found"}), 404

    agent_data_points = data_handler.get_data_points_for_agent(agent_id)
    return jsonify(agent_data_points), 200

@quality_bp.route('/data_points', methods=['GET'])
def get_all_quality_data_points_route():
    """
    Endpoint to retrieve all recorded quality data points.
    Mainly for debugging or overview purposes.
    """
    all_data_points = data_handler.get_all_data_points()
    return jsonify(all_data_points), 200
