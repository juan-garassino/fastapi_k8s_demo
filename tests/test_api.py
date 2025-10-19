from fastapi.testclient import TestClient
from src.app.main import app  # adjust to your actual import path

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "timestamp" in data
    assert data["message"].startswith("Welcome to FastAPI")

def test_read_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    data = response.json()
    assert "item" in data or "item_id" in data or "timestamp" in data

def test_healthz_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
