from django import forms
from django.contrib.gis import forms as fm
from django.contrib.auth.models import User
from django.forms import ModelForm

from atYourService.models import Client
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from leaflet.forms.widgets import LeafletWidget


class UserRegisterForm(forms.Form):
    Username = forms.CharField(max_length=100)
    Name = forms.CharField(max_length=100)
    phoneNumberRegex = RegexValidator(regex=r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")  # indian phone number validator
    PhoneNumber = forms.CharField(validators=[phoneNumberRegex], max_length=16, label="Phone Number")
    Password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class ProfessionalRegistrationForm(forms.Form):
    pro_choice = (
        ('mechanic', 'MECHANIC'),
        ('electrician', 'ELECTRICIAN'),
        ('plumber', 'PLUMBER'),
        ('domestic Worker', 'DOMESTIC WORKER'),
        ('cook', 'COOK'),
        ('driver', 'DRIVER'),
        ('gardener', 'GARDENER'),
        ('saloon', 'SALOON'),
    )

    Username = forms.CharField(max_length=100)
    Name = fm.CharField(max_length=100)
    Password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    profession = fm.CharField(max_length=30, widget=forms.Select(choices=pro_choice))
    phoneNumberRegex = RegexValidator(regex=r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")  # indian phone number validator
    PhoneNumber = fm.CharField(validators=[phoneNumberRegex], max_length=16, label="Phone Number")
    whatsappNumberRegex = RegexValidator(regex=r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")  # indian phone number validator
    whatsappNumber = fm.CharField(validators=[phoneNumberRegex], max_length=16, label="Whatsapp Number")
    yearsOfExperience = fm.DecimalField(max_digits=5, decimal_places=1, label="Years of Experience")
    Location = fm.PointField(widget=LeafletWidget())
