import re

email = input()


def Check_Mail(email):
    # check email is valid or not
    check_mail = re.match(r"[^@]+@[^@]+\.[^@]+", email)
    if check_mail:
        print('OK')
    else:
        print('WRONG')


if __name__ == '__main__':
    Check_Mail(email)
