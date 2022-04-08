import json
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime
from time import sleep
import time
from channels.exceptions import StopConsumer


class ws_consumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self._start_time = time.perf_counter()

    def connect(self):
        self.accept()
        self.timer()

    def disconnect(self, close_code):
        print('!!!Disconnect!!!')
        self.close()
        raise StopConsumer()

    def render(self):
        print('!!!render!!!')

    def receive(self, text_data=None, bytes_data=None):
        print('!!!receive!!!')

    def timer(self):
        start_time = True
        while start_time:
            now = datetime.now()
            self.send(json.dumps({'timeValue': now.strftime("%H:%M:%S")}))
            sleep(1)
            elapsed_time = time.perf_counter() - self._start_time
            print(elapsed_time)
            if elapsed_time > 20:
                start_time = False
                print('timer stopped')
