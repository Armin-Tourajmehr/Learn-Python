# Find pi to nth digit

# Modules
# math gives square easily
# sys is needed to set up for reduction
# decimal gives the Decimal type which is much better than float

import sys
from decimal import *
from math import sqrt

getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)


def factorial(n):
    '''
    Return the factorial of a number using recursion

    Parameter ----> n
    number to get factorial of
    '''
    if not n:
        return 1
    return n * factorial(n - 1)


def getIteratedValue(k):
    """
    :param k -----> Number of Decimal Digits to get
    :return a iteration as given in the chudnovsky algorithm
    """
    k = k + 1
    getcontext().prec = k
    sum = 0

    for k in range(k):
        numerator = (factorial(6 * k) * (13591409 + 545140134 * k))
        denominator = factorial(3 * k) * ((factorial(k) ** 3) * (640320) ** (3 * k))
        sum += numerator / denominator
    return Decimal(sum)


def getValueOfPi(k):
    """
    Return the value of the pi using the iterated value of the loop
    and same division as given in the chudnovsky algorithm

    :param k -- Number of Decimal Digits upto which the value of Pi should be calculated:
    """

    iter = getIteratedValue(k)
    up = 426880 * sqrt(10005)
    pi = Decimal(up) / iter
    return pi


def shell():
    """
    Console function to create the interactive shell
    Runs only when __name__ == __main__ that is when script is being called directly

    :return Not anything value or parameter
    """

    print('Welcome to PI calculator')

    while True:
        entry = input('How many digits do you want to calculate from PI: ')
        try:
            valid = int(entry)
            if valid > 300:
                print('Your number must be less than 300')
                continue
            else:
                print(getValueOfPi(valid))
        except ValueError:
            print('The value is not valid, choose a integer')
            continue
        else:
            print('Have a good time')
            break


if __name__ == '__main__':
    shell()
