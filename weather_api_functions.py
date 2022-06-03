import requests
import pprint

#pings API and returns json list of city info
def getInformationForCityName(cityName):
    response = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q={}&'
                            'mode=json&units=imperial&cnt=7'.format(cityName))
    cityObj = response.json()
    return cityObj

#input is the respons object from the api ping
#queries list and returns
def getDayinfo(totalcityinfo, daysout):
    return totalcityinfo['list'][daysout]