from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer

from .services.auth_service import authenticate_user, create_user_service


@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response(
            {"error": "Email and password are required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        tokens = authenticate_user(email, password)
        return Response(tokens, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)

    if serializer.is_valid():
        try:
            token = create_user_service(request.data)

            if token.get("error"):
                return Response(token, status=status.HTTP_400_BAD_REQUEST)

            return Response(token, status=status.HTTP_200_OK)

        except Exception as e:
            print("Registration api failed: " + str(e))

            return Response(
                {"error": "Something went wrong"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
