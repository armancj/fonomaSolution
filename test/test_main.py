import unittest

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

orders = [
    {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
    {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
    {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
    {"id": 4, "item": "Mouse", "quantity": 4, "price": 15.99, "status": "canceled"},
    {"id": 5, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"},
    {"id": 6, "item": "Mouse", "quantity": 4, "price": 50.99, "status": "completed"},
]


class MyTestCase(pytest.TestCase):

    @staticmethod
    @pytest.mark.asyncio
    def test_read_root():
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}  # add assertion here# add assertion here

    @staticmethod
    @pytest.mark.asyncio
    def test_read_say_hello():
        name = "test"
        response = client.get(f"/hello/{name}")
        assert response.status_code == 200
        assert response.json() == {"message": f"Hello {name}"}

    @staticmethod
    @pytest.mark.asyncio
    def test_process_orders():
        url = "/solution/?criterion=completed"
        response = client.post(url, json=orders)
        assert response.status_code == 200
        assert response.json() == 1150.88


if __name__ == '__main__':
    pytest.main()
