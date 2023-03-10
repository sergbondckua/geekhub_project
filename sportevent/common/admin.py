from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class BaseAdmin(admin.ModelAdmin):
    """Базовий клас зоготовка"""

    readonly_fields = ("id", "created_at", "updated_at",)
    fieldsets = (
        (_("Інфо запису"),
         {"fields": (
             "created_at",
             "updated_at",
         )}),
    )
