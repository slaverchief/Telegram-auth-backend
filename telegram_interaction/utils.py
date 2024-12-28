from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def tg_auth(username, password_filling):
    try:
        user = User.objects.get(username=username)
        user.set_password(password_filling)
        # так как авторизация через телеграм не предполагает использование пароля, а в условии сказано использовать встроенные механизмы авторизации
        # пароль на каждом акте авторизации заполняется токеном
        # идентификации вебсокета в качестве заглушки; тогда пользователь автоматически авторизовывается.
        user.save()
    except ObjectDoesNotExist:
        # если пользователя не существует, он создается с теми же данными как если бы пользователь авторизовывался
        user = User.objects.create_user(username=username, password=password_filling)
    return authenticate(username=username, password=password_filling)



