import requests

req = requests.get('http://localhost:8000/add/123123/Максим/')
print(req.text)