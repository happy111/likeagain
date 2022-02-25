"""
WSGI config for likeagain project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'likeagain.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
 'http' : get_asgi_application(),
 
})