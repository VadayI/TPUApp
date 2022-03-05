from django.apps import AppConfig
from django.db.models.signals import post_migrate


class CoordinationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coordination'

    def ready(self, **kwargs):
        from .signals import generate_groups, generate_regions, generate_voivodeships, generate_aplication_status

        post_migrate.connect(generate_groups, **kwargs)
        post_migrate.connect(generate_regions, **kwargs)
        post_migrate.connect(generate_voivodeships, **kwargs)
        post_migrate.connect(generate_aplication_status, **kwargs)