
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mainpages.forms import StaticPageAdminForm
from mainpages.models import StaticPage
from mainpages.common.admin import BaseAdmin


@admin.register(StaticPage)
class StaticPageAdmin(BaseAdmin):
    """Static page admin"""
    list_display = ("title", "url",)
    form = StaticPageAdminForm
    fieldsets = (
                    (_("Detail page"),
                     {"fields": ("title", "url", "content",)}),
                ) + BaseAdmin.fieldsets
