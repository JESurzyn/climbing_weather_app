class User:
    def __init__(self, name, temp, humid):
        self.name = name
        self.temp = temp
        self.humid = humid

def NewUserInstance():
    user_name = input('\nCreate your username.  ')
    temperature = input('\nEnter your temperature preference in Farenheit.\n'
                        'Simply enter an integer like \"60\".  No need to add degrees.\n')
    humidity = input('\nEnter the highest percentage humidity you are willing to climb in.'
                     '\nA number around 80 percent seems reasonable for this area.\nAs above, '
                     'just enter an integer.  No need to enter a percentage sign.\n')
    new_instance = User(user_name, temperature, humidity)
    return new_instance