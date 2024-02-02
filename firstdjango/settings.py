from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0m#%!j3^k#*recn6tz^7h&cy*uw3yc5-ctv8%ql%98o7v#+sz!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'https:/duckduckmorros.duckdns.org']
CSRF_TRUSTED_ORIGINS = ['https://duckduckmorros.duckdns.org'] # Permite entrar al adm

# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reactpy_django',
    'blog',
    'porfolio.apps.PorfolioConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'firstdjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'firstdjango.wsgi.application'

ASGI_APPLICATION = "firstdjango.asgi.application"


# # Django rest framework
# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.AllowAny',
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.SessionAuthentication',
#     ],
# }


# ReactPy config 

# https://reactive-python.github.io/reactpy-django/3.5.1/learn/add-reactpy-to-a-django-project/

REACTPY_CACHE = 'default'

# REACTPY_SESSION_MAX_AGE = 10

REACTPY_URL_PREFIX = "reactpy/"


# REACTPY_AUTH_BACKEND 	"django.contrib.auth.backends.ModelBackend" 	"example_project.auth.MyModelBackend" 	Dotted path to the Django authentication backend to use for ReactPy components. This is only needed if:
# 1. You are using AuthMiddlewareStack and...
# 2. You are using Django's AUTHENTICATION_BACKENDS setting and...
# 3. Your Django user model does not define a backend attribute.



# REACTPY_BACKHAUL_THREAD = "True"



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Default DB
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Deploy DB MYSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'porfolio',
        'USER': 'morros',
        'PASSWORD': 'polkKLOP: ',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'unix_socket': '/run/mysqld/mysqld.sock',
        },
    },
}





# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Configuración para archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'porfolio/static')]

# MEDIA 
MEDIA_URL = '/media/'
MEDIAFILES_DIRS = [os.path.join(BASE_DIR, 'porfolio/media')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
