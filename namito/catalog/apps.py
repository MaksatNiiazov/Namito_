from django.apps import AppConfig


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'namito.catalog'

    def ready(self):
        import namito.catalog.signals

