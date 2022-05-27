#program files
import db_functions
import users

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
    #CreateDB checks if db exists and creates if doesn't
    db_functions.CreateDB()

    #User login
    #with web app should be a normal login form/button
    login_action = input('Create a new user profile? ')
    if login_action.lower().strip() == 'yes':
        first_user = users.NewUserInstance()
        """
        below just for unit testing
        """
        print(first_user.name, '\n')
        print(first_user.temp, '\n')
        print(first_user.humid)
    else:
        """
        unit testing below
        """
        print('too bad can only create users right now')





#will run if script is called from command line

if __name__=='__main__':
    StartProgram()