from django.test import TestCase
from django.urls import reverse
from clients.weather_api_calls import WeatherConnClient

class TestClientConnection(TestCase):

    def test_weatherapi_call(self):
        location = "Likasi" #A small and beautiful in South - DRCongo
        period  = 2
        action = WeatherConnClient.weatherapi_call(location, period)
        self.assertIsNotNone(action)
        self.assertEqual(action["location"]["name"], "Likasi")
    
    def test_weather_data_rendering(self):
        url = reverse('forecast_url', args=["Likasi", 2])
        request = self.client.get(url)
        self.assertEqual(request.json()["location"], 'Likasi')
        

