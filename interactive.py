from data import data, save_data
from util import *


def reset():
  if input("Are you sure you want to reset all levels to 1? (y/n) ") != 'y':
    return
  for recipe in data:
     recipe['current_level'] = 1
  print("Levels reset to 1")


def get_recipe(name=None):
  if name is None:
    name = input("Enter recipe name: ")

  recipes = fuzzy_find_recipe(name)

  print("Recipes Found:")

  for recipe in recipes:
    format_recipe(recipe)


def calculate_amounts(name=None):
  amounts = {} 
  search_list = []

  if name is None:
    search_list = data
  else:
    search_list = fuzzy_find_recipe(name)

  for recipe in search_list:
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

  format_ingredients([{"fish_name": fish, "amount": amounts[fish]} for fish in amounts])


def upgrade_recipe():
  ...


def format_ingredients(ingredients):
  done = []
  still_needed = []

  for fish in ingredients:
    if fish['amount'] == 0:
      done.append(fish['fish_name'])
    else:
      still_needed.append(fish)
    
  print("Done:")
  for fish in done:
    print(fish)
  print()
  
  longest_fish_name = max([len(fish['fish_name']) for fish in still_needed])

  print("\nStill Needed:")
  for fish in still_needed:
    print(f"{fish['fish_name']:>{longest_fish_name}}: {str(fish['amount'])}")
  print()
