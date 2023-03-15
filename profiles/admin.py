""" Admin profiles """
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from profiles.models import Athlete


@admin.register(Athlete)
class AthleteAdmin(UserAdmin):
    """ Адмін інтерфейс для атлетів """
    list_display = UserAdmin.list_display + (
        "date_of_birth", "gender", "city", "phone", "club",
    )
    list_filter = UserAdmin.list_filter + (
        "date_of_birth", "gender", "city", "phone", "club",
    )
    search_fields = UserAdmin.search_fields + (
        "city", "club", "emergency_contact_name",
    )
    fieldsets = UserAdmin.fieldsets + (
        (_("Додаткові дані"),
         {"fields": (
             "date_of_birth",
             "gender",
             "phone",
             "emergency_contact_name",
             "emergency_contact_phone",
             "city",
             "club",
         )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_("Додаткові дані"),
         {"fields": (
             "first_name",
             "last_name",
             "email",
             "date_of_birth",
             "gender",
             "phone",
             "emergency_contact_name",
             "emergency_contact_phone",
             "city",
             "club",
         )}),
    )
