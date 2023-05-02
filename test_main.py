from fastapi.testclient import TestClient
from pydantic import Json

from main import app
from model.order import Status

client = TestClient(app)

process_orders = {
    "orders": [
        {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
        {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
        {"id": 6, "item": "Mouse", "quantity": 4, "price": 50.99, "status": "completed"},
    ], "criterion": "completed"}

orders: Json = {[
    {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "Status.completed"},
    {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": Status.pending},
    {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": Status.completed},
    {"id": 4, "item": "Mouse", "quantity": 4, "price": 15.99, "status": Status.canceled},
    {"id": 5, "item": "Mouse", "quantity": 4, "price": 24.99, "status": Status.canceled},
    {"id": 6, "item": "Mouse", "quantity": 4, "price": 50.99, "status": Status.completed},
]}


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}  # add assertion here


def test_read_say_hello():
    name = "test"
    response = client.get(f"/hello/{name}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {name}"}


def test_process_orders():
    response = client.post("/solution?criterion=completed", json=orders)
    assert response.status_code == 200
    assert response.json() == process_orders
