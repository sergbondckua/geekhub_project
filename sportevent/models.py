"""Models"""
import os

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from sportevent.common.models import BaseModel


class Athlete(AbstractUser):
    """ Full-featured site user model """

    GENDER_CHOICES = [
        ("male", _("Чоловіча")),
        ("female", _("Жіноча")),
    ]

    date_of_birth = models.DateField(
        _("Дата народження"),
        blank=True,
        null=True
    )
    gender = models.CharField(
        _("Стать"),
        max_length=10,
        blank=True,
        choices=GENDER_CHOICES
    )
    phone = models.CharField(_("Номер телефону"), max_length=15, blank=True)
    emergency_contact_name = models.CharField(
        _("Ім'я екстреного контакту"),
        max_length=50,
        blank=True,
    )
    emergency_contact_phone = models.CharField(
        _("Номер телефону екстреного контакту"),
        max_length=15,
        blank=True,
    )
    city = models.CharField(_("Населений пункт"), max_length=100, blank=True)
    club = models.CharField(_("Спортивний клуб"), max_length=100, blank=True)

    def __str__(self):
        """ A string representation of an instance of a class """
        return f"{self.first_name} {self.last_name}: ({self.username})" \
            if self.first_name and self.last_name is not None else self.username

    class Meta:
        """ Meta class """
        ordering = ("username",)
        verbose_name = _("Атлета")
        verbose_name_plural = _("Атлети")


class Event(BaseModel):
    """ Sports event """

    def generate_path(self, filename):
        """ Generates path and filename to save """
        ext = filename.rsplit(".", 1)[-1]
        result = f"event/posters/poster_event_{self.id}_{self.date_event}.{ext}"
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
        """
        A string representation of an instance of a class
        """
        return self.title

    class Meta:
        """ Meta class for events """
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
        on_delete=models.CASCADE
    )
    athlete = models.ManyToManyField(
        Athlete,
        verbose_name=_("Атлети"),
        related_name="distances",
        blank=True
    )

    def __str__(self) -> str:
        """ A string representation of an instance of a class """
        return f"{self.event} -- {self.title}: {self.distance_in_unit}"

    class Meta:
        """Meta клас"""
        ordering = ("-created_at",)
        verbose_name = _("Дистанція")
        verbose_name_plural = _("Дистанції")


class ResultEvent(BaseModel):
    """ Results of the event """
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, verbose_name=_("Захід"), on_delete=models.CASCADE)
    result_time = models.TimeField(_("Результат"))

    def __str__(self) -> str:
        return f"{self.athlete.last_name} - {self.event.title} ({self.result_time})"

    class Meta:
        """ Meta class """
        ordering = ("-created_at",)
        verbose_name = _("Результати заходу")
        verbose_name_plural = _("Результати заходів")
