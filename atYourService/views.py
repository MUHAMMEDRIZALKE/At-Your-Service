from django.shortcuts import render
from django.contrib.gis.db.models.functions import Distance
from .models import Worker
from .forms import UserForm
from django.contrib.gis.measure import Distance as D  # needed for the queryset
from django.contrib import messages


########################################################################################################################
# from django.views import generic
# from django.contrib.gis.geos import fromstr
# from django.contrib.gis.geos import Point
# from django.http import HttpResponse


# Create your views here.
# def home(request):
#     context = {
#         "title": "home",
#     }
#
#     return render(request, 'atYourService/home.html', context)


# hard coded location
# longitude = 76.406155
# latitude = 10.161879
#
# user_location = Point(longitude, latitude, srid=4326)


# class Home(generic.ListView):
#     model = Worker
#     context_object_name = 'workers'
#
#     # queryset = Worker.objects.annotate(distance=Distance('Location', user_location)).order_by('distance')[0:6]
#
#     queryset = Worker.objects.filter(Location__dwithin=(user_location, 0.1)).filter(  # 0.1 for 11.1km
#         Location__distance_lte=(user_location, D(km=10))).annotate(  # distance 10km
#         distance=Distance('Location', user_location)).order_by('distance')[0:6]
#     template_name = 'atYourService/home.html'
#
#     profession = 'mechanic'
#
#     def get_context_data(self, **kwargs):
#         context = super(Home, self).get_context_data(**kwargs)
#         context.update({'profession': self.profession})
#         return context

########################################################################################################################

class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''


def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                profession = form.cleaned_data.get('Profession')
                user_location = form.cleaned_data.get('location')
                radius = form.cleaned_data.get('radius')

                workers = Worker.objects.filter(Location__dwithin=(user_location, 1.1)).filter(  # 0.1 for 11.1km
                    Location__distance_lte=(user_location, D(km=radius))).annotate(  # distance 10km
                    distance=Distance('Location', user_location)).order_by('distance')[0:6]

                context = {'form': form,
                           'workers': workers,
                           'profession': profession,
                           # 'usr_loc': user_location,
                           'counter': Counter(),
                           'radius': radius,
                           }

                return render(request, 'atYourService/home.html', context)

            except Exception as e:
                messages.warning(request, e)

    else:
        form = UserForm()
    return render(request, 'atYourService/home.html', {'form': form})


#####################################################################################

def about(request):
    context = {
        "title": "about",
    }
    return render(request, 'atYourService/about.html', context)
