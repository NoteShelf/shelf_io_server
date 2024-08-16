from utils import get_collection_handle

collection_name = "notes"
db = get_collection_handle(collection_name)


def create_note_repo(note_details):
    note = db.insert_one(note_details)
    return note


def get_notes_by_book_id(id):
    pipeline = [
        {"$match": {"user_id": id}},
        {"$addFields": {"id": {"$toString": "$_id"}}},
        {"$project": {"_id": 0}},
    ]

    notes = list(db.aggregate(pipeline))
    return notes
