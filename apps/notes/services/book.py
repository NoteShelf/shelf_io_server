from django.utils import timezone

from ..repositories.book_repo import (
    create_book_in_db,
    get_all_books_by_user_id,
    delete_book_by_id_repo,
    update_book_name_repo,
)

from ..repositories.note_repo import delete_all_note_of_a_book


def create_book_service(book_details, user_info):
    try:
        if not book_details["title"]:
            book_details["title"] = "Untitled"

        book_details["user_id"] = user_info["id"]
        book_details["shelf_id"] = None
        book_details["created_at"] = timezone.now()
        book_details["updated_at"] = timezone.now()

        book_data = create_book_in_db(book_details)

        if hasattr(book_data, "inserted_id"):
            return {"success": True, "id": str(book_data.inserted_id)}
        else:
            return {"error": "Failed to create book"}
    except Exception as e:
        return {"error": "An unexpected error occurred: " + str(e)}


def get_all_books_service(user_id):
    try:
        all_books = get_all_books_by_user_id(user_id)
        return all_books
    except Exception as e:
        return {"error": str(e)}


def delete_book_by_id_service(book_id):
    try:
        result = delete_book_by_id_repo(book_id)
        delete_all_note_of_a_book(book_id)

        return result

    except Exception as e:
        return {"error": str(e)}


def update_book_name_service(book_id, book_name):

    result = update_book_name_repo(book_id, book_name)

    return result
