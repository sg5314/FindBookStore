from unicodedata import name
from django.urls import path
from .views import searchfunc, storefunc, kinokuniya_store_func
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', searchfunc, name='search'),
    path('stores/<int:pk>', storefunc, name='stores'),
    path('kinokuniya/<int:pk>',kinokuniya_store_func, name='kinokuniya')
]