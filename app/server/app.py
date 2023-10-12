from fastapi import FastAPI

from app.server.database import (orders_collection)
from app.server.models import (Order)
from app.server.rules import router

app = FastAPI()

app.include_router(router)


@app.get("/")
async def root():
    return 'Hello'


@app.get("/create_order")
async def create_order():
    order = await orders_collection.insert_one({
                "name": "pereira",
                "firstname": "julie",
                "dish": "Pizza test",
                "number": 2,
            })
    new_order = await orders_collection.find_one({"_id": order.id})
    return Order(new_order)