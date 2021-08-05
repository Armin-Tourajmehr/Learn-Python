from time import *
from datetime import *

host_path = r"C:\windows\system32\drivers\etc\hosts"
# This is LocalHost
redirect = "127.0.0.1"
# This is just an example
websites = ["www.facebook.com", "https://www.facebook.com"]

while True:
    # compare between datetime now and another datetime that you want
    if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 9) < datetime.now() < datetime(
            datetime.now().year, datetime.now().month, datetime.now().day, 17):
        # READ File
        with open(host_path, "r+") as fileptr:
            content = fileptr.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    fileptr.write(redirect + "        " + website + "\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    sleep(5)