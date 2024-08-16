from django.http import JsonResponse
from rest_framework import status
import jwt
import environ

env = environ.Env()


def bearer_token_middleware(get_response):
    def middleware(request):
        if request.path != "/login":
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                return JsonResponse(
                    {"error": "Authorization header missing"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            token = _get_token(auth_header)

            try:
                secret_key = env("SECRET_KEY")
                decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
                request.user_info = _get_user_from_token(decoded_token)

            except jwt.ExpiredSignatureError:
                return JsonResponse(
                    {"error": "Token has expired"}, status=status.HTTP_401_UNAUTHORIZED
                )

            except jwt.InvalidTokenError:
                return JsonResponse(
                    {"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
                )

            except Exception as e:
                return JsonResponse(
                    {"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED
                )

        return get_response(request)

    return middleware


def _get_token(auth_header):
    try:
        prefix, token = auth_header.split(" ")
        if prefix != "Bearer":
            raise ValueError("Invalid token prefix")
        return token

    except ValueError:
        raise JsonResponse(
            {"error": "Invalid token header"}, status=status.HTTP_401_UNAUTHORIZED
        )


def _get_user_from_token(decoded_token):
    user_info = {
        "id": decoded_token.get("id"),
        "name": decoded_token.get("name"),
        "email": decoded_token.get("email"),
    }

    return user_info
