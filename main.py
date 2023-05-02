from typing import List

from aiocache import cached, Cache
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model.order import Order, Status, LIST_ORDER_STATUS

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["App"])
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}", tags=["App"])
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("solution", tags=["Solution"])
@cached(ttl=3600, cache=Cache.REDIS, endpoint="localhost", port="6379")
async def process_orders(orders: List[Order], criterion: Status) -> LIST_ORDER_STATUS:
    filtered_orders = []
    for order in orders:
        if (order.status == criterion) or (criterion == Status.all):
            filtered_orders.append(order)
    return {"orders": filtered_orders, "criterion": criterion}

