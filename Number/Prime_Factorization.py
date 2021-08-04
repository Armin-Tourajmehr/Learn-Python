# Prime Factorization
'''
Have the user number and find all
Prime factors (if there are any) and display them
'''

# Counter calculators how many Prime number there are
from collections import Counter


def isPrime(n):
    # 2 is prime
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def GetExponent(n):
    '''
    Counts the same elements in m list
    returns a list with the exponent of
    the multiple elements
    '''

    c = Counter(n)
    factors = []

    for i in range(min(n), max(n) + 1):
        if i in n:
            if c[i] != 1:
                factors.append(str(i) + '^' + str(c[i]))
            else:
                factors.append(str(i))
    return factors


def valid_number(n):
    try:
        number = int(n)
    except ValueError:
        print('Your number is not valid, Try again!!!!')
        return False
    else:
        return True


def main():
    """
    Calculate how many factors there is in entrance number
    Get number from user
    """
    factors = []

    while True:
        number = input('Enter a number to find its prime factors: ')
        # Check if number is valid or not
        valid = valid_number(number)
        if valid:
            break
        else:
            continue

    while True:

        if number == 0 or number == 1:
            break

        number = int(number)
        for i in range(2, number + 1):
            if number % i == 0:
                if isPrime(i):
                    factors.append(i)
                    number //= i
                    break

    if len(factors) != 0:
        factors = GetExponent(factors)
        print(','.join(factors))

    else:
        print(f'The number {int(number)} does not have any prime factors.')


if __name__ == '__main__':
    main()
