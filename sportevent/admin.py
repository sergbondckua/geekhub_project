"""Admin"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from sportevent.models import Athlete
from sportevent.models import Event
from sportevent.models import Distance
from sportevent.models import ResultEvent
from sportevent.models import RegisterDistanceAthlete

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


class RegisterDistanceAthleteInLine(admin.TabularInline):
    """Athlete in line to Distance"""
    model = RegisterDistanceAthlete
    extra = 1


@admin.register(Distance)
class DistanceAdmin(BaseAdmin):
    """ Admin interface for adding distances """
    list_display = ("title", "distance_in_unit", "event",)
    list_filter = ("event",)
    search_fields = ("title",)
    inlines = [RegisterDistanceAthleteInLine]
    save_on_top = True
    fieldsets = (
                    (_("Деталі дистанції"),
                     {"fields": (
                         "id",
                         "title",
                         "distance_in_unit",
                         "event",
                     )}),
                ) + BaseAdmin.fieldsets


class DistanceInLine(admin.TabularInline):
    """Distance in line to Event"""
    model = Distance
    extra = 1


@admin.register(Event)
class EventAdmin(BaseAdmin):
    """ Admin interface for sports event """
    list_display = ("title", "date_event", "location", "get_image")
    list_filter = ("date_event",)
    search_fields = ("title", "location",)
    inlines = [DistanceInLine]
    readonly_fields = BaseAdmin.readonly_fields + ("get_image",)
    save_on_top = True
    save_as = True
    fieldsets = (
                    (_("Інформація спорт заходу"),
                     {"fields": (
                         "title",
                         "date_event",
                         "location",
                         "description",
                         ("poster", "get_image",),
                     )}),
                ) + BaseAdmin.fieldsets

    def get_image(self, obj):
        """View image for admin"""
        return mark_safe(f'<img src={obj.poster.url} width="120" height="100"')

    get_image.short_description = "Мініатюра"


@admin.register(RegisterDistanceAthlete)
class RegisterDistanceAthleteAdmin(BaseAdmin):
    """ Admin interface for registering distances """
    list_display = ("start_number", "athlete", "distance",)
    list_filter = ("distance", "athlete",)
    search_fields = ("start_number",)
    list_display_links = ("athlete",)
    fieldsets = (
                    (_("Деталі реєстрації"),
                     {"fields": (
                         "distance",
                         "start_number",
                         "athlete",
                     )}),
                ) + BaseAdmin.fieldsets


@admin.register(ResultEvent)
class ResultEventAdmin(BaseAdmin):
    """ Admin interface for results """
    fieldsets = (
                    (_("Інформація спорт заходу"),
                     {"fields": ("event", "athlete", "result_time",)}),
                ) + BaseAdmin.fieldsets


admin.site.site_title = "CrossRunChe manager"
admin.site.site_header = "CrossRunChe manager"
