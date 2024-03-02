from app.jwt_handler import create_jwt_token
from datetime import timedelta


def test_get_healthcheck(mock_env):
    response = mock_env.get("/healthcheck")
    assert response.status_code == 200


def test_read_root(mock_env):
    response = mock_env.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_create_item(mock_env):
    response = mock_env.post("/post-example", json={"item": "test_item"})
    assert response.status_code == 200
    assert response.json() == {"received_data": {"item": "test_item"}}


def test_login_for_access_token(mock_env):
    # Test valid credentials
    response = mock_env.post(
        "/token", json={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

    # Test invalid credentials
    response = mock_env.post(
        "/token", json={"username": "invaliduser", "password": "invalidpassword"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"


def test_protected_route(mock_env):
    # Test with a valid token (should return 200 OK)
    valid_token = create_jwt_token(
        data={"sub": "testuser"}, expires_delta=timedelta(minutes=10)
    )
    response = mock_env.get(f"/protected?token={valid_token}")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "You are authenticated!"
    assert "user" in response.json()
    assert (
        "sub" in response.json()["user"]
    )  # Check if the username is present in the response
