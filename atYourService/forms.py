from django.contrib.gis import forms
from leaflet.forms.widgets import LeafletWidget


class UserForm(forms.Form):
    jobs = (('mechanic', 'MECHANIC'),
            ('electrician', 'Electrician'))

    Profession = forms.CharField(widget=forms.Select(choices=jobs))
    location = forms.PointField(widget=LeafletWidget())
