from enum import Enum

from pydantic import BaseModel, PositiveInt, PositiveFloat


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


LIST_ORDER_STATUS = dict[str, list[Order] | Status]