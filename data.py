import json
data = []

with open('data.json') as file:
    data = json.load(file)


def save_data():
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)
