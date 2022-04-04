from django.urls import path
from.consumers import ws_consumer

# Задайте путь для вызова потребителя
ws_urlpatterns = [
    path('testpage/', ws_consumer.as_asgi())
]