# Built by jwan.yaw

import datetime
import string
import random

# Alle Charakter in einer Liste speichern
characters = list(string.digits + string.ascii_letters + "!@#$%^&*()")

# funktion, um das Passwort zu bilden
def generate_random_password():
    # Länge des Passwortes bestimmen
    length = int(input("Länge des Passwortes angeben: "))

    # Die Charakter mischen
    random.shuffle(characters)

    # Ein Password als String speichern
    now = datetime.datetime.now()
    date_string = now.strftime('%d-%m-%Y')

    # ein beliebiges Charakter von einer Liste auswählen und zur Password Variable hinzufügen
    password = []
    password.append(date_string)
    for i in range (length):
        password.append(random.choice(characters))
    
    # Liste in einen String umwandeln
    print("".join(password))

# Invoking the function
generate_random_password()


