import requests
import os
from dotenv import load_dotenv
load_dotenv()
the_key = os.environ.get('WEATHER_KEY')

#pings API and returns json list of city info
def getInformationForCityCoord(lat, lon):
    response = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}'
                        f'&lon={lon}&units=imperial&exclude=current,minutely,hourly,alerts&appid={the_key}')
    cityObj = response.json()
    return cityObj




