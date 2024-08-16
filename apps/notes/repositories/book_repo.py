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
