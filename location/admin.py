from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','longitude','latitude','location']
    list_filter = ['longitude','latitude']

admin.site.register(Location, LocationAdmin)
