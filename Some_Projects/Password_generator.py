# This program generate random password

from string import ascii_letters
from random import choice


def password_generator(length):
    char = '~!@#$%^&*()_+|}{":?></;][=\/-1234567890'
    ascii = ascii_letters + char
    if length > len(ascii):
        return f'Length your password should be less than {len(ascii)}'
    else:
        Pass = []
        lengths = length
        while lengths > 0:
            character = choice(ascii)
            if character in Pass:
                continue
            else:
                Pass.append(character)
                lengths -= 1
        return ''.join(Pass)


if __name__ == '__main__':
    length = int(input('how long will be your password: '))
    print(password_generator(length))
