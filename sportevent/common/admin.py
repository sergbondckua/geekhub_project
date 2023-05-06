""" Application for basic admin panel """
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class BaseAdmin(admin.ModelAdmin):
    """Basic model-workpiece"""

    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )
    fieldsets = (
        (
            _("Record info"),
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
