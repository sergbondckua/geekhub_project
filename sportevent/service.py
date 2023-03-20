"""Services"""
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _


def send_registrant_for_distance(athlete_email, distance, event):
    """ Send a email to the registrant for the race """
    subject = _("[crossrunche] Вітаємо! Ваша реєстрація була успішною!")
    message = _(
        f"Вітаємо! Ви успішно зареєструвалися на {event}. "
        f"Обрана вами дистанція {distance}."
    )
    from_email = "crossrunche@ukr.net"
    recipient_list = [athlete_email]
    send_mail(subject, message, from_email, recipient_list)
