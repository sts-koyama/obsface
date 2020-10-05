from django import forms

from .models import ImageTable


class ImageForm(forms.ModelForm):
  class Meta:
    model = ImageTable
    fields = ('title', 'content', 'author', 'images', 'evaluation')
