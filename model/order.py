from pydantic import BaseModel, PositiveInt, PositiveFloat
from enum import Enum
from typing import List


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
    status: Status = Status.completed


class OrdersResponse(BaseModel):
    orders: List[Order]
    criterion: Status
