"""Tags for templates"""
from django import template
from django.db.models import QuerySet

from sportevent.models import RegisterDistanceAthlete

register = template.Library()


@register.simple_tag
def get_all_event_distances(distance_id: int) -> list[QuerySet]:
    """ Returns all event distances """
    event_distance = RegisterDistanceAthlete.objects.filter(event=distance_id)
    return event_distance.all()
