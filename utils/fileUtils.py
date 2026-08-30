import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

print('Base Directory:', BASE_DIR)

TEST_DATA_DIR = BASE_DIR.joinpath('TestData')
print('Test Data Directory:', TEST_DATA_DIR)

def getJsonFromFile(filename):
    filename = TEST_DATA_DIR.joinpath(filename)
    with open(filename, 'r') as f:
        return json.load(f)

def getCsvDataAsDict(filename):
    filename = TEST_DATA_DIR.joinpath(filename)
    with open(filename, 'r') as f:
        csvFile = csv.DictReader(f)
        dictList = list(csvFile)
    return dictList

def getDataAsList(filename):
    filename = TEST_DATA_DIR.joinpath(filename)
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        lines = list(reader)
    return lines

#return list of tuples. With list of inputs and scalar of output status.
def getDataAsTuple(filename):
    dataList=getDataAsList(filename)
    newList= [(line[:2],line[2]) for line in dataList]
    return newList

# print(getCsvDataAsDict('registerAPIData.csv'))
print(getDataAsTuple('registerApiDataWithStatus.csv'))