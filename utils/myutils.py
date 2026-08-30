import requests, json

# get API call return response data
def getAPIData(url):
    headers = {'content-type': 'application/json'}
    print('\nRequest URL: ' + url)
    response = requests.get(url, headers=headers, verify=False)
    data= response.json()
    print(json.dumps(data, indent=4))
    assert len(data)>0, 'Empty Response'
    timeTaken= response.elapsed.total_seconds()
    return data, response.status_code, timeTaken

def putData(url, body):
    headers = {'content-type': 'application/json'}
    print('\nRequest URL: ' + url)
    print('ReqBody: ', json.dumps(body, indent=4))
    response = requests.put(url, verify=False, json=body, headers=headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken

def delData(url, opHeader=None):
    headers = {'content-type': 'application/json'}
    print('\nRequest URL: ' + url)
    headers=(headers | opHeader) if isinstance(opHeader, dict) else headers
    response = requests.delete(url, verify=False, headers=headers)
    print(response.headers)
    print(response.request.headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken