from mongoengine import Document, EmailField, StringField, DateTimeField
from django.utils import timezone

class Users(Document):
    email = EmailField(required=True, unique=True)
    password = StringField(max_length=128, required=True)
    name = StringField(max_length=30, required=True)
    created_at = DateTimeField(default=timezone.now)
    updated_at = DateTimeField(default=timezone.now)

