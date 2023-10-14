from typing import Union

from bson.objectid import ObjectId
from database.database import orders_collection
from fastapi import APIRouter, FastAPI
from fastapi.encoders import jsonable_encoder
from models.orders import Order

app = FastAPI()

orders_router = APIRouter()


@orders_router.get("/create_order/", response_model=Order)
async def create_order(order: Order) -> Order:
    order = jsonable_encoder(order)
    created_order = await orders_collection.insert_one(order)
    new_order = await orders_collection.find_one(
        {"_id": created_order.inserted_id}
    )
    return Order(**new_order)


@orders_router.get("/retrieve_order/{order_id}")
async def retrieve_order(order_id: str) -> Union[Order, str]:
    order = await orders_collection.find_one({"_id": ObjectId(order_id)})
    if order:
        return Order(**order)
    return 'No orders found'


@orders_router.get("/update_order/{order_id}/{data}")
async def update_order(order_id: str, payload: Order) -> Union[Order, str]:
    payload = jsonable_encoder(payload)
    order = await orders_collection.find_one({"_id": ObjectId(order_id)})
    if order:
        updated_order = await orders_collection.update_one(
            {"_id": ObjectId(order_id)}, {"$set": payload}
        )
        if updated_order:
            return Order(**order)
        return 'Unable to delete order'


@orders_router.get("/delete_order/{order_id}")
async def delete_order(order_id: str) -> str:
    order = await orders_collection.find_one({"_id": ObjectId(order_id)})
    if order:
        await orders_collection.delete_one({"_id": ObjectId(order_id)})
        return f'The order {order_id} was successfully deleted'
    return 'No order found, unable to delete'
