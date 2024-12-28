from asgiref.sync import async_to_sync
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
import secrets
import json
from django.views.generic import View
from channels.consumer import get_channel_layer
from .utils import tg_auth

from DjangoProj.settings import tg_url

class TGConnectionView(View):

    def get(self, request):
        token = secrets.token_hex(5)
        context = {"connect_url": f'{tg_url}?start={token}', 'token': token}
        return render(request, "telegram_interaction/telegram_connect.html", context=context)

    def post(self, request):
        data = json.loads(request.body)
        async_to_sync(get_channel_layer().group_send)(
            data['token'], {"type": "tg.message",
                            "message": {'username': data['user'], 'token': data['token']}
                            }
        )
        return HttpResponse()

def login_tg_user(request):
    username, password = request.POST['username'], request.POST['password']
    user = tg_auth(username, password)
    if user:
        login(request, user)
    return redirect('connect')

def logout_tg_user(request):
    logout(request)
    return redirect('connect')


