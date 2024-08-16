from  utils import get_collection_handle
from pymongo.errors import PyMongoError

collection_name = "users"

def get_user_by_email(email):
    try:
        collection = get_collection_handle(collection_name)
        user = collection.find_one({"email": email})
        return user
    
    except  PyMongoError as e:
        print(f"MongoDB query error: {e}")
        return None

