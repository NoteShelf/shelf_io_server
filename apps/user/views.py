from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .services.auth_service import authenticate_user

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        tokens = authenticate_user(email, password)
        return Response(tokens, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
