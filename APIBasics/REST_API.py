import requests
import json

BASE_URL ="https://reqres.in"
data ={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
response =requests.post(BASE_URL+"/api/register",data=data)

print(response.status_code)
print(response.text)
print(response.content)
print(response.headers)
print(json.dumps(response.json(),indent=4))
# print(response.json())
# #
# #
# # requests.post()