from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0m#%!j3^k#*recn6tz^7h&cy*uw3yc5-ctv8%ql%98o7v#+sz!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'https:/duckduckmorros.duckdns.org', '127.0.0.1', 'http://localhost:3000']
CSRF_TRUSTED_ORIGINS = ['https://duckduckmorros.duckdns.org'] # Permite entrar al adm



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Default DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Configuración para archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'porfolio/static')]

# MEDIA 
MEDIA_URL = '/media/'
MEDIAFILES_DIRS = [os.path.join(BASE_DIR, 'porfolio/media')]
