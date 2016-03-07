from django.contrib import admin
from .models import Location,Token

class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','longitude','latitude','location']
    list_filter = ['longitude','latitude']

class TokenAdmin(admin.ModelAdmin):
    list_display = ['id','access_token','valid','added']
    list_filter = ['valid']

admin.site.register(Location, LocationAdmin)
admin.site.register(Token, TokenAdmin)
