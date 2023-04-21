from django.urls import path
from . import views

urlpatterns = [

    path('countryinfo/', views.countryinfo, name='countryinfo'),
    path('continentlist/', views.continentlist, name='continentlist'),
]