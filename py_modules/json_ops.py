import json

dataDict = {
    "sampleString": "Great Automation Framework",
    "sampleList": ["Good", "Better", "Best"],
    "sampleTuple": ("Python", "Pytest", "Automation"),
    "sampleObj": {"platform": "Udemy", "Valuable": True},
    "sampleInteger": 555,
    "booleanValue": True,
    "noneValue": None
}

print('Dict to json')

resultJson= json.dumps(dataDict, sort_keys=True, indent=4)
# print(resultJson)
print(type(resultJson))

dataDict = json.loads(resultJson)
print(type(dataDict))
print(dataDict)

with open('example.json','r') as  file:
    data = json.load(file)
    print(data.keys())
    print(type(data['address']))
    for k,v in data.items():
        print(f'{k}: ,{v}')

def validate_json(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError as err:
        return err

JsonString = """{"name": "Raji", "salary": 25000, "email": "raji@mymail.com"}"""

print(f'Json {JsonString} is valid? {validate_json(JsonString)}')