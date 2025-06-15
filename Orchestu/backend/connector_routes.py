from flask import Blueprint, jsonify, request
from .connectors.cat_fact_connector import CatFactConnector
from .auth.decorators import token_required # Assuming auth setup is done

connectors_bp = Blueprint('connectors', __name__, url_prefix='/connectors')

@connectors_bp.route('/catfact', methods=['GET'])
@token_required # Secure this endpoint
def get_cat_fact():
    """
    Endpoint to get a (simulated) cat fact.
    """
    connector = CatFactConnector()
    result = connector.get() # Default endpoint "fact"
    return jsonify(result), 200

@connectors_bp.route('/catfact/test_post', methods=['POST'])
@token_required # Secure this endpoint
def post_cat_fact_test():
    """
    Endpoint to test a (simulated) POST request to a cat-fact-like service.
    """
    connector = CatFactConnector()
    payload = request.get_json()
    if not payload:
        return jsonify({"message": "No JSON payload provided for POST."}), 400

    # Using a specific endpoint for this test POST
    result = connector.post(endpoint="test_post_endpoint", data=payload)
    return jsonify(result), 200
