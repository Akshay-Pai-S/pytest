from utils.myutils import getAPIData, putData, delData
from utils.myconfigparser import *

import logging
LOGGER = logging.getLogger(__name__)

# baseURL = "https://petstore.swagger.io/v2/pet/"
petID = '151'
baseURL = getPetAPIURL()

def test_getPetByID_responce():
    url= baseURL + petID
    data, status, time = getAPIData(url)
    assert data['id'] == int(petID)
    assert status == 200
    print('Time Taken: ', time)

def test_updatePet():
    payload = {'id':petID, 'name':'cat', 'status':'pending'}
    data, resp_status, timeTaken = putData(baseURL, payload)
    LOGGER.info('Update API call done')
    assert resp_status == 200
    assert data['id'] == int(petID)
    print(data)
    print('Time Taken: ', timeTaken)

def test_deletePetbyId():
    url= baseURL + petID
    apiKey={'api_key': 'key123'}
    data, resp_status, timeTaken = delData(url, apiKey)
    print(data)
    assert resp_status == 200