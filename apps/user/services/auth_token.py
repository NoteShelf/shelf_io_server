import jwt
import datetime
import environ

env = environ.Env()


def create_access_token(user):
    issued_at = datetime.datetime.utcnow()
    expiration_time = issued_at + datetime.timedelta(hours=1)

    payload = {
        "id": str(user.get("_id")),
        "name": user.get("name"),
        "email": user.get("email"),
        "iat": issued_at,
        "exp": expiration_time,
    }

    token = jwt.encode(payload, env("SECRET_KEY"), algorithm="HS256")

    return str(token)


def generate_token(user):
    return {"token": create_access_token(user)}
