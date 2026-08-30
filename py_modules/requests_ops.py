import json

import requests

# url = 'https://www.google.com/search?q=pytest'
#
# r= requests.get(url)
# print(r.text)

# url = 'https://reqres.in/api/test-suite/collections/users/records'
#
# r=requests.get(url)
# print(r.status_code)
# print(r.headers)
# print(r.request.headers)
# print(r.text)
# print(r.json())


# print('\n*** request get - 3 ***\n')
# url = 'https://httpbin.org/get'
#
# myparams = {'key1': 'value1', 'key2': 'value2'}
#
# r=requests.get(url, params=myparams)
#
# print(r)
# print(r.url)
# print(r.status_code)
# print(type(r.text))
#
# for k,v in r.json().items():
#     print(k,' : ',v)
#
# print(r.json()['headers']['Host'])

print('\n*** request post ***\n')
url = 'https://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}
headers={'accept': 'application/json', 'Content-Type': 'application/json'}
# r = requests.post(url, data=json.dumps((payload)), headers=headers)
r = requests.post(url, json=payload, headers=headers)
print(r.url)
print(r.status_code)
print(r.text)
# print(r.request.headers)
# print(r.headers)