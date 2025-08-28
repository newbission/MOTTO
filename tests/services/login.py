from ..repository.login import UserRepository

user_repo = UserRepository(file_path="tests/repository/user.txt")

def user_login(user_id: str, password: str):
    user = user_repo.get_user_by_id(user_id)

    if not user or user.get("password") != password:
        return False
    return True