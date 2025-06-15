from flask import Blueprint, jsonify, request
# Assuming N8NConnector is in integrations.n8n_connector.client
from .integrations.n8n_connector.client import N8NConnector

integrations_bp = Blueprint('integrations', __name__, url_prefix='/integrations')

@integrations_bp.route('/n8n/trigger/<workflow_id>', methods=['POST'])
def trigger_n8n_workflow_route(workflow_id: str):
    """
    Endpoint to trigger an n8n workflow by its ID or tag.
    """
    payload = request.json
    if not payload:
        return jsonify({"message": "No payload provided"}), 400

    # Instantiate the connector (using default URL and API key for now)
    # In a real app, these would come from config
    connector = N8NConnector()

    # Call the trigger_workflow method
    result = connector.trigger_workflow(workflow_tag_or_id=workflow_id, payload=payload)

    return jsonify(result), 200
