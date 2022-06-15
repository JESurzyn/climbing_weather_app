#program files
import db_functions, j_weather, users
#import pandas as pd

#defining start program function
def StartProgram():
    print('\n','*'*80)
    print('''
    BAY AREA CLIMBING TEMPS:
    
    The program will return a list of local bouldering 
    areas that match your preferences for temperature and humidity; additionally, 
    the list will not include any areas where it is forecasted to rain.
    
    Happy Climbing!
    ''')
    print('*'*80,'\n')

    ##### first login user flow ####
    """
    In first login user flow, the user has not yet run the program at all
    Items that need to be done:
    
    1. create a local database to house user information/preferences so that
    they can be recalled later
    
    2. log user information
    
    3. save user information to database
    """
    #CreateDB checks if user db exists and creates if doesn't
    #this should eventually be hosted so the creation process is not local to the user
    db_functions.CreateDB()

    #querying locations db - this should be hosted eventually
    locations_df = db_functions.queryLocations()
    locations_list = locations_df['name'].tolist()

    #User login
    #with web app should be a normal login form/button
    login_action = input('Create a new user profile? ')
    if login_action.lower().strip() == 'yes':
        first_user = users.NewUserInstance()
        db_functions.saveUser(first_user)
        climbday = j_weather.dayIndex()

        #creates list of city attributes
        city_data_list = []
        for location in locations_list:
            lat = locations_df.loc[locations_df['name'] == location,'lat'].values[0]
            lon = locations_df.loc[locations_df['name'] == location, 'lon'].values[0]
            cityInstance = j_weather.CreateCityInsta(location,lat,lon,climbday)
            city_data_list.append(cityInstance)

        city_matches = j_weather.MatchList(city_data_list, first_user)
        print('\n')
        for locations in city_matches:
            print(locations)
        print('\n The above areas fit your criteria. Happy Climbing! \n')
        print('*'*80)

        quit_option = input('Type \"quit\" to exit, enter anything else to run the program again. ')
        if quit_option == 'quit':
            quit()





        """
        below just for unit testing
        """
        # print('from first_user object')
        # print(first_user.name, '\n')
        # print(first_user.temp, '\n')
        # print(first_user.humid, '\n'*3)
        # print(db_functions.queryAll())
    else:
        """
        unit testing below
        """
        print('too bad can only create users right now')

        """
        testing only
        """
        quit()



#will run if script is called from command line

if __name__=='__main__':
    StartProgram()