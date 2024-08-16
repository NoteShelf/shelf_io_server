from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services.book import create_book, get_all_books_service


@api_view(["GET", "POST"])
def book_view(request):

    if request.method == "GET":
        return get_all_books(request)

    elif request.method == "POST":
        book_data = request.data
        user_info = getattr(request, "user_info", None)

        book = create_book(book_data, user_info)

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
