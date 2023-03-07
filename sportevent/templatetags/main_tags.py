"""Tags for templates"""
from django import template
from django.db.models import QuerySet

from sportevent.models import Distance

register = template.Library()


@register.simple_tag
def get_all_event_distances(event_id: int) -> list[QuerySet]:
    """ Returns all event distances """
    event_distance = Distance.objects.filter(event=event_id)
    return event_distance.all()
