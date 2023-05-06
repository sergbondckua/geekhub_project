"""Services"""
import os
import uuid

from slugify import slugify

from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _


def send_registrant_for_distance(athlete_email, distance, event):
    """Send a email to the registrant for the race"""
    subject = _("[crossrunche] Вітаємо! Ваша реєстрація була успішною!")
    message = _(
        f"Вітаємо! Ви успішно зареєструвалися на {event}. "
        f"Обрана вами дистанція {distance}."
    )
    from_email = "crossrunche@ukr.net"
    recipient_list = [athlete_email]
    send_mail(subject, message, from_email, recipient_list)


def generate_path(instance, filename):
    """Generates path and filename to save"""
    title = slugify(instance.title).lower()
    try:
        event = slugify(instance.event.title).lower()
    except AttributeError:
        event = slugify(instance.title).lower()
        title = "poster"
    ext = os.path.splitext(filename)[-1]
    result = f"event/{event}_{title}_{str(uuid.uuid4().hex)}{ext}"
    path = os.path.join(settings.MEDIA_ROOT, result)
    if os.path.exists(path):
        os.remove(path)
    return result
