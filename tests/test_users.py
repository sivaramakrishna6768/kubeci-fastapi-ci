from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_users_empty():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_user():
    new_user = {"id": 1, "name": "Alice", "email": "alice@example.com"}
    response = client.post("/users/", json=new_user)
    assert response.status_code == 200
    assert response.json() == new_user

def test_read_users_after_creation():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Alice", "email": "alice@example.com"}]
