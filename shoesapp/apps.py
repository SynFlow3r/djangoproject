# apps.py
from django.apps import AppConfig

class ShoesappConfig(AppConfig):
    name = 'shoesapp'

    def ready(self):
        import shoesapp.signals
