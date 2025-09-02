from app.repositories.user import UserRepository, User

user_repo = UserRepository("/Users/kang/Desktop/motto/app/models/user.txt")

def test_load_users():
    a = user_repo.load_users()
    
    # 리스트인지 확인
    assert isinstance(a, list)

    # 리스트가 비어있지 않다면 각 요소가 User인지 확인
    if a:  # 빈 리스트가 아닌 경우에만 체크
        assert all(isinstance(user, User) for user in a)