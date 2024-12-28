
from .views import *
from django.urls import path

urlpatterns = [
    path('connect', TGConnectionView.as_view(), name='connect'),
    path('login', login_tg_user, name='login'),
    path('logout', logout_tg_user, name='logout')
]
