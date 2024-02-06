import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

# Ensure DJANGO_SETTINGS_MODULE is set properly based on your project name!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstdjango.settings.local")

# Fetch ASGI application before importing dependencies that require ORM models.
django_asgi_app = get_asgi_application()
