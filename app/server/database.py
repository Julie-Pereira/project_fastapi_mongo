import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:8000"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.orders

orders_collection = database.get_collection("orders_collection")