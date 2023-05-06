""" Forms profiles """
from datetime import datetime

from django import forms

from .models import Athlete


class AthleteForm(forms.ModelForm):
    """Forms"""

    class Meta:
        """Meta class"""

        model = Athlete
        fields = (
            # "username",
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
            "email": forms.EmailInput(
                attrs={"required": "True", "readonly": "True"}),
            "date_of_birth": forms.SelectDateWidget(
                years=range(datetime.now().year - 70, datetime.now().year - 18),
                attrs={
                    "style": "width: auto; display: inline-block;",
                    "required": "True",
                    "type": "date",
                    "class": "form-select",
                },
            ),
            "gender": forms.RadioSelect(attrs={"required": "True"}),
            "phone": forms.TextInput(attrs={"required": "True"}),
            "city": forms.TextInput(attrs={"required": "True"}),
        }
