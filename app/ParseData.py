import json

with open('../tests/resources/testData1.json') as f:
    data = json.load(f)
    
print(data)