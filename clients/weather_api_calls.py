import requests
import json

#This is for testing purposes, do not push secrets keys onto production
API_KEY = "ebd2d4802a1647be8c6100439200312"
FORECAST_BASE_URL = "http://api.weatherapi.com/v1/forecast.json?key="
# http://api.weatherapi.com/v1/forecast.json?key=ebd2d4802a1647be8c6100439200312&q=Likasi&days=3
HEADERS = {
     'content-type': "application/x-www-form-urlencoded"
    }
class WeatherConnClient():

    @staticmethod
    def weatherapi_call(location, period):
        """
        location is a string , eg. Lubumbashi, Pretoria, Lodon, etc.
        period is an integer that specifies the number of days.
        """
        LOCATION_PERIOD = "&q=" + location + "&days=" + str(period)
        URL_WITH_PARAMS = FORECAST_BASE_URL + API_KEY + LOCATION_PERIOD
        response = requests.get(URL_WITH_PARAMS, headers=HEADERS)
        #Convert .txt data to JSON data
        json_body = json.loads(response.text)
        return json_body