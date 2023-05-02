from enum import Enum
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, PositiveInt, PositiveFloat

app = FastAPI()


@app.get("/", tags=["App"])
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}", tags=["App"])
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


class Status(Enum):
    completed = "completed"
    pending = "pending"
    canceled = "canceled"
    all = "all"


class Order(BaseModel):
    id: PositiveInt
    item: str
    quantity: PositiveInt
    price: PositiveFloat
    status: Status = Status.all


@app.post("solution", tags=["App"])
async def process_orders(orders: List[Order], criterion: Status):
    pass
