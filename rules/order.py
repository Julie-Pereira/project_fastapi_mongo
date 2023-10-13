from fastapi import FastAPI, Body
from database.database import orders_collection
from models.orders import (Order)
from fastapi import APIRouter
from bson.objectid import ObjectId
from typing import Union
from fastapi.encoders import jsonable_encoder
import json

app = FastAPI()

orders_router = APIRouter()


@orders_router.get("/create_order/", response_model=Order)
async def create_order(order: Order = Body(...)) -> Order:
    order = jsonable_encoder(order)
    created_order = await orders_collection.insert_one(order)
    new_order = await orders_collection.find_one({"_id": created_order.inserted_id})
    return Order(**new_order)


@orders_router.get("/retrieve_order/{order_id}")
async def retrieve_order(order_id: str) -> Union[Order, str]:
    order = await orders_collection.find_one({"_id": ObjectId(order_id)})
    if order:
        return Order(**order)
    return 'No orders found'


@orders_router.get("/update_order/{order_id}/{data}")
async def update_order(order_id: str, data: str) -> Union[Order, str]:
    order = await orders_collection.find_one({"_id": ObjectId(order_id)})
    if order:
        updated_order = await orders_collection.update_one(
            {"_id": ObjectId(order_id)}, {"$set": json.loads(data)}
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
    return f'No order found, unable to delete'
