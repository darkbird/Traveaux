from functools import wraps
from flask import request, jsonify, g
from .services import get_user_by_username # To fetch user details for g.current_user

# This is a mock user store, ideally this comes from your user service/database
# For simulation, we'll use the users_db from services.py if needed,
# but the token itself will contain the username.

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        # Simulate token validation and user extraction
        # In a real app, you'd use a JWT library to decode and verify the token.
        # Here, we expect a specific format: "fake_jwt_token_for_<username>"
        if token.startswith("fake_jwt_token_for_"):
            username = token.replace("fake_jwt_token_for_", "")
            # Fetch the full user object to get roles etc.
            user = get_user_by_username(username)
            if user:
                g.current_user = user # Store the full user object in g
                print(f"User {username} authenticated via token.")
            else:
                g.current_user = None # User from token not found
                print(f"User {username} from token not found in user database.")
                # Even if token format is ok, if user doesn't exist, it's invalid.
                return jsonify({"message": "Token is invalid (user not found)!"}), 401
        else:
            g.current_user = None
            return jsonify({"message": "Token is invalid (format error)!"}), 401

        return f(*args, **kwargs)
    return decorated_function

def role_required(required_role: str):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not hasattr(g, 'current_user') or g.current_user is None:
                # This should ideally be caught by @token_required first
                return jsonify({"message": "Authentication required."}), 401

            user_role = g.current_user.get('role')
            if user_role != required_role:
                print(f"User {g.current_user.get('username')} with role '{user_role}' attempted action requiring role '{required_role}'.")
                return jsonify({"message": f"Insufficient permissions! Requires role: {required_role}"}), 403

            print(f"User {g.current_user.get('username')} authorized for role '{required_role}'.")
            return f(*args, **kwargs)
        return decorated_function
    return decorator
