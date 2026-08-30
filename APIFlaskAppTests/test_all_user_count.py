from utils.apiUtils import getAPIData
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
urlPath = 'allusercount'

def test_allUserCountStatus200():
    url= baseURI + urlPath
    headers= {'Accept': 'application/json'}
    resp=getAPIData(url,headers)
    assert resp.status_code == 200

def test_allUserCountStatus406():
    url= baseURI + urlPath
    resp=getAPIData(url)
    assert resp.status_code == 406

def test_allUsercountBody():
    url = baseURI + urlPath
    headers = {'Accept': 'application/json'}
    resp = getAPIData(url, headers)
    data = resp.json()
    assert data['count']
    assert data['status']
    assert data['status']['message'] == 'success'

def test_allUserCountTimeTaken():
    url = baseURI + urlPath
    headers = {'Accept': 'application/json'}
    resp = getAPIData(url, headers)
    time_taken=resp.elapsed.total_seconds()
    assert time_taken<0.005