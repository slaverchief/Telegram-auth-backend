
from .views import *
from django.urls import path

urlpatterns = [
    path('connect', TGConnectionView.as_view(), name='tg_connect'),
    path('login', login_tg_user, name='tg_login'),
    path('logout', logout_tg_user, name='tg_logout')
]
