import sqlite3


# function to create the db
# checks if db exists
# if exists, open and close
# if doesn't exist, creates db, creates table, closes db
def CreateDB():
    sql = '''CREATE TABLE weather_users (
                name text, 
                temperature real,
                humidity real)'''
    # db already exists
    try:
        conn = sqlite3.connect('file:users_data.db?mode=rw', uri=True)
        # just opens and closes db
        cursor = conn.cursor()
        cursor.close()
    # db does not exist
    except sqlite3.OperationalError:
        conn = sqlite3.connect('file:users_data.db?mode=rwc', uri=True)
        cursor = conn.cursor()
        # runs sql to create table
        cursor.execute(sql)
        cursor.close()


# function to save the user info to db when created
def saveUser(user):
    sql = '''
    INSERT INTO weather_users (name, temperature, humidity)
    VALUES (:nam, :temp, :hum)'''
    conn = sqlite3.connect('users_data.db')
    cursor = conn.cursor()
    cursor.execute(sql, {'nam': user.name, 'temp': user.temp, 'hum': user.humid})
    conn.commit()
    cursor.close()

#function to query database for all records and return
# for testing purposes
def queryAll():
    sql = '''
    SELECT *
    FROM weather_users
    '''
    conn = sqlite3.connect('users_data.db')
    cursor = conn.cursor()
    results = cursor.execute(sql)
    readout = results.fetchall()
    return readout
    cursor.close()

