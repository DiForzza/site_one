# import os
#
# from django.core.asgi import get_asgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RT_Group.settings')
#
# application = get_asgi_application()


# Импортировать модуль os
import os
# Импортировать get_asgi_application для обработки протокола http
from django.core.asgi import get_asgi_application
# Import ProtocolTypeRouter и URLRouter для установки маршрутизации веб-сокетов
from channels.routing import ProtocolTypeRouter, URLRouter
# Import AuthMiddlewareStack для обработки веб-сокета
from channels.auth import AuthMiddlewareStack
# Импортировать маршрутизацию веб-сокетов
from main.routing import ws_urlpatterns

# Назначьте значение для DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RT_Group.settings')

# Определить переменные приложения для обработки HTTP и WebSocket
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})