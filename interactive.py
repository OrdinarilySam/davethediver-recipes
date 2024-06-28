from data import data, save_data
from util import *
from collections import Counter


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
  amounts = Counter()
  search_list = []

  if name is None:
    search_list = data
  else:
    search_list = fuzzy_find_recipe(name)

  for recipe in search_list:
    amounts += Counter(calculate_cost(recipe))
  
  format_ingredients(dict(amounts))


def upgrade_recipe(name=None):
  if name is None:
    name = input("Enter recipe name: ").strip()

  recipes = fuzzy_find_recipe(name)

  if len(recipes) == 0:
    print("No recipes found")
    return

  if len(recipes) > 1:
    for index, recipe in enumerate(recipes):
      print(index + 1, end=": ")
      print(recipe['recipe_name'])

    print("Which recipe would you like to upgrade?")

    while True:
      try:
        choice = int(input(f"Enter choice 1-{len(recipes)}: "))
        if choice < 1 or choice > len(recipes):
          raise ValueError
        break

      except ValueError:
        print("Invalid choice")
    
    recipe = recipes[choice - 1]
  else:
    recipe = recipes[0]

  while True:
    try:
      inp = input(f"Current level: {recipe['current_level']}\nEnter new level (blank for +1): ")
      if inp == '':
        level = recipe['current_level'] + 1
        break
      else:
        level = int(inp)
        if level < 1 or level > 10:
          raise ValueError
        break

    except ValueError:
      print("Invalid level")
  
  recipe['current_level'] = level
  save_data()
  print(f"Level for {recipe['recipe_name']} set to {level}")


def calculate_recipe(name=None):
  search_list = []

  if name is None:
    search_list = data
  else:
    search_list = fuzzy_find_recipe(name)
  
  print("Cost per Recipe:\n")
  for recipe in search_list:
    print(f"{recipe['recipe_name']}:")
    for fish, amount in calculate_cost(recipe).items():
      print(f"  {fish}: {amount}")
    print()

