from django.contrib import admin
from django.urls import path
from core.views import  weather_data_rendering

urlpatterns = [
    #loc variable is for location , days variables is for period
    path('forecast/<loc>/<int:days>/', weather_data_rendering, name='forecast_url'),
    
]