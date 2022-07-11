# (library concept) this program generates a random password with combination of the date of the actual day 
# Built by @jwan.yaw

import datetime
import string
import random

# save all characters in a list
characters = list(string.digits + string.ascii_letters + "!@#$%^&*()")

# the password generation function
def generate_random_password():
    # define the length of the password
    length = int(input("Länge des Passwortes angeben: "))

    # mix the characters
    random.shuffle(characters)

    # save the password as a string
    now = datetime.datetime.now()
    date_string = now.strftime('%d-%m-%Y')

    # choose a random character and add it to the password variable
    password = []
    password.append(date_string)
    for i in range (length):
        password.append(random.choice(characters))
    
    # convert the password to a string
    print("".join(password))

# Invoking the function
generate_random_password()


