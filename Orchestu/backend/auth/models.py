from typing_extensions import TypedDict
import datetime

class User(TypedDict):
    user_id: str
    username: str
    hashed_password: str
    role: str # e.g., 'user', 'admin', 'viewer'
    creation_date: str # ISO format string
