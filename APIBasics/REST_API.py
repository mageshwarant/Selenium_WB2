import requests
import json

BASE_URL ="https://reqres.in"

response =requests.get(BASE_URL+"/api/users?page=2")

print(response.status_code)
print(response.text)
print(response.content)
print(response.headers)

# print(response.json())
# # print(json.dumps(response.json(),indent=4))
# #
# # requests.post()