from django.forms import ModelForm

from .models import VectorDrawing


class VectorDrawingForm(ModelForm):
    class Meta:
        model = VectorDrawing
        fields = ('title', 'description', 'image', 'tags')
