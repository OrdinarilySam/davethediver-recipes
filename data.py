import json
data = []
maxed_list = set()

with open('data.json') as file:
  data = json.load(file)

with open('maxed_fish.json') as file:
  maxed_list = set(json.load(file))

def save_data():
  with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)
