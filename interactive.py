from data_module.data import data, save_data, ingredients, maxed_list, create_backup
from util import *
from collections import Counter


def reset():
  if input("Are you sure you want to reset all levels to 1? (y/N) ") != 'y':
    return
  if input("Would you like to make a backup first? (Y/n) ") != 'n':
    create_backup()
  for recipe in data:
     recipe['current_level'] = 1
  print("Levels reset to 1")
  save_data()


def get_recipe():
  name = input("Enter recipe name: ")
  recipes = fuzzy_find_recipe(name)

  if not recipes:
    print("No recipes found")
    return

  print("Recipes Found:")
  for recipe in recipes:
    format_recipe(recipe)

def get_recipe_from_ingredient():
  name = input("Enter ingredient name: ").strip()

  ingredients = set(fuzzy_find_ingredients(name))

  if not ingredients:
    print("No ingredients found")
    return

  for recipe in data:
    for fish in recipe['fish']:
      if fish['fish_name'] in ingredients:
        format_recipe(recipe)
  

def calculate_amounts(filters={}):
  amounts = Counter()
  search_list = []
  filter_boss_items = False

  if not filters.get("ingredient"):
    search_list = set([fish for category in ingredients for fish in ingredients[category]])
    filter_boss_items = True

  else:
    search_list = filters.get("ingredient") 
    if not len(search_list):
      print("No ingredients found")
      return

  for recipe in data:
    if filter_boss_items and recipe['recipe_name'] in maxed_list:
      continue

    if filters.get("num_ingredients", len(recipe['fish'])) != len(recipe['fish']):
      continue

    return_val = Counter(calculate_cost(recipe))
    all_keys = set(amounts.keys()).union(set(return_val.keys()))

    amounts = Counter(
      {key: return_val[key] + amounts[key] for key in all_keys if key in search_list}
    )

  amounts = sorted(amounts.items(), key=lambda x: x[1], reverse=True)

  if filters.get("category"):
    category = filters.get("category")
    ings = set(
      [fish for cat, fish_list in ingredients.items() 
       if category.lower() in cat.lower() for fish in fish_list]
    )
    amounts = [(fish, amount) for fish, amount in amounts if fish in ings]
    
  format_ingredients(dict(amounts))


def upgrade_recipe():
  name = input("Enter recipe name: ").strip()

  recipes = fuzzy_find_recipe(name)

  text = "Which recipe would you like to upgrade?"
  index = choice_picker(text, list(map(lambda x: x['recipe_name'], recipes)))

  if index is None:
    print("No recipes found")
    return

  recipe = recipes[index]

  while True:
    try:
      print(f"\nRecipe: {recipe['recipe_name']} (Level: {recipe['current_level']})")
      inp = input("Enter new level (blank for +1): ")

      if not inp:
        level = recipe['current_level'] + 1

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


def calculate_recipe():
  search_list = []
  name = input("Enter recipe name (blank for all): ").strip()

  if not name:
    search_list = data

  else:
    search_list = fuzzy_find_recipe(name)
  
  if not search_list:
    print("No recipes found")
    return
  
  print("Cost per Recipe:\n")
  for recipe in search_list:
    print(f"{recipe['recipe_name']}:")
    for fish, amount in calculate_cost(recipe).items():
      print(f"  {fish}: {amount}")
    print()

