from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse
from apiclient.discovery import build

from location.models import Location

class IndexView(View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, args)

def get_fusion_table_entry(request):
    api_key = 'AIzaSyDp-SUMb87oArzDC66fGyVkptlCae3bI-c'
    table = '14CoGxBdCA2URHZq8nlLrR8swp3AFU1JSijak0rY1'
    service = build('fusiontables', 'v2', developerKey=api_key)
    #result = service.activities().list(userId='me', collection='public').execute()
    #tasks = result.get('items', [])
    #for task in tasks:
    #    print task['title']

class StoreLocation(View):
    def get(self,request,*args,**kwargs):
        try:
            lat = request.GET.get('lat',None)
            lng = request.GET.get('lng',None)
            location = request.GET.get('location',None)
            Location.objects.get_or_create(latitude = lat,longitude = lng, defaults={'location':str(location)})
            return JsonResponse({'message':'success'})
        except Exception,e:
            print e
            return JsonResponse({'message':'error'})
