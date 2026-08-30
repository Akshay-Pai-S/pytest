import requests, json

baseURL = "https://petstore.swagger.io/v2/pet/"
petID = '151'

def test_getPetByID_responce():
    url= baseURL + petID
    headers =  {'content-type': 'application/json'}
    print('Request URL: ' + url)
    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    print(json.dumps(data, indent=3))
    assert len(data) > 0 , 'Empty response'

def test_getPetByID_id():
    url= baseURL + petID
    headers = {'content-type': 'application/json'}
    print('Request URL: ' + url)
    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    assert data['id'] == 151

def test_addNewPet():
    url = baseURL
    headers = {'content-type': 'application/json'}
    payload = {'id' : 152, 'name' : 'Tommy', 'status' : 'available'}
    response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
    data = response.json()
    print(json.dumps(data, indent=3))
    assert len(data) > 0 , 'Empty response'
    assert data['id'] == 152