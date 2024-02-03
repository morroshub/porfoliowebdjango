"""
WSGI config for firstdjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys


sys.path.append('/home/morros/porfoliowebdjango/firstdjango')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstdjango.settings')


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
