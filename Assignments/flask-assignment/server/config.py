from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/flask")

def get_db():
    client = MongoClient(MONGO_URI)
    return client.get_database()
