import urllib.request
import urllib.parse
import json
from api import _getapikey
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def load_home_page():
    return render_template('city.html')

@app.route('/city',methods = ['POST', 'GET'])
def take_input():
    if request.method == 'POST':
        city = request.form['nm']
        return redirect(url_for('success',city = city))
    else:
        city = request.args.get('nm')
        return redirect(url_for('success',city = city))

@app.route('/success/<city>')
def success(city):
    weather_temp=get_city_temp(city)
    return 'Temperature of %s is %s' % (city, weather_temp)

def get_city_temp(city):
    apikey=_getapikey()
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
    return weather_temp
   
if __name__ == '__main__':
    app.run(host="0.0.0.0")
    