import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

url = 'https://httpbin.org/digest-auth/auth/1234/1234'
auth = HTTPDigestAuth('1234', '1234')

def test_auth():
    headers = {'accept': 'application/json'}
    r= requests.get(url, headers=headers, auth=auth)
    print(r.status_code)
    assert r.status_code == 200