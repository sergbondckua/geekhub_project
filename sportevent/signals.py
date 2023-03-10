"""Signals"""
from django.db.models.signals import pre_save
from django.dispatch import receiver
from sportevent.models import RegisterDistanceAthlete


@receiver(pre_save, sender=RegisterDistanceAthlete)
def assign_start_number(sender, instance, **kwargs):
    """Assigns start number"""
    prefix = instance.distance.distance_in_unit
    if not instance.start_number:
        last_participant = RegisterDistanceAthlete.objects.filter(
            distance=instance.distance).order_by("-start_number").first()
        if last_participant:
            instance.start_number = last_participant.start_number + 1
        else:
            instance.start_number = prefix * 100 + 1
