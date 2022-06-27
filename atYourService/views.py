from django.shortcuts import render
from .models import Client

# from django.http import HttpResponse


# dummy data for testing
number = "9544610809"


# number = "7777777777"


# Create your views here.
def home(request):
    # return HttpResponse('<h1> This is the Home page </h1>')

    # context = {
    #     "title": "home",
    #     "client": Client.objects.get(PhoneNumber=number),  # just for testing needed to be changed
    # }

    if request.user.is_authenticated:
        context = {
            "title": "home",
            "client": Client.objects.get(UserName=request.user.id),  # temporary
        }
    else:
        context = {
            "title": "home",
        }

    return render(request, 'atYourService/home.html', context)


def about(request):
    context = {
        "title": "about",
    }
    return render(request, 'atYourService/about.html', context)
