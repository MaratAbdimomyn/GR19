from django import forms
from django.utils import timezone

class AddPhone(forms.Form):
    brand = forms.CharField(max_length=40, label='Бренд')
    model_name = forms.CharField(max_length=40, label='Модель')
    country = forms.CharField(max_length=40, label='Страна')