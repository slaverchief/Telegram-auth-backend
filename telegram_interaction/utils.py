from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def tg_auth(username, password_filling):
    try:
        user = User.objects.get(username=username)
        user.set_password(password_filling)
        user.save()
    except ObjectDoesNotExist:
        user = User.objects.create_user(username=username, password=password_filling)
    return authenticate(username=username, password=password_filling)



