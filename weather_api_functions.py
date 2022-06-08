import requests
import pprint

the_key = 'df0dbcedccd9b8205dda92325771e2b7'


#pings API and returns json list of city info
def getInformationForCityCoord(lat, lon):
    response = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}'
                            f'&lon={lon}&appid={the_key}')
    cityObj = response.json()
    return cityObj

#input is the respons object from the api ping
#queries list and returns
def getDayinfo(totalcityinfo, daysout):
    return totalcityinfo['list'][daysout]