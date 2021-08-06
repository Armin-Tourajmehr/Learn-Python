import datetime  # get time

import gtts
from playsound import playsound  # play song

# this function checks valid or not valid time
def valid_time(user_time):
    if len(user_time) != 11:
        return 'Invalid time format'
    else:
        if int(user_time[:2]) > 24:
            return f'Invalid Hours time,{user_time[:2]} time must be less than 24'
        elif int(user_time[3:5]) > 59:
            return f'Invalid minute time,{user_time[3:5]} time must be less than 60'
        elif int(user_time[6:8]) > 59:
            return f'Invalid second time,{user_time[6:8]} time must be less than 60'
        else:
            return 'OK'


while True:
    user_time = input('Enter your time that want to set\n'
                      'like this format HH:MM:SS AM/PM: ')
    validate = valid_time(user_time).lower()
    if validate != 'ok':
        print(validate)
    else:
        print(f'setting your time is {user_time}')
        break

while True:
    time_online = datetime.datetime.now().strftime('%H:%M:%S %p')
    if time_online == user_time:
        print('Wake up')
        # You can download or upload your music in root of file
        playsound('(name of song).mp3', True) # e.g : playsound('classical.mp3',True)
        break
