from django import forms
from django.core.exceptions import ValidationError

from .models import Advertisement
class AdvertisementForm(forms.ModelForm):
    def __init__(self):
        super().__init__()
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'image', 'price', 'auction']

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?') or title.startswith('!'):
            raise ValidationError('Уберите лишние знаки')
        return title