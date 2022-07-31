from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ays-index'),
    path('home/<arg_pro>', views.home, name='ays-home'),
    path('home/', views.home, name='ays-home'),
    path("about/", views.about, name='ays-about'),
]
