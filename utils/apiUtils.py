import requests, json

def getAPIData(url, opHeader = None):
    headers={'content-type': 'application/json'}
    headers=(headers | opHeader) if opHeader else headers
    response = requests.get(url, headers=headers, verify=False)
    print('\nRequest URL', url)
    print('Request Headers', response.request.headers)
    print('Response Headers:', response.headers)
    return response

def postAPIData(url, body):
    headers={'content-type': 'application/json'}
    print('\nRequest URL', url)
    print('Request Body', body)
    return requests.post(url, json=body, headers=headers, verify=False)

def deleteAPIData(url, body, opHeader = None):
    headers={'content-type': 'application/json'}
    headers=(headers | opHeader) if opHeader else headers
    response = requests.delete(url, headers=headers, json=body)
    print('\nRequest URL', url)
    print('Request Body', body)
    return response