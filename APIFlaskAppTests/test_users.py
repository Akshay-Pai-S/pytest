import json

from utils.apiUtils import getAPIData
from utils.myconfigparser import getFlaskAppBaseURL

baseurl = getFlaskAppBaseURL()
userUrlPath = 'users'

#test get users with fixtures
def test_getUsers(get_token):
    token = get_token
    userURL = baseurl + userUrlPath
    headers = {'x-access-token': token}
    resp = getAPIData(userURL, headers)
    print(json.dumps(resp.json(), indent=4))
    assert resp.json()['users'][0]['email']