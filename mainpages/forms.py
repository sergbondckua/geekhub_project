
from django import forms
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from mainpages.models import StaticPage


class StaticPageAdminForm(forms.ModelForm):
    """Form for static pages"""
    content = forms.CharField(
        label=_("Content"),
        widget=CKEditorUploadingWidget(),
    )

    class Meta:
        model = StaticPage
        fields = '__all__'
