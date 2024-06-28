from data import data


# added extra 0 at start for easier indexing in calculate amounts
level_cost = [0,0,3,4,6,10,15,22,34,51,76,115]


def format_recipe(recipe):
  recipe_string = f"\n{recipe['recipe_name']} (Level {recipe['current_level']})\n"
  for fish in recipe['fish']:
    recipe_string += f"{fish['fish_name']}: {fish['amount']}\n"
  print(recipe_string)


def fuzzy_find_recipe(search):
  found = []
  for recipe in data:
    if search.lower() in recipe['recipe_name'].lower():
      found.append(recipe)
  return found