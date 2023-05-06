from django.db import models
from django.utils.translation import gettext_lazy as _

from mainpages.common.models import BaseModel


class StaticPage(BaseModel):
    """A static page"""

    title = models.CharField(_("Title"), max_length=50)
    url = models.CharField(
        _("URL-name"),
        max_length=20,
        unique=True,
        help_text=_("Only latin characters"),
    )
    content = models.TextField(_("Content"))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)
        verbose_name = _("Static page")
        verbose_name_plural = _("Static pages")
