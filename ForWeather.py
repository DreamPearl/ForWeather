import urllib.request
import urllib.parse
import json

from api import apikey

city=input('Please Enter City Name: ').strip()
en_city=urllib.parse.quote(city)

try:
    url='http://api.openweathermap.org/data/2.5/weather?q='+en_city+'&appid='+apikey+'&units=metric'
    f=urllib.request.urlopen(url)
    mydata=f.read()
except Exception as e:
    print('Error in finding temperature. \n '+str(e))
    exit(-1)

y=json.loads(mydata)
weather_temp=y['main']['temp']

print('The temperature in '+city+' is '+str(weather_temp))
