
# Getting pi number

# Use Nilakantha formula

from time import sleep

# Calculate Pi Number
def calc_pi(num):
    Pi = 3
    op = 1
    for n in range(num):
        if n % 2 == 0 and n > 1:
            yield Pi
            Pi += 4 / ((n) * (n + 1) * (n + 2) * op)
            op *= -1


def valid_number():
    while True:
        num = input('Enter a number for calculating Pi:\nHow many? ')
        try:
            number = int(num)
            if number > 100:
                print('Wait!!!!')
                return number
            else:
                print('Please choose number more than 100')
                continue
        except ValueError:
            print('Non negative number,Please try again!')


if __name__ == '__main__':
    number = valid_number()
    sleep(2)
    PI = None
    for i in calc_pi(number):
        PI = i
    print(PI)

