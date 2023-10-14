from fastapi import FastAPI
from rules.order import orders_router

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return "Welcome to Julie's FastApi MongoDb CRUD test"

app.include_router(orders_router, tags=["Orders"], prefix="/order")
