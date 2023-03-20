"""Tasks"""
from celery import shared_task

from .service import send_registrant_for_distance


@shared_task
def send_to_athlete(athlete_email, distance, event):
    """Process send email to athlete"""
    send_registrant_for_distance(athlete_email, distance, event)
