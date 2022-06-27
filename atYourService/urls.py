from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ays-home'),
    path("about/", views.about, name='ays-about'),
]
