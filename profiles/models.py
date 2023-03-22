""" Models profiles """

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Athlete(AbstractUser):
    """ Custom full-featured user model """

    GENDER_CHOICES = (
        ("male", _("Чоловіча")),
        ("female", _("Жіноча")),
    )

    date_of_birth = models.DateField(
        _("Дата народження"),
        blank=True,
        null=True
    )
    gender = models.CharField(
        _("Стать"),
        max_length=10,
        default="male",
        choices=GENDER_CHOICES
    )
    phone_regex = RegexValidator(regex=r"^\+?1?\d{9,13}$",
                                 message="Номер телефону у форматі: "
                                         "'+380999999'. Дозволено до 13 цифр."
                                 )
    phone = models.CharField(_("Номер телефону"), validators=[phone_regex],
                             max_length=13, blank=True)
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
