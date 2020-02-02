import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests

r = SimpleMFRC522()

first_name = input('First_name: ')
surname = input('Surname: ')
patronymic = input('Patronymic: ')
email = input('Email: ')
try:
    req = requests.get('http://0:8000/add/{}/{}/{}/{}'.format(first_name,surname, patronymic, email))
    print(req.text)
    r.write(req.text)
    print('sucsess')
finally:
    GPIO.cleanup()
