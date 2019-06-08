from django import forms
from .models import GroupModel


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40)
    group = forms.ChoiceField(choices=GroupModel.objects.all())
