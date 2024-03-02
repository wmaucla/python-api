import pytest
from unittest.mock import patch
from app.jwt_handler import create_jwt_token, decode_jwt_token
from datetime import datetime, timedelta


@pytest.fixture
def fixed_datetime():
    return datetime(2022, 1, 1, 12, 0, 0)


@patch("app.jwt_handler.datetime")
@patch("app.jwt_handler.jwt.encode")
def test_create_jwt_token(mock_encode, mock_datetime, fixed_datetime):
    # Set the fixed datetime for testing
    mock_datetime.utcnow.return_value = fixed_datetime

    # Define test data
    data = {"sub": "test_user"}
    expires_delta = timedelta(minutes=15)

    # Expected token
    expected_token = "example_token"

    # Mock jwt.encode to return the expected token
    mock_encode.return_value = expected_token

    # Call the function
    result = create_jwt_token(data, expires_delta)

    # Ensure jwt.encode was called with the correct arguments
    mock_encode.assert_called_once_with(
        {"sub": "test_user", "exp": fixed_datetime + expires_delta},
        "test_secret_key",
        algorithm="HS256",
    )

    # Ensure the function returns the expected token
    assert result == expected_token


@patch("app.jwt_handler.jwt.decode")
def test_decode_jwt_token(mock_decode):
    # Define a test token
    test_token = "example_token"

    # Mock jwt.decode to return the decoded data
    mock_decode.return_value = {"sub": "test_user"}

    # Call the function
    result = decode_jwt_token(test_token)

    # Ensure jwt.decode was called with the correct arguments
    mock_decode.assert_called_once_with(
        "example_token", "test_secret_key", algorithms=["HS256"]
    )

    # Ensure the function returns the decoded data
    assert result == {"sub": "test_user"}
