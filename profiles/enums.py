from django.db import models
from django.utils.translation import gettext_lazy as _


class GenderChoices(models.TextChoices):
    """ The gender choices """
    MALE = "male", _("Чоловіча")
    FEMALE = "female", _("Жіноча")
