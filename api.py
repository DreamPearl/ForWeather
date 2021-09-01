# Please find api keys from https://home.openweathermap.org/api_keys

import os

def _getapikey():
    try:
        apikey=os.environ['OPENWEATHER_API_KEY']
    except KeyError:
        apikey='<Enter your api key here>'
    return apikey