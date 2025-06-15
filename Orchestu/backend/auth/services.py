import hashlib
import uuid
import datetime
from typing import Dict, Optional
from .models import User # Assuming models.py is in the same directory

# In-memory store for users
users_db: Dict[str, User] = {}

def hash_password(password: str) -> str:
    """Hashes a password using SHA256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain password against a hashed password."""
    return hash_password(plain_password) == hashed_password

def create_user(username: str, password: str, role: str = 'user') -> Optional[User]:
    """
    Creates a new user if the username doesn't already exist.
    Stores the user in the in-memory users_db.
    """
    if username in users_db:
        print(f"Attempt to create existing user: {username}")
        return None  # User already exists

    user_id = str(uuid.uuid4())
    creation_date = datetime.datetime.utcnow().isoformat()
    hashed = hash_password(password)

    new_user: User = {
        "user_id": user_id,
        "username": username,
        "hashed_password": hashed,
        "role": role,
        "creation_date": creation_date
    }
    users_db[username] = new_user # Using username as key for quick lookup
    print(f"User created: {username}, Role: {role}")
    return new_user

def get_user_by_username(username: str) -> Optional[User]:
    """Retrieves a user by their username."""
    return users_db.get(username)

def authenticate_user(username: str, password: str) -> Optional[User]:
    """
    Authenticates a user by username and password.
    Returns the user object if authentication is successful, otherwise None.
    """
    user = get_user_by_username(username)
    if user and verify_password(password, user['hashed_password']):
        print(f"User authenticated: {username}")
        return user
    print(f"Authentication failed for user: {username}")
    return None

def get_user_without_password(user: User) -> Dict:
    """Helper to return user details excluding the password."""
    user_data = user.copy()
    del user_data["hashed_password"]
    return user_data
