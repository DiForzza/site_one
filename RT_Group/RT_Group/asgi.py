import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from main.routing import ws_urlpatterns
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RT_Group.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),

        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(ws_urlpatterns)
            )
        ),
    }
)