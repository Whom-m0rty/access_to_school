import RPi.GPIO as GPIO
import requests


try:
	first_name = input('First_name: ')
	surname = input('Surname')
	patronymic = input('Patronymic: ')
	email = input('Email: ')
	req = requests.get('http://0:8000/{}/{}/{}/{}'.format(first_name,surname, patronymic, email))
	print(req.text)
except:
	pass
