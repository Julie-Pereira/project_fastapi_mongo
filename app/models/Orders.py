from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from bson.objectid import ObjectId


class Orders(BaseModel):
    id: ObjectId = Field(alias='_id')
    name: str
    firstname: str
    # date: datetime = Field(default_factory=datetime.utcnow)
    dish: str
    number: int

    class Config:
        schema_extra = {
            "example": {
                "name": "pereira",
                "firstname": "julie",
                "dish": "Pizza test",
                "number": 2,
            }
        }