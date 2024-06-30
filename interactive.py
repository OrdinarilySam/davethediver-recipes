from data_module.data import data, save_data, ingredients
from util import *
from collections import Counter


def reset():
  if input("Are you sure you want to reset all levels to 1? (y/n) ") != 'y':
    return
  for recipe in data:
     recipe['current_level'] = 1
  print("Levels reset to 1")


def get_recipe(name=None):
  if not name:
    name = input("Enter recipe name: ")

  recipes = fuzzy_find_recipe(name)

  print("Recipes Found:")

  for recipe in recipes:
    format_recipe(recipe)

def get_recipe_from_ingredient(name=None):
  if not name:
    name = input("Enter ingredient name: ")

  ingredients = set(fuzzy_find_ingredients(name))

  for recipe in data:
    for fish in recipe['fish']:
      if fish['fish_name'] in ingredients:
        format_recipe(recipe)
  
def calculate_amounts(name=None, category=None):
  amounts = Counter()
  search_list = []

  if not name:
    search_list = set([fish for category in ingredients for fish in ingredients[category]])
  else:
    search_list = fuzzy_find_ingredients(name)
    if not len(search_list):
      print("No ingredients found")
      return

  for recipe in data:
    return_val = Counter(calculate_cost(recipe))
    all_keys = set(amounts.keys()).union(set(return_val.keys()))

    amounts = Counter({key: return_val[key] + amounts[key] for key in all_keys if key in search_list})

  amounts = sorted(amounts.items(), key=lambda x: x[1], reverse=True)
    

  if category:
    ings = set([fish for cat, fish_list in ingredients.items() if category in cat for fish in fish_list])
    amounts = [(fish, amount) for fish, amount in amounts if fish in ings]
    
  format_ingredients(dict(amounts))


def upgrade_recipe(name=None):
  if not name:
    name = input("Enter recipe name: ").strip()

  recipes = fuzzy_find_recipe(name)

  if not len(recipes):
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
      print(f"\nRecipe: {recipe['recipe_name']} (Level: {recipe['current_level']})")
      inp = input("Enter new level (blank for +1): ")
      if not inp:
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
  print(f"Level set to {level}")


def continuous_upgrade():
  try:
    while True:
      upgrade_recipe()
      print()
  except (EOFError, KeyboardInterrupt):
    print("\nExiting")


def calculate_recipe(name=None):
  search_list = []

  if not name:
    search_list = data
  else:
    search_list = fuzzy_find_recipe(name)
  
  print("Cost per Recipe:\n")
  for recipe in search_list:
    print(f"{recipe['recipe_name']}:")
    for fish, amount in calculate_cost(recipe).items():
      print(f"  {fish}: {amount}")
    print()

