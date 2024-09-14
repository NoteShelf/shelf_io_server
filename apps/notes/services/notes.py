from django.utils import timezone

from ..repositories.note_repo import (
    create_note_repo,
    get_notes_by_book_id,
    update_note_repo,
    delete_note_by_id_repo,
)


def update_note_service(note_data):
    try:
        updated_note = update_note_repo(
            note_data["id"], note_data["title"], note_data["content"], timezone.now()
        )

        if hasattr(updated_note, "upserted_id"):
            return {"success": True}
        else:
            return {"error": "Failed to update note"}

    except Exception as e:
        return {"error": "An unexpected error occurred: " + str(e)}


def create_note_service(note_data, user_info):
    try:
        if not note_data["title"]:
            note_data["title"] = "Untitled"

        note_data["user_id"] = user_info["id"]
        note_data["shelf_id"] = None
        note_data["created_at"] = timezone.now()
        note_data["updated_at"] = timezone.now()

        note_details = create_note_repo(note_data)

        if hasattr(note_details, "inserted_id"):
            return {"success": True, "id": str(note_details.inserted_id)}
        else:
            return {"error": "Failed to create book"}
    except Exception as e:
        return {"error": "An unexpected error occurred: " + str(e)}


def get_all_notes_by_id(book_id):
    try:
        all_notes = get_notes_by_book_id(book_id)
        return all_notes
    except Exception as e:
        return {"error": str(e)}


def delete_note_by_id_service(note_id):
    try:
        result = delete_note_by_id_repo(note_id)
        return result
    except Exception as e:
        return {"error": str(e)}
