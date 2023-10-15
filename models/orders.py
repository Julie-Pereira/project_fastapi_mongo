import uuid
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

__all__ = [
    'Order',
    'UpdateOrder'
]


class Dish(str, Enum):
    pizza = "pizza"
    hamburger = "hamburger"
    salad = "salad"
    fish = "fish"


class Order(BaseModel):
    _id: str = Field(default_factory=uuid.uuid4, alias='_id')
    name: str
    firstname: str
    dish: Dish
    number: int

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "Pereira",
                "firstname": "Julie",
                "dish": "pizza",
                "number": 2,
            }
        }


class UpdateOrder(BaseModel):
    name: Optional[str]
    firstname: Optional[str]
    dish: Optional[Dish]
    number: Optional[int]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "Pereira",
                "firstname": "Julie",
                "dish": "pizza",
                "number": 3,
            }
        }
