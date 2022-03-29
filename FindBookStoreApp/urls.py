from django.urls import path
from .views import searchfunc

urlpatterns = [
    path('', searchfunc)
]