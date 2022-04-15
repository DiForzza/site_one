import json
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime
from time import sleep
from channels.exceptions import StopConsumer


class ws_consumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def connect(self):
        print('!!!Connected!!!')
        self.accept()
        # self.timer()

    def disconnect(self, close_code):
        print('!!!Disconnect!!!')
        self.close()
        raise StopConsumer()

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message, text_data, bytes_data)

    def timer(self):
        self.timer_start()

    def timer_start(self):
        while True:
            now = datetime.now()
            self.send(json.dumps({'timeValue': now.strftime("%H:%M:%S")}))
            sleep(1)
