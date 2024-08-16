from pymongo import MongoClient
from pymongo.errors import PyMongoError
from django.conf import settings

db_handle = None


def get_db_handle():
    global db_handle

    try:
        client = MongoClient(settings.MONGO_URI)
        db_handle = client[settings.MONGO_DB_NAME]
        return db_handle

    except PyMongoError as e:
        print(f"MongoDB Connection Error: {e}")
        return None



get_db_handle()


def get_collection_handle(collection_name):

    if db_handle is not None:
        return db_handle[collection_name]
    else:
        print(f"Database handle not found for collection '{collection_name}'")
        return None
