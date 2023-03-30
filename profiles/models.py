""" Models profiles """

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from profiles.enums import GenderChoices


class Athlete(AbstractUser):
    """ Custom full-featured user model """

    date_of_birth = models.DateField(
        verbose_name=_("Дата народження"),
        blank=True,
        null=True,
    )
    gender = models.CharField(
        verbose_name=_("Стать"),
        max_length=6,
        default=GenderChoices.MALE,
        choices=GenderChoices.choices,
    )
    phone_regex = RegexValidator(regex=r"^\+?1?\d{9,13}$",
                                 message="Номер телефону у форматі: "
                                         "'+380999999'. Дозволено до 13 цифр.",
                                 )
    phone = models.CharField(
        verbose_name=_("Номер телефону"),
        validators=[phone_regex],
        max_length=13,
        blank=True,
        null=True,
    )
    emergency_contact_name = models.CharField(
        verbose_name=_("Ім'я екстреного контакту"),
        max_length=50,
        blank=True,
        null=True,
    )
    emergency_contact_phone = models.CharField(
        verbose_name=_("Номер телефону екстреного контакту"),
        max_length=15,
        blank=True,
        null=True,
    )
    city = models.CharField(
        verbose_name=_("Населений пункт"),
        max_length=100,
        blank=True,
        null=True,
    )
    club = models.CharField(
        verbose_name=_("Спортивний клуб"),
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}: ({self.username})" \
            if self.first_name and self.last_name is not None else self.username

    class Meta:
        ordering = ("username",)
        verbose_name = _("Athlete")
        verbose_name_plural = _("Athletes")
