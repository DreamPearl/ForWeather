import urllib.request
import urllib.parse
import json

from api import apikey

def take_input():
	city=input('Please Enter City Name: ').strip()
	en_city=urllib.parse.quote(city)
	return en_city

def fetch_weather(city):
	try:
	    url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+apikey+'&units=metric'
	    f=urllib.request.urlopen(url)
	    mydata=f.fread()
	except Exception as e:
	    print('Error in finding temperature. \n '+str(e))
	    exit(-1)
	return mydata

def print_weather(data,city):
	y=json.loads(data)
	weather_temp=y['main']['temp']

	print('The temperature in '+city+' is '+str(weather_temp))

def main():
	city=take_input()
	data=fetch_weather(city)
	print_weather(data,city)

if __name__ == '__main__':
	main()
