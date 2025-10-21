from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import random

app = FastAPI(
    title="FastAPI CI/CD Demo",
    description="Simple FastAPI app showcasing CI/CD deployment with GET, POST, PUT, DELETE endpoints.",
    version="1.1.0"
)

# --- Models ---
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    quantity: int

# Mock in-memory store
items_db = {}

# --- Endpoints ---

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI CI/CD Demo!", "timestamp": datetime.utcnow()}

@app.get("/healthz")
def health_check():
    """Health check endpoint for CI/CD smoke tests."""
    return {"status": "healthy", "timestamp": datetime.utcnow()}

@app.get("/items")
def list_items():
    """List all items."""
    return {"items": list(items_db.values()), "count": len(items_db)}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Retrieve a single item by ID."""
    item = items_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": item, "timestamp": datetime.utcnow()}

@app.post("/items")
def create_item(item: Item):
    """Create a new item."""
    item_id = len(items_db) + 1
    items_db[item_id] = item.dict()
    return {"message": "Item created", "item_id": item_id, "timestamp": datetime.utcnow()}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Update an existing item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item.dict()
    return {"message": "Item updated", "item_id": item_id, "timestamp": datetime.utcnow()}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted = items_db.pop(item_id)
    return {"message": "Item deleted", "deleted": deleted, "timestamp": datetime.utcnow()}

@app.get("/random")
def get_random_number():
    """Simple random number generator for testing variability."""
    return {"random_number": random.randint(1, 100), "timestamp": datetime.utcnow()}

@app.get("/echo/{text}")
def echo_text(text: str):
    """Echo back any text."""
    return {"echo": text, "timestamp": datetime.utcnow()}

@app.get("/status")
def service_status():
    """Returns metadata about the service."""
    return {
        "service": "FastAPI CI/CD Demo",
        "version": "1.1.0",
        "status": "running",
        "region": "europe-west1",
        "timestamp": datetime.utcnow()
    }

print("DEPLOY TEST 1 🚀")