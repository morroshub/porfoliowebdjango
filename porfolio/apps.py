from django.apps import AppConfig
from . import views

class PorfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'porfolio'
