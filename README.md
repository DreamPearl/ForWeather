# ForWeather ![Python application](https://github.com/DreamPearl/ForWeather/workflows/Python%20application/badge.svg)

### Application to display weather report

#### Please find api keys from https://home.openweathermap.org/api_keys

### Usage 1 [Git clone]:
- Clone the repository.
   - `git clone https://github.com/DreamPearl/ForWeather.git`

   - `cd ForWeather` 
- Build docker image. 
   - `docker build --tag forweather:1.0 .` 

- Run docker image. 
   - `docker run --name forweather -i -e OPENWEATHER_API_KEY='<Enter your api key here>' forweather:1.0`  

   OR (edit api key within file name api.py)

   - `docker run --name forweather -i forweather:1.0`
 

### Usage 2 [Pull docker image]:
- Pull docker image. 
    - `docker pull dreampearl/forweather:1.0` 

- Run docker image. 
    - `docker run --name forweather -i -e OPENWEATHER_API_KEY='<Enter your api key here>' forweather:1.0` 


#### Enjoy the application :)
