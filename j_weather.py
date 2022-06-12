import weather_api_functions as waf

# prompts user for when they are planning to climb
# will be used to ping the climbing weather api
def dayIndex():
    days_out = input('\nIn how many days are you planning to climb? (Choose between 0, meaning today, and 8 days).')
    return days_out

# city weather class
class CityWeather:
    def __init__(selfself, name, Temp, Humidity, Raining):
        self.name = name
        self.Temp = Temp
        self.Humidity = Humidity
        self.Raining = Raining

# calls the api function to get json respons for each city
# each function grabs a relevant piece of info from response object ex. day info, temp, humid, etc.
def CreateCityInsta(name, lat,lon, climbday):
    cityName = name
    info = waf.getInformationForCityCoord(lat,lon)
    dayinfo = info['daily'][climbday]
    cityTemp = dayinfo['temp']['day']
    cityHumid = dayinfo['humidity']
    # Probability of precipitation. The values of the parameter vary between 0 and 1, where 0
    # is equal to 0%, 1 is equal to 100%
    cityRain = dayinfo['pop']
    return CityWeather(cityName, cityTemp, cityHumid, cityRain)

