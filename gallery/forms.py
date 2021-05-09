from django import forms

from .models import VectorDrawing


class VectorDrawingForm(forms.ModelForm):
    new_tags = forms.CharField(
        label='Новые теги', help_text='Укажите новые теги через ";"', required=False)

    class Meta:
        model = VectorDrawing
        fields = ('title', 'description', 'image', 'tags', 'new_tags')
