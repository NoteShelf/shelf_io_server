from utils import get_collection_handle
from pymongo.errors import PyMongoError, DuplicateKeyError

collection_name = "users"
collection = get_collection_handle(collection_name)
collection.create_index([("email", 1)], unique=True)


def create_user(user_details):
    try:
        result = collection.insert_one(user_details)
        return {
            "user_id": result.inserted_id,
        }

    except DuplicateKeyError as e:
        return {"error": "Sorry email already exists"}

    except PyMongoError as e:
        print(f"Failed to create user error: {e}")
        return {"error": "Failed to created user " + str(e)}


def get_user_by_email(email):
    try:
        user = collection.find_one({"email": email})
        return user

    except PyMongoError as e:
        print(f"MongoDB query error: {e}")
        return None
