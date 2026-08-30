import configparser

from pathlib import Path
cfgFile= 'petsqa.ini'
cfgFileDir = 'config'
cfgFileFlaskApp = 'qa.ini'

config = configparser.ConfigParser()
configFlaskApp = configparser.ConfigParser()

BASE_Dir = Path(__file__).resolve().parent.parent
print(BASE_Dir)

CONFIG_FILE= BASE_Dir.joinpath(cfgFileDir).joinpath(cfgFile)
CONFIG_FILE_FLASK= BASE_Dir.joinpath(cfgFileDir).joinpath(cfgFileFlaskApp)

config.read(CONFIG_FILE)
configFlaskApp.read(CONFIG_FILE_FLASK)


def getPetAPIURL():
    return config['pet']['url']

def getStoreAPIURL():
    return config['store']['url']

def getFlaskAppBaseURL():
    baseURL = configFlaskApp['flask']['url'] + ':' + configFlaskApp['flask']['port'] + '/api/'
    return baseURL


print(getPetAPIURL())
print(getStoreAPIURL())
print(getFlaskAppBaseURL())

