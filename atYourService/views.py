from django.shortcuts import render, redirect
from django.contrib.gis.db.models.functions import Distance
from .models import Worker
from .forms import UserForm, UserForm1
from django.contrib.gis.measure import Distance as D  # needed for the queryset
from django.contrib import messages


class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''


def home(request, arg_pro="default"):
    if arg_pro != "default":
        if request.user.is_authenticated:

            if request.method == 'POST':
                form = UserForm1(request.POST)
                if form.is_valid():
                    try:
                        user_location = form.cleaned_data.get('location')
                        radius = form.cleaned_data.get('radius')

                        workers = Worker.objects.filter(Location__dwithin=(user_location, 1.1)).filter(
                            # 0.1 for 11.1km
                            Location__distance_lte=(user_location, D(km=radius))).annotate(  # distance 10km
                            distance=Distance('Location', user_location)).order_by('distance')[0:6]

                        context = {'form': form,
                                   'workers': workers,
                                   'profession': arg_pro,
                                   # 'usr_loc': user_location,
                                   'counter': Counter(),
                                   'radius': radius,
                                   }

                        return render(request, 'atYourService/home.html', context)

                    except Exception as e:
                        messages.warning(request, e)

            else:
                form = UserForm1()
            return render(request, 'atYourService/home.html', {'form': form})
        else:
            return redirect('login')

    if request.user.is_authenticated:

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
    else:
        return redirect('login')


def about(request):
    context = {
        "title": "about",
    }
    return render(request, 'atYourService/about.html', context)


def index(request):
    return render(request, 'atYourService/index.html')
