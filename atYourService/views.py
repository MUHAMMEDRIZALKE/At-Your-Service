from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Worker
from django.contrib.gis.geos import Point

# from .forms import MyGeoForm

from django.contrib.gis.measure import Distance as D  # needed for the queryset

# from django.http import HttpResponse


# Create your views here.
# def home(request):
#     context = {
#         "title": "home",
#     }
#
#     return render(request, 'atYourService/home.html', context)


# hard coded location
longitude = 76.406155
latitude = 10.161879

user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Worker
    context_object_name = 'workers'

    # queryset = Worker.objects.annotate(distance=Distance('Location', user_location)).order_by('distance')[0:6]

    queryset = Worker.objects.filter(Location__dwithin=(user_location, 0.1)).filter(  # 0.1 for 11.1km
        Location__distance_lte=(user_location, D(km=10))).annotate(  # distance 10km
        distance=Distance('Location', user_location)).order_by('distance')[0:6]
    template_name = 'atYourService/home.html'

    profession = 'mechanic'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context.update({'profession': self.profession})
        return context


def about(request):
    context = {
        "title": "about",
    }
    return render(request, 'atYourService/about.html', context)
