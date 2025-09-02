from fastapi.testclient import TestClient
from app.main import app

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
    assert response.json() == {"message": "Success!!"}

def test_login_fail():
    response = client.post(
        "/users/login",
        json={"email": "test1@example.com", "password": "12345678"}
    )

    assert response.status_code == 401
    assert response.json() == {"detail": "Fail.."}

