import pytest

from utils.apiUtils import postAPIData
from utils.myconfigparser import getFlaskAppBaseURL
from utils.fileUtils import getJsonFromFile

loginJSONFile = 'loginValid.json'
baseuri = getFlaskAppBaseURL()
loginUrlPath = 'login'

@pytest.fixture
def get_token():
    loginURL = baseuri + loginUrlPath
    payload = getJsonFromFile(loginJSONFile)
    r = postAPIData(loginURL, payload)
    token = r.json()['token']
    print(token)
    yield token