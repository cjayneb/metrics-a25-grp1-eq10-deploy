from unittest.mock import MagicMock, patch
import pytest
from src.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    expected_json = {"message": "Kanban Metrics API is running"}

    response = client.get("/")

    assert response.status_code == 200
    assert response.json == expected_json

def test_swagger_yaml(client):
    expected_swagger_start = "openapi"
    expected_swagger_end = "format: date-time"

    response = client.get("/swagger.yaml")
    text = response.data.decode("utf-8").strip()

    assert response.status_code == 200
    assert text.startswith(expected_swagger_start)
    assert text.endswith(expected_swagger_end)

@patch("src.app.requests.get")
def test_get_issues_mocked(mock_get: MagicMock, client):
    expected_issues = [{"id": 1, "title": "Fake issue"}]
    mock_get.return_value.json.return_value = expected_issues

    response = client.get("/issues")

    assert response.status_code == 200
    assert response.json == expected_issues
    mock_get.assert_called_once()
