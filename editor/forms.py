from django import forms
from .models import info
from ckeditor.widgets import CKEditorWidget


class InfoForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(),label="Text Editor")
    class Meta:
        model=info
        fields="__all__"


