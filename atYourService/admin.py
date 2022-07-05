from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Client, Worker

# Register your models here.
admin.site.register(Client)


@admin.register(Worker)
class WorkerAdmin(OSMGeoAdmin):
    list_display = ('Name', 'Location')  # fields of the table
