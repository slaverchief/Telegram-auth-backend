import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer



class TelegramConnectionConsumer(WebsocketConsumer):

    def connect(self):
        self.sid = self.scope["url_route"]["kwargs"]["id"] # идентификация вебсокета через группы
        async_to_sync(self.channel_layer.group_add)(
            self.sid, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.sid, self.channel_name
        )

    def tg_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"message": message}))
