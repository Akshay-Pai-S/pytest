from utils.fileUtils import getJsonFromFile
from utils.apiUtils import getAPIData, postAPIData
from utils.myconfigparser import getFlaskAppBaseURL

loginJSONFile = 'loginValid.json'
baseuri = getFlaskAppBaseURL()

loginUrlPath = 'login'
userUrlPath = 'users'

def test_getUserDemo():
    loginURL = baseuri + loginUrlPath
    payload = getJsonFromFile(loginJSONFile)
    r= postAPIData(loginURL, payload)
    token = r.json()['token']
    print(token)
    userURL = baseuri + userUrlPath
    headers = {'x-access-token': token}
    resp= getAPIData(userURL, headers)
    print(resp.json())