from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services.book import (
    create_book_service,
    get_all_books_service,
    delete_book_by_id_service,
    update_book_name_service,
)
from .services.notes import (
    create_note_service,
    get_all_notes_by_id,
    update_note_service,
    delete_note_by_id_service,
)


@api_view(["GET", "POST", "PUT", "DELETE"])
def book_view(request):

    if request.method == "GET":
        return get_all_books(request)
    elif request.method == "PUT":
        return update_book_name_view(request)
    elif request.method == "POST":
        return create_book_view(request)
    elif request.method == "DELETE":
        return delete_note_or_book(request, True)


def create_book_view(request):
    book_data = request.data
    user_info = getattr(request, "user_info", None)

    book = create_book_service(book_data, user_info)

    if book.get("success"):
        return Response(
            {"message": "Book created successfully", "id": book["id"]},
            status=status.HTTP_201_CREATED,
        )
    else:
        return Response(book, status=status.HTTP_400_BAD_REQUEST)


def get_all_books(request):
    user_info = request.user_info

    response = get_all_books_service(user_info["id"])

    if "error" in response:
        return Response(
            {"error": response["error"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    else:
        return Response(response, status=status.HTTP_200_OK)


def update_book_name_view(request):
    try:
        book_id = request.data["id"]
        book_name = request.data["title"]

        update_book_name_service(book_id, book_name)

        return Response({"success": True}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET", "POST", "PUT", "DELETE"])
def note_view(request):

    if request.method == "GET":
        return get_all_notes(request)

    elif request.method == "PUT":
        return update_note(request)

    elif request.method == "DELETE":
        return delete_note_or_book(request)

    elif request.method == "POST":
        return create_a_note(request)


def create_a_note(request):
    user_info = request.user_info
    book_data = request.data

    note = create_note_service(book_data, user_info)

    if note.get("success"):
        return Response(
            {"message": "Note created successfully", "id": note["id"]},
            status=status.HTTP_201_CREATED,
        )
    else:
        return Response(note, status=status.HTTP_400_BAD_REQUEST)


def get_all_notes(request):
    book_id = request.GET.get("id")

    response = get_all_notes_by_id(book_id)

    if "error" in response:
        return Response(
            {"error": response["error"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    else:
        return Response(response, status=status.HTTP_200_OK)


def update_note(request):
    response = update_note_service(request.data)

    if response.get("success"):
        return Response(
            {"message": "Note update successfully"},
            status=status.HTTP_201_CREATED,
        )
    else:
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


def delete_note_or_book(request, isBook=False):

    id = request.GET.get("id")

    response = None

    if isBook:
        response = delete_book_by_id_service(id)
    else:
        response = delete_note_by_id_service(id)

    if "error" in response:
        return Response(
            {"error": response["error"]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    else:
        return Response(response, status=status.HTTP_200_OK)
