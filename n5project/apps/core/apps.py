from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'n5project.apps.core'

    def ready(self):
        from .permissions import Group
