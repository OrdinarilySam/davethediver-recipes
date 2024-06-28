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


def upgrade_recipe():
  ...


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

