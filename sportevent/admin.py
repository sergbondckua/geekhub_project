"""Admin"""
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from sportevent.models import Event
from sportevent.models import Distance
from sportevent.models import ResultEvent
from sportevent.models import RegisterDistanceAthlete
from sportevent.forms import EventAdminForm, DistanceAdminForm

from sportevent.common.admin import BaseAdmin


class RegisterDistanceAthleteInLine(admin.TabularInline):
    """Athlete in line to Distance"""
    model = RegisterDistanceAthlete
    extra = 1


class ResultEventInline(admin.TabularInline):
    model = ResultEvent
    extra = 1


@admin.register(Distance)
class DistanceAdmin(BaseAdmin):
    """ Admin interface for adding distances """
    list_display = ("title", "distance_in_unit", "event",)
    list_filter = ("event",)
    search_fields = ("title",)
    inlines = [RegisterDistanceAthleteInLine]
    save_on_top = True
    form = DistanceAdminForm
    fieldsets = (
                    (_("Distance details"),
                     {"fields": (
                         "id",
                         "event",
                         "title",
                         "distance_in_unit",
                         "description",
                         "road_map",
                         "road_map_image",
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
    form = EventAdminForm
    fieldsets = (
                    (_("Event information"),
                     {"fields": (
                         "title",
                         "date_event",
                         "registration_end_date",
                         "location",
                         "description",
                         ("poster", "get_image",),
                     )}),
                ) + BaseAdmin.fieldsets

    def get_image(self, obj):
        """View image for admin"""
        if obj.poster:
            return mark_safe(
                f'<img src={obj.poster.url} width="120" height="100"')
        return None

    get_image.short_description = "Thumbs"


@admin.register(ResultEvent)
class ResultEventAdmin(BaseAdmin):
    """ Admin interface for results """
    list_filter = ("athlete",)
    list_display = ("athlete", "result_time",)
    list_editable = ("result_time",)
    fieldsets = (
                    (_("Event information"),
                     {"fields": ("athlete", "result_time",)}),
                ) + BaseAdmin.fieldsets


@admin.register(RegisterDistanceAthlete)
class RegisterDistanceAthleteAdmin(BaseAdmin):
    """ Admin interface for registering distances """
    list_display = ("start_number", "athlete", "distance", "result_time",)
    readonly_fields = BaseAdmin.readonly_fields + ("start_number", "athlete", "distance",)
    list_filter = ("distance", "athlete",)
    search_fields = ("start_number",)
    inlines = [ResultEventInline]
    fieldsets = (
                    (_("Registration details"),
                     {"fields": (
                         "distance",
                         "start_number",
                         "athlete",
                     )}),
                ) + BaseAdmin.fieldsets

    def result_time(self, obj):
        for res in obj.results.all():
            return res.result_time if res.result_time else None

    result_time.short_description = _("Result")


admin.site.site_title = "CrossRunChe manager"
admin.site.site_header = "CrossRunChe manager"
