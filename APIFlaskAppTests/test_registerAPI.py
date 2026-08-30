from utils.apiUtils import postAPIData
from utils.fileUtils import getJsonFromFile
from utils.myconfigparser import getFlaskAppBaseURL

baseURL = getFlaskAppBaseURL()
urlPath = 'register'
registerJSONFile = 'registerAPIvalid.json'

def test_registerAPI():
    url=baseURL+urlPath
    payload = getJsonFromFile(registerJSONFile)
    print('\nPayload: ',payload)
    r=postAPIData(url, payload)
    print(r.json())
    assert r.status_code == 201