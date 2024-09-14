from rest_framework.exceptions import AuthenticationFailed

from ..repositories.user_repo import get_user_by_email, create_user
from .auth_token import generate_token


def create_user_service(user_details):
    result = create_user(user_details)

    if result.get("error"):
        return result
    else:
        token = authenticate_user(
            user_details.get("email"), user_details.get("password")
        )

        return token


def authenticate_user(email, password):
    user_details = get_user_by_email(email)

    print(user_details)

    if user_details is None:
        raise AuthenticationFailed("User Not Found")

    if not password == user_details.get("password"):
        raise AuthenticationFailed("Incorrect username or password")

    token = generate_token(user_details)

    return token
