""" Forms sportevent """


from django import forms
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from sportevent.models import Event, Distance


class EventAdminForm(forms.ModelForm):
    """Form for Event """
    description = forms.CharField(
        label=_("Description"),
        widget=CKEditorUploadingWidget(),
    )

    class Meta:
        model = Event
        fields = '__all__'


class DistanceAdminForm(forms.ModelForm):
    """Form for Distance"""
    description = forms.CharField(
        label=_("Description"),
        widget=CKEditorUploadingWidget(),
    )

    class Meta:
        model = Distance
        fields = '__all__'
