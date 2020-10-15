import os
import subprocess as s


def ping():
    hostname = input("Enter the name of website you want to check :")
    response = os.system("ping -c 1 " + hostname + " > /dev/null 2>&1")
    if response == 0:
        print(hostname + " is up !")
        print("\U0001f600")
        s.call(['notify-send', 'Requested Host is UP'])

    else:
        print(hostname + " is down !")
        s.call(['notify-send', 'Requested Host is DOWN :)'])


ping()
