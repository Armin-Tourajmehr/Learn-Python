# Wikipedia Random Article
import requests
from bs4 import BeautifulSoup
import webbrowser


def random_article():
    while True:
        # it gets back random of article
        url = 'https://en.wikipedia.org/wiki/Special:Random'
        get_url = requests.get(url)
        # it parses url
        soup = BeautifulSoup(get_url.content, 'html.parser')
        # get back title
        title = soup.find('h1', {'class': 'firstHeading'}).text
        print('Title Of Article :',title)
        ans = input('\nDo you want to view it? (Y \ N \ Q): ').lower()

        if ans == 'y':
            new_url = 'https://en.wikipedia.org/wiki/%s' % title
            webbrowser.open(new_url)
            break
        elif ans == 'n':
            print('OK, Try again !!!')
            continue
        elif ans == 'q':
            print('Enjoy your day')
            quit(0)
        else:
            print('Wrong Choice')
            continue


if __name__ == '__main__':
    random_article()


