import requests
import json

BASE_URL ="https://reqres.in"
data ={
    "name": "morpheus",
    "job": "leader"
}
response =requests.post(BASE_URL+"/api/user",data=data)

print(response.status_code)
print(response.text)
print(response.content)
print(response.headers)
print(json.dumps(response.json(),indent=4))
# print(response.json())
# #
# #
# # requests.post()