"""Models"""
import os
import random

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from profiles.models import Athlete
from sportevent.common.models import BaseModel


class Event(BaseModel):
    """ Sports event """

    def generate_path(self, filename):
        """ Generates path and filename to save """
        ext = filename.rsplit(".", 1)[-1]
        result = f"event/posters/poster_event_" \
                 f"{random.randint(1, 999)}_{self.date_event}.{ext}"
        path = os.path.join(settings.MEDIA_ROOT, result)
        if os.path.exists(path):
            os.remove(path)
        return result

    title = models.CharField(_("Назва"), max_length=100)
    date_event = models.DateField(_("Дата проведення"))
    location = models.CharField(_("Місце проведення"), max_length=200)
    description = models.TextField(_("Опис"), blank=True)
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
    event = models.ForeignKey(
        Event,
        verbose_name=_("Спорт захід"),
        related_name="distances",
        on_delete=models.CASCADE,
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
        # TODO: make this set default
        on_delete=models.CASCADE,
        related_name="results",
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
