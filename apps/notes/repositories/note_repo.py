from bson import ObjectId

from utils import get_collection_handle

collection_name = "notes"
db = get_collection_handle(collection_name)


def update_note_repo(id, title, content, updatedAt):
    updated_note = db.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "title": title,
                "content": content,
                "updated_at": updatedAt,
            }
        },
    )

    return updated_note


def create_note_repo(note_details):
    note = db.insert_one(note_details)
    return note


def get_notes_by_book_id(id):
    pipeline = [
        {"$match": {"book_id": id}},
        {"$addFields": {"id": {"$toString": "$_id"}}},
        {"$project": {"_id": 0}},
    ]

    notes = list(db.aggregate(pipeline))
    return notes


def delete_note_by_id_repo(noteId):
    response = db.delete_one({"_id": ObjectId(noteId)})

    result = (
        {"error": "No such note found"}
        if response.deleted_count == 0
        else {"success": True}
    )

    return result


def delete_all_note_of_a_book(bookId):
    response = db.delete_many({"book_id": bookId})

    result = (
        {"error": "No such note found"}
        if response.deleted_count == 0
        else {"success": True}
    )

    return result
