from app.repositories.user import UserRepository
from app.utils.auth import create_access_token

user_repo = UserRepository(file_path="app/models/user.txt")

def authenticate_user(email: str, password: str):
    user = user_repo.get_user_by_email(email)

    if not user or user.password != password:
        return None
    return user

def user_login(email: str, password: str):
    user = authenticate_user(email, password)
    if not user:
        return None
    
    access_token = create_access_token(data={"sub": user.email})
    return {
        "access_token": access_token,
    }