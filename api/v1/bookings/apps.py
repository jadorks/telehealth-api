from django.apps import AppConfig


class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.v1.bookings'

    def ready(self) -> None:
        import api.v1.bookings.signals