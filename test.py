import os, sys, django
os.environ["DJANGO_SETTINGS_MODULE"] = "mappy.settings"
sys.path.insert(0, os.getcwd())

django.setup()

from mappy.views import StoreLocation as s
x = s()
x.store_to_fusion('est') 
