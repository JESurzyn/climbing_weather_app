import sqlite3

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

    ### first logical section, a try-except clause to check if database exists
    try:
        # if local database already exists clause
        # leads into either creating a table and creating user credentials
        # or leads to querying for existing user credentials
        conn = sqlite3.connect('file:users_data.db?mode=rw', uri=True)
        cursor = conn.cursor()
        cursor.close()
        '''
        below print is just for unit testing
        '''
        print('database found, opened, and closed')


    except sqlite3.OperationalError:
        # 1. create local database
        """
        uses sqlite3 but in web app will probably use SQLAlchemy
        """
        conn = sqlite3.connect('file:users_data.db?mode=rwc', uri=True)
        cursor = conn.cursor()
        sql = '''
            create table weather_users 
            (
            name text,
            temperature real,
            humidity real
            )
        '''
        cursor.execute(sql)
        cursor.close()
        '''
        below print is just for unit testing
        '''
        print('database created!')



#will run if script is called from command line

if __name__=='__main__':
    StartProgram()