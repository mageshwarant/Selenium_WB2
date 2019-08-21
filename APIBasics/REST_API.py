import requests
import json

BASE_URL ="https://reqres.in"
data ={
    "name": "morpheus",
    "job": "leader"
}
response =requests.post(BASE_URL+"/api/user",data=data)

print(response.json())

params = {"page": 2}

req =requests.get(BASE_URL+"/api/users",params=params)

print(req.json())

payload={
    "name": "morpheus",
    "job": "zion resident"
}
req1= requests.put(BASE_URL+"/api/users",data=payload)

print(req1.json())
req1= requests.delete(BASE_URL+"/api/users/2")
print(req1.status_code)
#############################################

from APIBasics.keys import *

url ='https://api.openweathermap.org/data/2.5/weather?q=London&APPID='+ WEATHER_API_KEY

resp= requests.get(url)
print(resp.json())


#
#
# print(response.status_code)
# print(response.text)
# print(response.content)
# print(response.headers)
# print(json.dumps(response.json(),indent=4))
# print(json.dumps(req.json(),indent=4))
# print(response.json())
# #
# #
# # requests.post()