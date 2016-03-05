from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse

from location.models import Location
import requests

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
            loc,created = Location.objects.get_or_create(latitude = lat,longitude = lng, defaults={'location':str(location)})
            self.store_to_fusion(loc)

            return JsonResponse({'message':'success'})
        except Exception,e:
            print e
            return JsonResponse({'message':'error'})

    def store_to_fusion(self,loc):
        url = "https://www.googleapis.com/fusiontables/v2/query"
        table = '1UbnbcY4LOlfyrXzW3DwKmziMqYwUr1KOBA0UstY7'
        key = 'AIzaSyCbrQhFZ1je_6JBQqxL4EUc4UDz5pVplXM'
        client_id = "814241495129-grl2uqh5bqon21r5q767nn3b918e6lig.apps.googleusercontent.com"
        client_secret = "GmOIbjxIi5up9AyzMPayhvHl"
        redirect_uri = "http://localhost"
        scope = ["https://www.googleapis.com/auth/fusiontables"]
        authorization_base_url = "https://accounts.google.com/o/oauth2/auth"

        code = "4/_iooTu6M9hYh-FPFlJ0FBzVyQBfpkDBRYdGxTEsudOs#"
        refresh_token = "1/EJ24h-a0eQn_ofss5S12QiFL0nSFHY44jMGnLG4iGzY"

        payload = {"grant_type": "authorization_code",
                    "code": code,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "redirect_uri": redirect_uri,}

        payload2 = {
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri,
        }

        #print "https://accounts.google.com/o/oauth2/auth?%s%s%s%s%s" % ("client_id=%s&" % (client_id), "redirect_uri=%s&" % (redirect_uri),"scope=https://www.googleapis.com/auth/fusiontables&", "response_type=code&","access_type=offline")

        #serv_resp = requests.post("https://accounts.google.com/o/oauth2/token",data=payload)
        #print serv_resp.text

        access_token = "ya29.nAJnrftsFh_7nxyQv-xfOjz5HWp5jr0V4G7LoBK9BdD7FtjTtM9ZPrj9oELkGfwr5A"

        #request = requests.post("https://accounts.google.com/o/oauth2/token",data =payload)
        #print request.text
        #tokens = simplejson.loads(request.text)
        #access_token = tokens["access_token"]

        data = {'sql': "INSERT INTO "+table+"(Address,Longitude,Latitude) VALUES ('"+loc.location+"','"+loc.longitude+"','"+loc.latitude+"');"}
        #data = {'sql':'SELECT * FROM '+table +';'}
        r = requests.post(url + "?key="+key+"&access_token="+access_token,data=data)
        print r.text
        return r.text

class FlushDB(View):
    def get(self,request,*args,**kwargs):
        try:
            Location.objects.all().delete() 
            self.flush_fusion_table()
            return JsonResponse({'message':'success'})
        except Exception,e:
            print e
            return JsonResponse({'message':'error'})

    def flush_fusion_table(self):
        url = "https://www.googleapis.com/fusiontables/v2/query"
        table = '1UbnbcY4LOlfyrXzW3DwKmziMqYwUr1KOBA0UstY7'
        key = 'AIzaSyCbrQhFZ1je_6JBQqxL4EUc4UDz5pVplXM'
        client_id = "814241495129-grl2uqh5bqon21r5q767nn3b918e6lig.apps.googleusercontent.com"
        client_secret = "GmOIbjxIi5up9AyzMPayhvHl"
        redirect_uri = "http://localhost"
        scope = ["https://www.googleapis.com/auth/fusiontables"]
        authorization_base_url = "https://accounts.google.com/o/oauth2/auth"

        code = "4/_iooTu6M9hYh-FPFlJ0FBzVyQBfpkDBRYdGxTEsudOs#"
        refresh_token = "1/EJ24h-a0eQn_ofss5S12QiFL0nSFHY44jMGnLG4iGzY"

        payload = {"grant_type": "authorization_code",
                    "code": code,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "redirect_uri": redirect_uri,}

        access_token = "ya29.nAJnrftsFh_7nxyQv-xfOjz5HWp5jr0V4G7LoBK9BdD7FtjTtM9ZPrj9oELkGfwr5A"

        data = {'sql': "DELETE FROM "+table}
        r = requests.post(url + "?key="+key+"&access_token="+access_token,data=data)
        print r.text
        return r.text
