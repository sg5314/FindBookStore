from django.urls import path
from .views import searchfunc, storefunc, kinokuniya_store_func

urlpatterns = [
    path('', searchfunc, name='search'),
    path('stores/<int:pk>', storefunc, name='stores'),
    path('kinokuniya/<int:pk>',kinokuniya_store_func, name='kinokuniya')
]