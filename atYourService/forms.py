from django.contrib.gis import forms
from leaflet.forms.widgets import LeafletWidget


class UserForm(forms.Form):
    jobs = (
        ('mechanic', 'MECHANIC'),
        ('electrician', 'ELECTRICIAN'),
        ('plumber', 'PLUMBER'),
        ('domestic Worker', 'DOMESTIC WORKER'),
        ('cook', 'COOK'),
        ('driver', 'DRIVER'),
        ('gardener', 'GARDENER'),
        ('saloon', 'SALOON'),
    )

    Profession = forms.CharField(widget=forms.Select(choices=jobs))
    location = forms.PointField(widget=LeafletWidget())
    radius = forms.IntegerField()
