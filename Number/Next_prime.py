# Ask user do you want to see a next Prime number

from collections import Counter


def IsPrime(n):
    # Return Prime Number
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def GenPrime(currentPrime):
    # Return Next Prime Number
    newPrime = currentPrime + 1

    while True:

        if not IsPrime(newPrime):
            newPrime += 1
        else:
            break
    return newPrime


def shall():
    currenPrime = 2

    while True:

        ask = input('Do you want to see the next prime (Y/N): ').lower()

        if ask == 'y' or ask == 'yes':
            print(currenPrime)
            currenPrime = GenPrime(currenPrime)

        elif ask == 'n' or ask == 'quit' or ask == 'no':
            print('Have a good time\nWe hope see you soon')
            break
        else:
            print('Invalid Input, Try Again!!!!')
            continue


if __name__ == '__main__':
    shall()
