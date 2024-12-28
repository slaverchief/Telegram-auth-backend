from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/tgcon/(?P<id>\w+)/$", consumers.TelegramConnectionConsumer.as_asgi()),
]