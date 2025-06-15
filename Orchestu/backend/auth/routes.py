from flask import Blueprint, request, jsonify
from .services import create_user, authenticate_user, get_user_without_password, get_user_by_username

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user') # Default role to 'user' if not specified

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    # Check if user already exists
    if get_user_by_username(username):
        return jsonify({"message": "Username already exists"}), 409 # Conflict

    new_user = create_user(username, password, role)
    if new_user:
        return jsonify({"message": "User created successfully", "user": get_user_without_password(new_user)}), 201
    else:
        # This case should ideally be caught by the check above, but as a fallback:
        return jsonify({"message": "User creation failed"}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = authenticate_user(username, password)
    if user:
        # Simulate JWT token generation
        simulated_token = f"fake_jwt_token_for_{user['username']}"
        user_details = get_user_without_password(user)
        return jsonify({"token": simulated_token, "user": user_details}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401
