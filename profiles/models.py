""" Models profiles """

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from profiles.enums import GenderChoices


class Athlete(AbstractUser):
    """Custom full-featured user model"""

    date_of_birth = models.DateField(
        verbose_name=_("Date of birth"),
        blank=True,
        null=True,
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        max_length=6,
        default=GenderChoices.MALE,
        choices=GenderChoices.choices,
    )
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,13}$",
        message=_("Phone number in the format: '+380999999'. Up to 13 digits allowed."),
    )
    phone = models.CharField(
        verbose_name=_("Phone number"),
        validators=[phone_regex],
        max_length=13,
        blank=True,
        null=True,
    )
    emergency_contact_name = models.CharField(
        verbose_name=_("Emergency contact name"),
        max_length=50,
        blank=True,
        null=True,
    )
    emergency_contact_phone = models.CharField(
        verbose_name=_("Emergency contact phone number"),
        max_length=15,
        blank=True,
        null=True,
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=100,
        blank=True,
        null=True,
    )
    club = models.CharField(
        verbose_name=_("Sport Club"),
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}: ({self.username})"
            if self.first_name and self.last_name is not None
            else self.username
        )

    class Meta:
        ordering = ("username",)
        verbose_name = _("Athlete")
        verbose_name_plural = _("Athletes")
