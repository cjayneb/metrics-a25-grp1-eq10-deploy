import pytest
from src.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_issues_integration(client):
    response = client.get("/issues")

    data = response.json

    assert response.status_code == 200
    assert isinstance(data, list)
    if data:
        assert "id" in data[0]
        assert "title" in data[0]
        assert "state" in data[0]
        assert "user" in data[0]
        assert "assignees" in data[0]
        assert "labels" in data[0]
        assert "milestone" in data[0]
        assert "created_at" in data[0]
        assert "updated_at" in data[0]
        assert "closed_at" in data[0]
