import json
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime
from time import sleep
from channels.exceptions import StopConsumer
from .models import Task, Test
from django.forms.models import model_to_dict


class ws_consumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def connect(self):
        print(self.scope['url_route'])
        print('!!!Connected!!!')
        self.accept()
        # self.timer()

    def websocket_disconnect(self, close_code):
        print('!!!Disconnect!!!')
        self.close()
        raise StopConsumer()

    def websocket_receive(self, text_data=None, bytes_data=None):
        print(Test.objects.all())
        new_spisok = {}
        for k in Test.objects.all():
            k = model_to_dict(k)
            print(k)
            k = k['text']

       # print(testlist)
            self.send(json.dumps({'random': k}))
        sleep(1)
        print('!!received!!!', text_data['text'])

    def timer(self):
        self.timer_start()

    def timer_start(self):
        while True:
            now = datetime.now()
            self.send(json.dumps({'timeValue': now.strftime("%H:%M:%S")}))
            sleep(1)
