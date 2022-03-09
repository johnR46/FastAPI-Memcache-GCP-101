from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_find_all():
    response = client.get("/api/v1/todo/find/all")
    assert response.status_code == 200


def test_get_find_by_id():
    response = client.get("/api/v1/todo/find/2")
    assert response.status_code == 200
