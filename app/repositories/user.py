import json
from typing import List, Optional
from sqlmodel import SQLModel

class User(SQLModel):
    email: str
    password: str

class UserRepository:
    def __init__(self, file_path: str = "user.txt"):
        self.file_path = file_path
    
    def load_users(self) -> List[User]:
        with open(self.file_path, "r") as f:
            data = json.load(f)
            return [User(**user_data) for user_data in data]
        
    def get_user_by_email(self, email: str) -> Optional[User]:
            users = self.load_users()
            for user in users:
                if user.get("email") == email:
                    return user
            return None