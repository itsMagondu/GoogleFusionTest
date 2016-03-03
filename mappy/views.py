from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse

from location.models import Location

class IndexView(View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, args)

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
