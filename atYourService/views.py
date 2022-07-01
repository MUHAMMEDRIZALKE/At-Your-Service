from django.shortcuts import render
from .models import Client


# from django.http import HttpResponse


# Create your views here.
def home(request):
    context = {
        "title": "home",
    }

    return render(request, 'atYourService/home.html', context)


def about(request):
    context = {
        "title": "about",
    }
    return render(request, 'atYourService/about.html', context)
