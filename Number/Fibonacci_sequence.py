# Enter a number and have the program generate
# The Fibonacci sequence number or the nth number

def Fibonacci_sequence(n):
    '''
    Return Fibonacci

    :param n using for digit that user want to calculator Fibonacci:
    :return sequence number as Fibonacci :
    '''
    # Initialization number
    a = 1
    b = 1
    for i in range(n):
        a, b = b, b + a
        yield b


def ValidInput(n):
    '''
    Return True or False

    :param n: Get number
    :return: True if number will be correct or versa vise
    '''
    try:
        number = int(n)
    except ValueError:
        print('Enter an integer')
    else:
        print('Wait.....')
        return True


if __name__ == '__main__':

    while True:
        user = input('Please Enter a number: ')
        if ValidInput(user):
            n = int(user)
            for i in Fibonacci_sequence(n):
                print(i)
            break
        else:
            continue
