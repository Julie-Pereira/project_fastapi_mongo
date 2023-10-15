from typing import Union

from bson.objectid import ObjectId
from database.database import orders_collection
from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from models.orders import Order, UpdateOrder

app = FastAPI()

orders_router = APIRouter()


@orders_router.post("/create_order/{order}", response_model=Order)
async def create_order(data: Order) -> Order:
    order = jsonable_encoder(data)
    created_order = await orders_collection.insert_one(order)
    new_order = await orders_collection.find_one(
        {"_id": created_order.inserted_id}
    )
    return Order(**new_order)


@orders_router.get("/retrieve_order/{order_id}", response_model=Order)
async def retrieve_order(order_id: str) -> Union[Order, str]:
    order = await orders_collection.find_one({"_id": ObjectId(order_id)})
    if not order:
        raise HTTPException(status_code=404, detail='No orders found')
    return Order(**order)


@orders_router.post("/update_order/{order_id}/{order}", response_model=Order)
async def update_order(order_id: str, data: UpdateOrder) -> Union[Order, str]:

    order_resource = await orders_collection.find_one(
        {"_id": ObjectId(order_id)}
    )
    if not order_resource:
        raise HTTPException(
            status_code=404,
            detail=f'No order found with id {order_id}'
        )

    updated_order = await orders_collection.update_one(
        {"_id": ObjectId(order_id)}, {"$set": jsonable_encoder(data)}
    )
    if updated_order.modified_count == 1:
        return Order(
            **await orders_collection.find_one({"_id":  ObjectId(order_id)})
        )


@orders_router.get("/delete_order/{order_id}")
async def delete_order(order_id: str) -> str:
    order = await orders_collection.find_one({"_id": ObjectId(order_id)})
    if order:
        await orders_collection.delete_one({"_id": ObjectId(order_id)})
        return f'The order {order_id} was successfully deleted'
