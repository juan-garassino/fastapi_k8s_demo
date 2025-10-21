from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data

def test_create_and_read_item():
    # First create an item
    new_item = {"name": "Test", "description": "For testing", "price": 10.0, "quantity": 1}
    post_response = client.post("/items", json=new_item)
    assert post_response.status_code == 200
    item_id = post_response.json()["item_id"]

    # Then read the item
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert "item" in data
    assert data["item"]["name"] == "Test"

def test_healthz_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
