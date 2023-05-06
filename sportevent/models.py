"""Models"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from profiles.models import Athlete
from sportevent.common.models import BaseModel
from sportevent.service import generate_path


class Event(BaseModel):
    """Sports event"""

    title = models.CharField(_("Title"), max_length=100)
    date_event = models.DateField(_("Date of the event"))
    registration_end_date = models.DateTimeField(
        _("Registration end date"),
        default=None,
        help_text=_("Enter the end date of registration for the event"),
    )
    location = models.CharField(_("Event location"), max_length=200)
    description = models.TextField(_("Description"), blank=True, null=True)
    poster = models.ImageField(
        _("Poster"),
        blank=True,
        null=True,
        upload_to=generate_path,
        default=None,
        help_text=_("Upload image: (PNG, JPEG, JPG)"),
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-date_event",)
        verbose_name = _("Sports event")
        verbose_name_plural = _("Sports events")


class Distance(BaseModel):
    """Distance"""

    title = models.CharField(_("Title"), max_length=50)
    distance_in_unit = models.PositiveSmallIntegerField(_("Distance"))
    description = models.TextField(_("Description"), blank=True, null=True)
    road_map = models.TextField(_("Road map"), blank=True, null=True)
    event = models.ForeignKey(
        Event,
        verbose_name=_("Sports event"),
        related_name="distances",
        on_delete=models.CASCADE,
    )
    road_map_image = models.ImageField(
        _("Road map image"),
        blank=True,
        null=True,
        upload_to=generate_path,
        help_text=_("Upload image: (PNG, JPEG, JPG)"),
    )

    def __str__(self) -> str:
        return f"{self.event} -- {self.title}: {self.distance_in_unit}"

    class Meta:
        ordering = ("-distance_in_unit",)
        verbose_name = _("Distance")
        verbose_name_plural = _("Distances")


class RegisterDistanceAthlete(BaseModel):
    """Registered athletes for the distance"""

    distance = models.ForeignKey(
        Distance,
        verbose_name=_("Distance"),
        on_delete=models.CASCADE,
        related_name="registered_distance",
    )
    athlete = models.ForeignKey(
        Athlete,
        verbose_name=_("Athletes"),
        on_delete=models.CASCADE,
        related_name="registered_distance",
        blank=True,
        null=True,
    )
    start_number = models.PositiveSmallIntegerField(
        verbose_name=_("Starting number"),
        unique=False,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return (
            f"{self.athlete.first_name} {self.athlete.last_name} - "
            f"{self.distance.event.title} "
            f"({self.distance.distance_in_unit}): {self.start_number}"
        )

    class Meta:
        ordering = ("start_number",)
        verbose_name = _("Athlete to distance")
        verbose_name_plural = _("Registered athletes to distance")


class ResultEvent(BaseModel):
    """Results of the event"""

    athlete = models.ForeignKey(
        RegisterDistanceAthlete,
        verbose_name=_("Athlete"),
        on_delete=models.SET_NULL,
        related_name="results",
        null=True,
    )
    result_time = models.DurationField(
        verbose_name=_("Result time"),
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return (
            f"{self.athlete.athlete.first_name} "
            f"{self.athlete.athlete.last_name} - "
            f"{self.athlete.distance.event.title} - "
            f"{self.athlete.distance.title} - "
            f"{self.athlete.distance.distance_in_unit}: {self.result_time}"
        )

    class Meta:
        ordering = ("-result_time",)
        verbose_name = _("Athlete results at the distance")
        verbose_name_plural = _("Athletes results at the distance")
