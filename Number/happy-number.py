# Find Happy Number
# A happy number is defined by numbers that sum of
# squares of its digits , and repeat process until
# the numbers equal 1

def GetNumber(number):
    """
    First define a list for saving digits
    Get a number, then does process for reminding 10 and append to list
    after that it'll separated number by 10
    """

    digits = []
    while number:
        digits.append(number % 10)
        number //= 10
    digits.reverse()
    return digits


def IsHappy(number):
    all_number = []

    while True:
        digits = GetNumber(number)
        # First squares any digits in digits
        # Then stores in list and finally sums all digits in list
        sum_squared_digits = sum(list(map(lambda x: x ** 2, digits)))

        if sum_squared_digits == 1:
            return True
        elif sum_squared_digits in all_number:
            return False
        else:
            number = sum_squared_digits
            all_number.append(number)


def main(number):
    happy_number = []
    counter = 0
    while counter < 8:
        if IsHappy(number):
            happy_number.append(str(number))
            counter += 1
        number += 1
    return happy_number

if __name__ == '__main__':

    while True:
        num = input('Enter a number: ')
        try:
            number = int(num)
            print(', '.join(main(number)))
            break
        except ValueError:
            print('Invalid Number!!!!')
            continue

