from rest_framework_simplejwt.tokens import  AccessToken

def create_access_token(user):
    token  = AccessToken.for_user(user)

    payload = token.payload
    payload['email'] = user.email
    payload['name'] = user.name

    return str(token)


def generate_token(user):
    return {'token':create_access_token(user)}

