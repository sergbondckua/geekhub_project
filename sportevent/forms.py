"""Forms"""
from datetime import datetime

from django import forms

from .models import Athlete


class AthleteForm(forms.ModelForm):
    """Forms"""

    class Meta:
        """Meta class"""
        model = Athlete
        fields = (
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "gender",
            "phone",
            "city",
            "club",
        )

        widgets = {
            "first_name": forms.TextInput(attrs={"required": "True"}),
            "last_name": forms.TextInput(attrs={"required": "True"}),
            "email": forms.EmailInput(attrs={"required": "True"}),
            "date_of_birth": forms.DateInput(
                attrs={"required": "True", "type": ""},
            ),
            "gender": forms.Select(attrs={"required": "True"}),
            "phone": forms.TextInput(attrs={"required": "True"}),
            "city": forms.TextInput(attrs={"required": "True"}),
            "club": forms.TextInput(attrs={"required": "True"}),
        }
