import requests


def check_internet(url='https://www.google.com/', timeout=5):
    try:
        req = requests.head(url, timeout=timeout)
        req.raise_for_status()
        print('Your Internet Connected')
        return True
    except requests.HTTPError as error:
        print("Checking internet connection failed, status code {0}.".format(
            error.response.status_code))
    except requests.ConnectionError as con:
        print("No internet connection available {0}".format(con))
    return False


if __name__ == '__main__':
    check_internet()
