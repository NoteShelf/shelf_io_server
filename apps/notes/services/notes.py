from django.utils import timezone

from ..repositories.note_repo import create_note_repo, get_notes_by_book_id


def create_note(note_data, user_info):
    try:
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
