import mysql.connector
import re

cnx = mysql.connector.connect(user='root', password='armin2500', host='127.0.0.1', database='info')
cursor = cnx.cursor()

while True:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if re.match(r"[^@]+@[^@]+\.[^@]+",username):
        # insert user name & password into database
        cursor.execute('INSERT INTO information VALUES (\'%s\',\'%s\')' % (username, password))
        cnx.commit()
        cnx.close()
        quit(0)

    else:
        print(f' correct:\n expression@string.string\n Try Again!\n')
        continue
