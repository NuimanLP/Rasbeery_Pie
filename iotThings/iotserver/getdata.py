import requests

url = 'http://192.168.1.109:8000/apitest'

data = {'token':'abc1234'}
r = requests.get(url=url,data=data)

print(r.json())