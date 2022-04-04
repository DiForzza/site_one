# Импортировать модуль JSON
import json
# Импортировать WebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
# Импортировать модуль datetime
from datetime import datetime
# Импортировать модуль sleep
from time import sleep


# Определить класс потребителя для отправки данных через
class ws_consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        while True:
            now = datetime.now()
            self.send(json.dumps({'timeValue': now.strftime("%H:%M:%S")}))
            sleep(1)

    def disconnect(self, code):
        self.disconnect(code)
