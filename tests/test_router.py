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


# def test_login_for_access_token(mock_env):
#     response = mock_env.post("/token", data={"username": "testuser", "password": "testpassword"})
#     assert response.status_code == 200
#     assert "access_token" in response.json()
#     assert "token_type" in response.json()

# def test_protected_route():
#     # Create a valid JWT token for testing
#     token_data = {"sub": "testuser"}
#     expires_delta = timedelta(minutes=15)
#     valid_token = create_jwt_token(token_data, expires_delta)

#     client = TestClient(router)
#     response = client.get("/protected", headers={"Authorization": f"Bearer {valid_token}"})
#     assert response.status_code == 200
#     assert response.json() == {"message": "You are authenticated!", "user": {"sub": "testuser"}}

# def test_protected_route_invalid_token():
#     # Create an invalid JWT token for testing
#     invalid_token = "invalid_token"

#     client = TestClient(router)
#     response = client.get("/protected", headers={"Authorization": f"Bearer {invalid_token}"})
#     assert response.status_code == 401
#     assert response.json() == {"detail": "Invalid credentials"}
