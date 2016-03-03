from django.conf.urls import url
from django.contrib import admin
from views import IndexView,StoreLocation

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^location', StoreLocation.as_view(),name='addlocation'),
    url(r'^', IndexView.as_view(),name='index'),
]
