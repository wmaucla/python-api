import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture()
def mock_env():
    with TestClient(app) as test_client:
        yield test_client
