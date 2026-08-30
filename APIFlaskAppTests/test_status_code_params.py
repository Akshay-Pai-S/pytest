import pytest

from utils.apiUtils import getAPIData
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
urlPath = 'allusercount'

test_data= [
    ('application/json', 200),
    ('application/xml', 406),
    ('multipart/mixed', 406),
    ('text/html', 200)
]

@pytest.mark.parametrize('type , status', test_data)
def test_getAllUserStatus(type, status):
    url = baseURI + urlPath
    headers = {'Accept': type}
    resp=getAPIData(url, headers)
    print(resp.status_code)
    assert resp.status_code == status