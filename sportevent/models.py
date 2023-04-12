"""Models"""

from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from profiles.models import Athlete
from sportevent.common.models import BaseModel
from sportevent.service import generate_path


class Event(BaseModel):
    """ Sports event """

    title = models.CharField(_("Назва"), max_length=100)
    date_event = models.DateField(_("Дата проведення"))
    registration_end_date = models.DateTimeField(
        _("Registration end date"),
        default=None,
        help_text=_("Enter the end date of registration for the event"),
    )
    location = models.CharField(_("Місце проведення"), max_length=200)
    description = models.TextField(_("Опис"), blank=True, null=True)
    poster = models.ImageField(
        _("Постер"),
        blank=True,
        null=True,
        upload_to=generate_path,
        default=None,
        help_text=_("Завантажити зображення: (PNG, JPEG, JPG)"),
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-date_event",)
        verbose_name = _("Спортивний захід")
        verbose_name_plural = _("Спортивні заходи")


class Distance(BaseModel):
    """ Distance """
    title = models.CharField(_("Назва"), max_length=50)
    distance_in_unit = models.PositiveSmallIntegerField(_("Дистанція"))
    description = models.TextField(_("Description"), blank=True, null=True)
    road_map = models.TextField(_("Road map"), blank=True, null=True)
    event = models.ForeignKey(
        Event,
        verbose_name=_("Спорт захід"),
        related_name="distances",
        on_delete=models.CASCADE,
    )
    road_map_image = models.ImageField(
        _("Road map image"),
        blank=True,
        null=True,
        upload_to=generate_path,
        help_text=_("Download image: (PNG, JPEG, JPG)"),
    )

    def __str__(self) -> str:
        return f"{self.event} -- {self.title}: {self.distance_in_unit}"

    class Meta:
        ordering = ("-distance_in_unit",)
        verbose_name = _("Дистанція")
        verbose_name_plural = _("Дистанції")


class RegisterDistanceAthlete(BaseModel):
    """ Registered athletes for the distance """
    distance = models.ForeignKey(
        Distance,
        verbose_name=_("Дистанція"),
        on_delete=models.CASCADE,
        related_name="registered_distance",
    )
    athlete = models.ForeignKey(
        Athlete,
        verbose_name=_("Атлети"),
        on_delete=models.CASCADE,
        related_name="registered_distance",
        blank=True,
        null=True,
    )
    start_number = models.PositiveSmallIntegerField(
        verbose_name=_("Номер учасника"),
        unique=False,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if timezone.now().replace(microsecond=0) > \
                self.distance.event.registration_end_date.replace(
                    microsecond=0):
            raise ValueError(
                'Registration date is outside of the allowed period')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.athlete.first_name} {self.athlete.last_name} - " \
               f"{self.distance.event.title} " \
               f"({self.distance.distance_in_unit}): {self.start_number}"

    class Meta:
        ordering = ("start_number",)
        verbose_name = _("Атлета на дистанцію")
        verbose_name_plural = _("Зареєстровані атлети на дистанції")


class ResultEvent(BaseModel):
    """ Results of the event """
    athlete = models.ForeignKey(
        RegisterDistanceAthlete,
        verbose_name=_("Атлет"),
        on_delete=models.SET_NULL,
        related_name="results",
        null=True,
    )
    result_time = models.DurationField(
        verbose_name=_("Час результату"),
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.athlete.athlete.first_name} " \
               f"{self.athlete.athlete.last_name} - " \
               f"{self.athlete.distance.event.title} - " \
               f"{self.athlete.distance.title} - " \
               f"{self.athlete.distance.distance_in_unit}: {self.result_time}"

    class Meta:
        ordering = ("-result_time",)
        verbose_name = _("Результат атлета на дистанції")
        verbose_name_plural = _("Результати атлетів на дистанції")
