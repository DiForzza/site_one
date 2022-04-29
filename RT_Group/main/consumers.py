import json
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime
from time import sleep
from channels.exceptions import StopConsumer
import random


class ws_consumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def websocket_connect(self, message):
        print('!!!Connected!!!')
        self.accept()
        # self.timer()

    def websocket_disconnect(self, close_code):
        print('!!!Disconnect!!!')
        self.close()
        raise StopConsumer()

    def websocket_receive(self, text_data=None, bytes_data=None):
        self.send(json.dumps({'random': random.randint(10, 20)}))
        sleep(1)
        print('!!received!!!', text_data['text'])

    def timer(self):
        self.timer_start()

    def timer_start(self):
        while True:
            now = datetime.now()
            self.send(json.dumps({'timeValue': now.strftime("%H:%M:%S")}))
            sleep(1)
