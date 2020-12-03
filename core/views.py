from django.shortcuts import render
from django.http import JsonResponse
from clients.weather_api_calls import WeatherConnClient

def weather_data_rendering(request, loc, days):
    response = WeatherConnClient.weatherapi_call(loc, days)
    weather_data = {}
    weather_data["location"] = response["location"]["name"]
    
    #Loop through the response to get only what is required.
    for index in range(len(response["forecast"]["forecastday"])):
        weather_data["date"+"_"+ str(index)]= response["forecast"]["forecastday"][index]["date"]
        weather_data["max_temperature"+"_"+ str(index)]= response["forecast"]["forecastday"][index]["day"]["maxtemp_c"]
        weather_data["min_temperature"+"_"+ str(index)]= response["forecast"]["forecastday"][index]["day"]["mintemp_c"]
        weather_data["average_temperature"+"_"+ str(index)]= response["forecast"]["forecastday"][index]["day"]["avgtemp_c"]
        weather_data["humidity"+"_"+ str(index)]= response["forecast"]["forecastday"][index]["day"]["avghumidity"]
    return JsonResponse(weather_data)
