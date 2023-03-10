from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SporteventConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sportevent"
    verbose_name = _("Спортивні заходи")

    def ready(self):
        import sportevent.signals
