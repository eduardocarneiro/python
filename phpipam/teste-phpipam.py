import requests
import json

server = "http://10.11.58.12"
appid = "appid"
username = "admin"
password = "password"

baseurl = server + "/api/" + appid

res = requests.post(baseurl + '/user/', auth=(username, password))
#print(res.status_code)
#print(res.content)
token = json.loads(res.content)['data']['token']

res = requests.get(baseurl + '/sections/', headers={'token': token})
#print(res.status_code)
#print(res.content.json())
print(res.json())

print(" ")
res = requests.get(baseurl + '/subnets/', headers={'token': token})
#print(res.status_code)
#print(res.content.json())
print(res.json())

print(" ")
res = requests.get(baseurl + '/subnets/7/first_free', headers={'token': token})
#print(res.status_code)
#print(res.content.json())
print(res.json())

print(" ")
res = requests.get(baseurl + '/addresses/first_free/7', headers={'token': token})
#print(res.status_code)
#print(res.content.json())
print(res.json())

#res = requests.get(baseurl + '/sections/3/subnets/', headers={'token': token})
#print(res.status_code)
#print(res.content)

# reference
#https://gist.github.com/cl4u2/de6ed34cb948fbcdba0c71257d33fee5
#https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
#https://phpipam.net/api-documentation/
#https://pypi.org/project/requests3/
#https://requests.readthedocs.io/en/master/
#https://www.freecodecamp.org/news/python-read-json-file-how-to-load-json-from-a-file-and-parse-dumps/
