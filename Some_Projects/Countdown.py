# Countdown Clock and Timer
# Let's make the countdown
from time import sleep
import gtts
from playsound import playsound


def countdown(hours, minutes, seconds):
    while hours > -1:
        while minutes > -1:
            while seconds > 0:
                seconds -= 1
                print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds),end='\r')
                sleep(1)
            minutes -= 1
            seconds = 60
        hours -= 1
        minutes = 59
        seconds = 60

    hours = 0
    if hours == 0:
        t1 = gtts.gTTS('Time over')
        t1.save('timer.mp3')
        playsound('timer.mp3')


def main():
    hours = int(input('Enter hours : '))
    minutes = int(input('Enter minutes : '))
    seconds = int(input('Enter second: '))
    print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds), end='\r')
    sleep(1)
    countdown(hours, minutes, seconds)


if __name__ == '__main__':
    main()
