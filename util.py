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