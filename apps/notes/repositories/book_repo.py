from bson import ObjectId

from utils import get_collection_handle

collection_name = "books"
db = get_collection_handle(collection_name)


def create_book_in_db(book):
    book_data = db.insert_one(book)

    return book_data


def get_all_books_by_user_id(id):
    pipeline = [
        {"$match": {"user_id": id}},
        {"$addFields": {"id": {"$toString": "$_id"}}},
        {"$project": {"_id": 0}},
    ]

    books = list(db.aggregate(pipeline))

    return books


def delete_book_by_id_repo(bookId):
    response = db.delete_one({"_id": ObjectId(bookId)})

    result = (
        {"error": "No such note found"}
        if response.deleted_count == 0
        else {"success": True}
    )

    return result


def update_book_name_repo(bookId, name):
    response = db.update_one({"_id": ObjectId(bookId)}, {"$set": {"title": name}})

    return response
