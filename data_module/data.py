import json
data = []
maxed_list = set()
ingredients = {}

try:
  with open('json/data.json') as file:
    data = json.load(file)
except FileNotFoundError:
  print("No data file found. Please run:")
  print("cp data_module/data.json.template json/data.json")

with open('json/maxed_fish.json') as file:
  maxed_list = set(json.load(file))

with open('json/ingredients.json') as file:
  ingredients = json.load(file)

def save_data():
  with open('json/data.json', 'w') as file:
    json.dump(data, file, indent=2)
