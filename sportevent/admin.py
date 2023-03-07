"""Admin"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from sportevent.models import Athlete, Event, Distance, ResultEvent
from sportevent.common.admin import BaseAdmin


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


@admin.register(Distance)
class DistanceAdmin(BaseAdmin):
    """ Admin interface for adding distances """
    list_display = ("title", "distance_in_unit", "event",)
    list_filter = ("event",)
    search_fields = ("title", "event",)
    fieldsets = (
                    (_("Деталі дистанції"),
                     {"fields": (
                         "title",
                         "distance_in_unit",
                         "event",
                         "athlete",
                     )}),
                ) + BaseAdmin.fieldsets


@admin.register(Event)
class EventAdmin(BaseAdmin):
    """ Admin interface for sports event """
    list_display = ("title", "date_event", "location",)
    list_filter = ("date_event",)
    search_fields = ("title", "location",)
    fieldsets = (
                    (_("Інформація спорт заходу"),
                     {"fields": (
                         "title",
                         "date_event",
                         "location",
                         "description",
                     )}),
                ) + BaseAdmin.fieldsets


@admin.register(ResultEvent)
class ResultEventAdmin(BaseAdmin):
    """ Admin interface for results """
    fieldsets = (
                    (_("Інформація спорт заходу"),
                     {"fields": ("event", "athlete", "result_time",)}),
                ) + BaseAdmin.fieldsets
