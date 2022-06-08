import weather_api_functions as waf

#prompts user for when they are planning to climb
#will be used to ping the climbing weather api
def dayIndex():
    days_out = input('\nIn how many days are you planning to climb? (Choose between 1 and 7 days).')
    days_index = days_out - 1
    return days_index

#calls the api function to get json respons for each city
#each function grabs a relevant piece of info from response object ex. day info, temp, humid, etc.
def CreateCityInsta(lat,lon, climbday):
    info = waf.getInformationForCityCoord(lat,lon)
    dayinfo = waf.getDayinfo(info, climbday)
    cityTemp = waf.getTemp(dayinfo)
    cityHumid = getHumidity(dayinfo)
