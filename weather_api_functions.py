import requests
import pprint

the_key = 'df0dbcedccd9b8205dda92325771e2b7'


#pings API and returns json list of city info
def getInformationForCityCoord(lat, lon):
    response = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}'
                        f'&lon={lon}&units=imperial&exclude=current,minutely,hourly,alerts&appid={the_key}')
    cityObj = response.json()
    return cityObj




