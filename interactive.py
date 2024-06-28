import json
data = []

# added extra 0 at start for easier indexing in calculate amounts
level_cost = [0,0,3,4,6,10,15,22,34,51,76,115]


with open('data.json') as f:
    data = json.load(f)

def reset():
  if input("Are you sure you want to reset all levels to 1? (y/n) ") != 'y':
    return
  for recipe in data:
     recipe['current_level'] = 1
  print("Levels reset to 1")

def get_recipe(name=None):
  if name is None:
    name = input("Enter recipe name: ")

  out = []

  for recipe in data:
    if recipe['recipe_name'].lower().startswith(name.lower()):
      out.append(recipe)

  print("Recipes Found:")

  for recipe in out:
    print()
    print(f"{recipe['recipe_name']}: {recipe['current_level']}")

    for fish in recipe['fish']:
      print(f"  {fish['fish_name']}: {fish['amount']}")

  print()
    

def calculate_all_amounts():
  amounts = {} 

  for recipe in data:
    for fish in recipe['fish']:
      fish_name = fish['fish_name']

      if fish_name not in amounts.keys():
        amounts[fish_name] = 0

      for level in range(recipe['current_level'] + 1, len(level_cost) - 1):
        fish_cost = fish['amount']

        match fish_cost:
          case 1:
            amounts[fish_name] += level_cost[level]

          case 2:
            amounts[fish_name] += level_cost[level + 1]

          case 3:
            amounts[fish_name] += level_cost[level] * 2 + (level % 2) # +1 if upgrading to odd level

          case 5:
            amounts[fish_name] += level_cost[level] * 3 + (level % 2) # +1 if upgrading to odd level

          case _:
            print("Invalid fish cost for " + fish_name)

  for fish in amounts:
    print(fish + ": " + str(amounts[fish]))

def calculate_amount():
  ...

def find_recipe_by_ingredient():
  ...

def find_recipe_by_name():
  ...

def upgrade_recipe():
  ...

