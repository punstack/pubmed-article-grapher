import json

with open('test.json', 'r', encoding = 'utf-8') as f:
    json_data = json.load(f)

#print(json.dumps(json_data, indent = 4))

for document in json_data[0]['documents']:
    print("Document ID:", document['id'])
    for passage in document['passages']:
        for key, value in passage['infons'].items():
            if key.startswith('name_'):
                surname, given_names = value.split(";given-names:")
                surname = surname.split(":")[1]
                print(f"Author: {given_names} {surname}")
        print("Title:", passage.get('text'))
        print('-'*40)
