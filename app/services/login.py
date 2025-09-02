from app.repositories.user import UserRepository

user_repo = UserRepository(file_path="app/models/user.txt")

def user_login(email: str, password: str):
    user = user_repo.get_user_by_email(email)

    if not user or user.get("password") != password:
        return False
    return True