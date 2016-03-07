import os, sys, django
os.environ["DJANGO_SETTINGS_MODULE"] = "mappy.settings"
sys.path.insert(0, os.getcwd())

django.setup()

from mappy.views import StoreLocation as s
x = s()
x.store_to_fusion('est') 

error_message = '{"error": { "errors": [ {"domain": "global","reason": "authError","message": "Invalid Credentials","locationType": "header", "location": "Authorization" }  ], "code": 401, "message": "Invalid Credentials"}}'

success_message = '{ "kind": "fusiontables#sqlresponse", "columns": [  "rowid" ], "rows": [  [ "4002"  ]]}'
