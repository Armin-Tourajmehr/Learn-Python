from random import choice


def flip_coin(times):
    heads = 0
    tails = 0
    for i in range(times):
        choices = choice([0, 1])
        if choices == 0:
            tails += 1

        elif choices == 1:
            heads += 1

    print(f'Heads: {heads}')
    print(f'Tails: {tails}')


def valid():
    while True:
        number = input('How many times do you want to run COINS and TAILS: ')
        try:
            times = int(number)
            if times > 50 or times < 1:
                print('Enter a number less than 50 and bigger than 0')
                continue
            else:
                flip_coin(times)
        except ValueError:
            print('Invalid Number,Try Again!!!')

        else:
            print('We hope see you soon')
            break


if __name__ == '__main__':
    valid()
