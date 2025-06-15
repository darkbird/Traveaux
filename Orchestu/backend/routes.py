from flask import Blueprint, jsonify, request
import uuid
import datetime
from .models import Agent # Import Agent class
from .auth.decorators import token_required, role_required # Import decorators

agents_bp = Blueprint('agents', __name__, url_prefix='/agents')

# In-memory storage for agents (for now)
agents_db = {}

@agents_bp.route('/', methods=['GET'])
def get_agents():
    return jsonify([agent for agent in agents_db.values()]), 200

@agents_bp.route('/', methods=['POST'])
@token_required
def create_agent():
    data = request.json
    if not data or not data.get('name') or not data.get('description'):
        return jsonify({"message": "Missing name or description"}), 400

    agent_id = str(uuid.uuid4())

    # creation_date is handled by the Agent model constructor
    new_agent = Agent(
        agent_id=agent_id,
        name=data['name'],
        description=data['description'],
        status=data.get('status', 'active'), # Default status if not provided
        config=data.get('config', {})      # Default config if not provided
    )

    agents_db[agent_id] = new_agent.to_dict()
    return jsonify(agents_db[agent_id]), 201

@agents_bp.route('/<agent_id>', methods=['GET'])
def get_agent(agent_id):
    agent = agents_db.get(agent_id)
    if agent:
        return jsonify(agent), 200
    return jsonify({"message": "Agent not found"}), 404

@agents_bp.route('/<agent_id>', methods=['PUT'])
@token_required
def update_agent(agent_id):
    if agent_id not in agents_db:
        return jsonify({"message": "Agent not found"}), 404

    data = request.json
    if not data:
        return jsonify({"message": "No update data provided"}), 400

    agent_to_update = agents_db[agent_id]

    # Update fields if provided in the request
    agent_to_update['name'] = data.get('name', agent_to_update['name'])
    agent_to_update['description'] = data.get('description', agent_to_update['description'])
    agent_to_update['status'] = data.get('status', agent_to_update['status'])
    agent_to_update['config'] = data.get('config', agent_to_update['config'])
    # agent_id and creation_date should not be updated

    agents_db[agent_id] = agent_to_update # Update the stored dictionary
    return jsonify(agent_to_update), 200

@agents_bp.route('/<agent_id>', methods=['DELETE'])
@token_required
@role_required('admin')
def delete_agent(agent_id):
    if agent_id in agents_db:
        deleted_agent = agents_db.pop(agent_id)
        return jsonify({"message": f"Agent {agent_id} deleted successfully", "agent": deleted_agent}), 200
        # Or use 204 No Content, but then we can't return the deleted agent's info
        # return '', 204
    return jsonify({"message": "Agent not found"}), 404
