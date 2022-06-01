import weather_api_functions as waf

#prompts user for when they are planning to climb
#will be used to ping the climbing weather api
def dayIndex():
    days_out = input('\nIn how many days are you planning to climb? (Choose between 1 and 7 days).')
    days_index = days_out - 1
    return days_index

def CreateCityInsta(name, climbday):
    info = waf.getInformationForCityName(name)
