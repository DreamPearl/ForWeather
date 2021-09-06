import unittest
from unittest.mock import patch
import forweather

FAKE_DATA='{"coord":{"lon":78.08,"lat":27.88},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":16.32,"feels_like":12.05,"temp_min":16.32,"temp_max":16.32,"pressure":1017,"humidity":29,"sea_level":1017,"grnd_level":994},"visibility":10000,"wind":{"speed":2.92,"deg":293},"clouds":{"all":0},"dt":1608380759,"sys":{"country":"IN","sunrise":1608341618,"sunset":1608378964},"timezone":19800,"id":1279017,"name":"Aligarh","cod":200}'

class FakeWeather():
    def read(self):
        return FAKE_DATA

def fake_urlopen(a):
    obj=FakeWeather()
    return obj

class TestForWeather(unittest.TestCase):

    @patch('urllib.request.urlopen', fake_urlopen)
    def test_get_city_temp(self):
        city='Aligarh'
        got_temp=forweather.get_city_temp(city)
        self.assertEqual(got_temp,16.32)

if __name__ == '__main__':
    unittest.main()