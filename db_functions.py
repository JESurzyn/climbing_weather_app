import sqlite3

# function to create the db
#checks if db exists
    #if exists, open and close
    #if doesn't exist, creates db, creates table, closes db
def CreateDB():
    sql = '''create table weather_users (
                name text, 
                temperature real,
                humidity real)'''
    #db already exists
    try:
        conn = sqlite3.connect('file:users_data.db?mode=rw', uri=True)
        #just opens and closes db
        cursor = conn.cursor()
        cursor.close()
    #db does not exist
    except sqlite3.OperationalError:
        conn = sqlite3.connect('file:users_data.db?mode=rwc', uri=True)
        cursor = conn.cursor()
        #runs sql to create table
        cursor.execute(sql)
        cursor.close()