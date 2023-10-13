import uuid
from pydantic import BaseModel, Field
from enum import Enum

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