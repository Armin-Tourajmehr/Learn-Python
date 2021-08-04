# Continue until the number less than or equal 1

def FindCountNumber(collatz, count=0):
    '''
    Return Count
    at the beginning count = 0 and after each calculation
    one is added to it

    :param collatz: Input number
    :param count: it counts when finds number that would be less than or equal 1
    :return: return count
    '''
    if collatz <= 1:
        return count
    if collatz % 2 == 0:
        return FindCountNumber(collatz / 2 , count + 1)
    elif collatz % 2 != 0:
        return FindCountNumber((collatz * 3) + 1, count + 1)


if __name__ == '__main__':
    user = int(input('Enter a number: '))
    print(FindCountNumber(user))