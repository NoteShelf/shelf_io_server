from django.utils import timezone

from ..repositories.book_repo import create_book_in_db, get_all_books_by_user_id


def create_book(book_details, user_info):
    try:

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
