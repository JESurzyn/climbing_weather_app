import requests

def getInformationForCityName(cityName):
    response = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q={}&'
                            'mode=json&units=imperial&cnt=7'.format(cityName))
    cityObj = response.json()
    return cityObj