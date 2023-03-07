from django import template
from sportevent.models import Distance, Athlete, Event

register = template.Library()


@register.simple_tag
def get_all_athletes_of_distance(event_id):
    """Повертає всіх атлетів дистанції даного заходу"""
    event = Distance.objects.get(id=event_id)
    return event.athlete.all()
