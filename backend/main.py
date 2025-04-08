from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    app.mongodb_client = AsyncIOMotorClient(mongo_uri)
    app.mongodb = app.mongodb_client["mydatabase"]

@app.get("/api/hello")
async def say_hello():
    return {"message": "Hello from FastAPI"}
