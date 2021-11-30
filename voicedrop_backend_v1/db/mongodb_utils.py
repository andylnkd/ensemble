import logging

from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db


async def connect_to_mongo():
    # logging.info("Connect to the database...")
    print("Connect to the database...")
    db.client = AsyncIOMotorClient(MONGODB_URL,
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    # logging.info("Successfully connected to the database")
    print("Successfully connected to the database")


async def close_mongo_connection():
    # logging.info("Close database connection...")
    print("Close database connection...")
    db.client.close()
    # logging.info("Database connection closed")
    print("Database connection closed")
