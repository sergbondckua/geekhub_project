"""Models"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from sportevent.common.models import BaseModel


class Athlete(AbstractUser):
    """
    Повнофункціональна модель користувача сайту
    """

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
        """
        Рядкове представлення экземпляру класу
        """
        return f"{self.first_name} {self.last_name}: ({self.username})" \
            if self.first_name and self.last_name is not None else self.username

    class Meta:
        """Meta клас"""
        ordering = ("username",)
        verbose_name = _("Атлета")
        verbose_name_plural = _("Атлети")


class Event(BaseModel):
    """
    Спортивний захід
    """

    title = models.CharField(_("Назва"), max_length=100)
    date_event = models.DateField(_("Дата проведення"))
    location = models.CharField(_("Місце проведення"), max_length=200)
    description = models.TextField(_("Опис"), blank=True)

    def __str__(self):
        """
        Рядкове представлення экземпляру класу
        """
        return self.title

    class Meta:
        """Meta клас"""
        ordering = ("date_event",)
        verbose_name = _("Спортивний захід")
        verbose_name_plural = _("Спортивні заходи")


class Distance(BaseModel):
    """
    Дистанція
    """

    title = models.CharField(_("Назва"), max_length=50)
    distance_in_unit = models.PositiveSmallIntegerField(_("Дистанція"))
    event = models.ForeignKey(
        Event,
        verbose_name=_("Спорт захід"),
        related_name="events",
        on_delete=models.CASCADE
    )
    athlete = models.ManyToManyField(
        Athlete,
        verbose_name=_("Атлети"),
        related_name="athletes",
        blank=True
    )

    def __str__(self):
        """
        Рядкове представлення экземпляру класу
        """
        return f"{self.event} -- {self.title}: {self.distance_in_unit}"

    class Meta:
        """Meta клас"""
        ordering = ("-created_at",)
        verbose_name = _("Дистанція")
        verbose_name_plural = _("Дистанції")


class ResultEvent(BaseModel):
    """
    Результати заходу
    """
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, verbose_name=_("Захід"), on_delete=models.CASCADE)
    result_time = models.TimeField(_("Результат"))

    def __str__(self):
        return f"{self.athlete.last_name} - {self.event.title} ({self.result_time})"

    class Meta:
        """Meta клас"""
        ordering = ("-created_at",)
        verbose_name = _("Результати заходу")
        verbose_name_plural = _("Результати заходів")
