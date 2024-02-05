"""
WSGI config for firstdjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

#sys.path.append('/var/www/porfoliowebdjango/firstdjango')  # Ruta de tu proyecto Django
#sys.path.append('/var/www/porfoliowebdjango/venv/lib/python3.8/site-packages')  # Ruta del venv


from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstdjango.settings')
application = get_wsgi_application()

