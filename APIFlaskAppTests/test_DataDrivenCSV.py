import pytest

from utils.fileUtils import getCsvDataAsDict, getDataAsTuple
from utils.apiUtils import postAPIData
from utils.myconfigparser import getFlaskAppBaseURL

baseURL = getFlaskAppBaseURL()

dataFile = 'registerAPIData.csv'
dataFileWithStatus = 'registerApiDataWithStatus.csv'
urlPath = 'register'

getData=getDataAsTuple(dataFileWithStatus)

def test_dataDrivenRegApi():
    url=baseURL + urlPath
    payloadList=getCsvDataAsDict(dataFile)
    for dataLines in payloadList:
        print(dataLines)
        resp=postAPIData(url,dataLines)
        assert resp.status_code == 201
        data=resp.json()
        print(data)
        assert data['id']



#using parameterization
@pytest.mark.parametrize('input, respStatus', getData)
def test_dataDriven(input, respStatus):
    url=baseURL + urlPath
    keys=['email', 'password']
    requestDict=dict(zip(keys, input))
    print('req data', requestDict, respStatus)
    resp=postAPIData(url,requestDict)
    assert resp.status_code == int(respStatus)