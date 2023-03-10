"""Forms"""
from django import forms

from .models import Distance


class DistanceForm(forms.ModelForm):
    """Forms"""

    class Meta:
        """Meta class"""
        model = Distance
        fields = ["athlete"]
