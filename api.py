# Please find api keys from https://home.openweathermap.org/api_keys

import os

def _getapikey():
    try:
        apikey=os.environ['OPENWEATHER_API_KEY']
    except KeyError:
        apikey='60196c37f5a29d2f98931642c7eedb6a'
    return apikey