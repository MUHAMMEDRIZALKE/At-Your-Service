from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from atYourService.models import Client
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


class UserRegisterForm(forms.Form):
    Username = forms.CharField(max_length=100)
    Name = forms.CharField(max_length=100)
    phoneNumberRegex = RegexValidator(regex=r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")  # indian phone number validator
    PhoneNumber = forms.CharField(validators=[phoneNumberRegex], max_length=16)
    Password = forms.CharField(max_length=100, widget=forms.PasswordInput)


