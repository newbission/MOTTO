from app.repositories.user import UserRepository, User

user_repo = UserRepository("/Users/kang/Desktop/motto/app/models/user.txt")

def test_load_users():
    a = user_repo.load_users()
    assert isinstance(a, list)
    if a:  # 빈 리스트가 아닌 경우에만 체크
        assert all(isinstance(user, User) for user in a)