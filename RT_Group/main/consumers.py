import json
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime
from time import sleep
from channels.exceptions import StopConsumer
from .models import Task, Test
from django.forms.models import model_to_dict
from django.db import connection
from django.core.management.color import no_style


def sql_sort():
    sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Test])
    with connection.cursor() as cursor:
        for sql in sequence_sql:
            cursor.execute(sql)


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
        # print(Test.objects.all())
        print(text_data)
        if len(Test.objects.all()) > 10:
            print(Test.objects.filter(id=0))
            delete = Test.objects.all()[0]
            delete.delete()
            sql_sort()
            #Test.objects.filter(id=list(Test.objects.values_list('id', flat=True)[:1]))
            #delete = Test.objects.all()[:1]
            #delete.delete()
        new_dict = {}
        for k in Test.objects.all():
            k = model_to_dict(k)
            key = k['id']
            value = k['text']
            new_dict[key] = value

       # print(testlist)
        self.send(json.dumps({'random': new_dict}))
        sleep(1)
        print('!!received!!!', len(Test.objects.all()))

    def timer(self):
        self.timer_start()

    def timer_start(self):
        while True:
            now = datetime.now()
            self.send(json.dumps({'timeValue': now.strftime("%H:%M:%S")}))
            sleep(1)
