import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests

r = SimpleMFRC522()

try:
    id, slug = r.read()
    print(slug)
    url = 'http://0:8000/add/{}'.format(str(slug.replace(' ','')))
    print(url)
    req = requests.get(url)
    print(req.text)
finally:
    GPIO.cleanup()