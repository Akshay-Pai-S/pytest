import random
import pytest
from utils.apiUtils import postAPIData, deleteAPIData
from utils.fileUtils import getJsonFromFile
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
regURLPath = 'register'
loginURLPath = 'login'
delPath = 'delete'
registerJsonFile = 'registerAPIvalid.json'
randNum=random.randint(1,1000)
email='automateUser@auto'+str(randNum)
password='1234'


@pytest.fixture(scope='module')
def reg_user():
    print('Setup')
    payload=getPayloadDict_RegAPI(email,password)
    regURL=baseURI+regURLPath
    reg_resp=postAPIData(regURL, payload)
    assert reg_resp.status_code == 201
    assert reg_resp.json()['id']
    data=reg_resp.json()
    print('Yield data')
    yield data
    print('Teardown')
    delUrl=baseURI+delPath
    loginURL=baseURI+loginURLPath
    loginResp=postAPIData(loginURL,payload)
    token=loginResp.json()['token']
    headers={'x-access-token': token}
    payload={'id':reg_resp.json()['id']}
    del_resp=deleteAPIData(delUrl,payload, headers)
    assert del_resp.status_code == 200
    assert del_resp.json()['id'] == reg_resp.json()['id']
    print('Delete data')


def test_loginCorrectCred(reg_user):
    payload=getPayloadDict_RegAPI(email,password)
    url=baseURI+loginURLPath
    resp=postAPIData(url, payload)
    assert resp.status_code == 200

def test_loginEmptyPassword(reg_user):
    data=reg_user
    payload=getPayloadDict_RegAPI(email,'')
    url=baseURI+loginURLPath
    resp=postAPIData(url, payload)
    assert resp.status_code == 401


def getPayloadDict_RegAPI(email=None,password=None):
    payload=getJsonFromFile(registerJsonFile)
    payload['email']=email
    payload['password']=password
    return payload