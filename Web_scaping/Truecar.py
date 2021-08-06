'''
This is just a Web Scraping project, in this project we enter just a name of car
and the it stores the Price and function of the first 20 people who
sell the car in https://www.truecar.com, in database that you write in mysql
'''

# First Create a database in mysql and then
# import mysql.connector
import mysql.connector
from bs4 import BeautifulSoup
import requests
import re

cnx = mysql.connector.connect(user='root', password='****', host='127.0.0.1', database='car')
cursor = cnx.cursor()

url = 'https://www.truecar.com/used-cars-for-sale/listings/'
model_car = input('Enter model: ')
url += model_car
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
link = soup.find_all('a', attrs={'class': 'linkable order-2 vehicle-card-overlay'})
cars = []
for h in link:
    cars.append(h.get('href'))
    if len(cars) == 20:
        break

for href in cars:
    # change url and add links into List of cars
    new_url = str(re.sub(r'/used-cars-for-sale/listings/', href, url))

    new_html = requests.get(new_url)
    link_of_price = BeautifulSoup(new_html.text, 'html.parser')
    price = link_of_price.find_all('div', attrs={'class': 'label-block-text'})
    miles = link_of_price.find_all('span', attrs={'data-qa': 'used-vdp-header-miles'})
    for p, m in zip(price, miles):
        cursor.execute('INSERT INTO model VALUES (\'%s\',\'%s\')' % (p.text, m.text))
        cnx.commit()
        # price
        # print(p.text)
        # miles
        # print(m.text)

        # 'Miles' is removed by below code
        # m = re.findall(r"^\d+\,\d+",j.text)
        # print(m[0])

cnx.close()
