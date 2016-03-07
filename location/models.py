from __future__ import unicode_literals
from django.db import models

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=200, null=True, blank=True)
    def __unicode__(self):
        return self.location
    
class Token(models.Model):
    access_token = models.CharField(max_length=200, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    valid = models.BooleanField(default=True)
    def __unicode__(self):
        return self.access_token
    
