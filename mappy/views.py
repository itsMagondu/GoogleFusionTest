from django.views.generic import View
from django.shortcuts import render
from django.http import JsonResponse

from location.models import Location,Token
import simplejson
import requests

class IndexView(View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, args)

class StoreLocation(View):
    url = "https://www.googleapis.com/fusiontables/v2/query"
    table = '1UbnbcY4LOlfyrXzW3DwKmziMqYwUr1KOBA0UstY7'
    key = 'AIzaSyCbrQhFZ1je_6JBQqxL4EUc4UDz5pVplXM'
    client_id = "814241495129-grl2uqh5bqon21r5q767nn3b918e6lig.apps.googleusercontent.com"
    client_secret = "GmOIbjxIi5up9AyzMPayhvHl"
    redirect_uri = "http://localhost"
    authorization_base_url = "https://accounts.google.com/o/oauth2/auth"

    code = "4/_iooTu6M9hYh-FPFlJ0FBzVyQBfpkDBRYdGxTEsudOs#"
    refresh_token = "1/EJ24h-a0eQn_ofss5S12QiFL0nSFHY44jMGnLG4iGzY"

    payload = {
            "client_id":client_id,
            "client_secret":client_secret,
            "refresh_token":refresh_token,
            "grant_type":"refresh_token",
        }

    def get(self,request,*args,**kwargs):
        try:
            lat = request.GET.get('lat',None)
            lng = request.GET.get('lng',None)
            location = request.GET.get('location',None)
            loc,created = Location.objects.get_or_create(latitude = lat,longitude = lng, defaults={'location':str(location)})
            if created:
                self.store_to_fusion(loc)

            return JsonResponse({'message':'success'})
        except Exception,e:
            print e
            return JsonResponse({'message':'error'})

    def store_to_fusion(self,loc):
        tokens = Token.objects.filter(valid=True)
        if tokens:
            access_token = tokens[0].access_token
        else:
            access_token=self.generate_token()
            t,created = Token.objects.get_or_create(access_token=access_token)

        data = {'sql': "INSERT INTO "+self.table+"(Address,Longitude,Latitude) VALUES ('"+loc.location+"','"+loc.longitude+"','"+loc.latitude+"');"}
        r = requests.post(self.url + "?key="+self.key+"&access_token="+access_token,data=data)
        print r.text

        resp = simplejson.loads(r.text)
        if resp['error']:
            er = resp['error']
            for i in tokens:
                i.valid = False
                i.save()
            access_token = self.generate_token()
            t,created = Token.objects.get_or_create(access_token=access_token)
            r = requests.post(url + "?key="+key+"&access_token="+access_token,data=data)
        return r.text

    def generate_token(self):
        r = requests.post("https://www.googleapis.com//oauth2/v3/token",data=self.payload)
        print r.text
        resp = simplejson.loads(r.text)
        return resp['access_token']

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

        resp = simplejson.loads(r.text)
        if resp['error']:
            er = resp['error']

        print r.text
        return r.text

def get_new_token(refresh_token):
    {}
