from fastapi.testclient import TestClient
from app.main import app
from app.utils.auth import verify_token

client = TestClient(app)

def test_basic():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "pong"

def test_login_success():
    response = client.post(
        "/users/login",
        json={"email": "test1@example.com", "password": "1234"}
    )
    
    assert response.status_code == 200
    
    response_data = response.json()
    assert "access_token" in response_data
    token = response_data["access_token"]

    payload = verify_token(token)
    assert payload is not None
    assert payload["sub"] == "test1@example.com" 

def test_login_fail():
    response = client.post(
        "/users/login",
        json={"email": "test1@example.com", "password": "12345678"}
    )
    
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid email or password"}

def test_login_invalid_email():
    """존재하지 않는 이메일로 로그인 테스트"""
    response = client.post(
        "/users/login", 
        json={"email": "nonexistent@example.com", "password": "1234"}
    )
    
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid email or password"}

def test_token_validation():
    """토큰 검증 테스트"""
    login_response = client.post(
        "/users/login",
        json={"email": "test1@example.com", "password": "1234"}
    )
    
    token = login_response.json()["access_token"]
    