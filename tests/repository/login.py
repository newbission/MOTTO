import json
from typing import List, Optional
# FILE_PATH = "tests/crud/user.txt"
User = dict

class UserRepository:
    def __init__(self, file_path: str = "user.txt"):
        self.file_path = file_path
    
    def load_users(self) -> List[User]:
        with open(self.file_path, "r") as f:
            return json.load(f)
        
    def get_user_by_id(self, user_id: str) -> Optional[User]:
            users = self.load_users()
            for user in users:
                if user.get("id") == user_id:
                    return user
            return None

