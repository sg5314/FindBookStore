from unicodedata import name
from django.urls import path
from .views import searchfunc, storefunc, storesfinc
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', searchfunc),
    path('store/',storefunc),
    path('stores/<int:pk>', storesfinc, name='stores')
]