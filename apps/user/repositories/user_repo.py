from apps.user.models import Users

def get_user_by_email(email):
    try:
        user = Users.objects.get(email=email)
        return user
    except Users.DoesNotExist:
        return None

