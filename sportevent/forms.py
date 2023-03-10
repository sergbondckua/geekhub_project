"""Forms"""
from django import forms

from .models import Athlete


class AthleteForm(forms.ModelForm):
    """Forms"""

    class Meta:
        """Meta class"""
        model = Athlete
        fields = "__all__"
